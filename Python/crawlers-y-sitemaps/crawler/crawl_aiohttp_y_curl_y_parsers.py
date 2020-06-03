import http.client
import urllib.parse

import lxml.etree
import lxml.html
import requests.adapters
import selenium.common.exceptions
import selenium.webdriver
import selenium.webdriver.chrome.options
import selenium.webdriver.common.proxy
import selenium.webdriver.firefox.options
import urllib3.util.retry
from utils import *


@contextlib.asynccontextmanager
async def executor(func, pool: Executor = Executor.NONE):
    l = log()
    loop = asyncio.get_event_loop()

    if not func:
        raise ValueError

    if pool == Executor.THREAD:
        with concurrent.futures.ThreadPoolExecutor() as thread_pool:
            l.t('Custom executor: thread_pool == {}, func  == {}'.format(thread_pool, func))
            yield await loop.run_in_executor(thread_pool, func)
    elif pool == Executor.PROCESS:
        with concurrent.futures.ProcessPoolExecutor() as process_pool:
            l.t('Custom executor: process_pool  == {}, func  == {}'.format(process_pool, func))
            yield await loop.run_in_executor(process_pool, func)
    else:
        # 3. Run in the default loop's executor (blocking_io):
        l.t('Default executor:  loop == {}, func  == {}'.format(loop, func))
        yield await loop.run_in_executor(None, func)

class Net(Sem):
    t_patterns = ['http://t.me/', 'https://t.me/', 'http://www.t.me/', 'https://www.t.me/', 'http://telegram.me/',
                  'https://telegram.me/', 'http://www.telegram.me/', 'https://www.telegram.me/']
    header_content_type = {"Content-Type": "text/html; charset=utf-8"}
    header_accept_language = {"Accept-Language": "en"}
    header_content_language = {"Content-Language": "en-US"}
    header_dnt = {"DNT": "0"}
    header_accept = {'Accept': 'text/html'}
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) " \
                 "Version/5.1.3 Safari/534.53.10"

    class Client(Enum):
        REQUESTS = enum.auto()
        FIREFOX = enum.auto()
        AIOHTTP = enum.auto()
        CURL = enum.auto()
        WGET = enum.auto()
        FILE = enum.auto()
        DIR = enum.auto()
        NONE = enum.auto()

    class Parser(Enum):
        SELF = enum.auto()
        REGEX = enum.auto()
        LXML = enum.auto()
        SOUP = enum.auto()
        MIO = enum.auto()

        SOUP_TEXT = enum.auto()
        GREP = "grep -Po '(?<=link=\")[^\"]*(?=\")|(?<=href=\")[^\"]*(?=\")'"

    @staticmethod
    def referer(url):
        return 'https://www.google.com/search?q={}&ie=utf-8&oe=utf-8&client=firefox-b-ab'.format(url)

    @staticmethod
    def get_headers(url):
        return {**Net.header_content_type, **Net.header_accept_language, **Net.header_content_language,
                **Net.header_dnt, **Net.header_accept, "User-Agent": Net.user_agent,
                "Referer": Net.referer(url)}

    @staticmethod
    async def ip_ok(ip):
        l = log()
        try:
            socket.inet_aton(ip)
            l.t('IP == {}'.format(ip))
            return ip
        except socket.error or OSError:
            l.d('IP == Error from {}'.format(ini['default']['ip_url']))

    @staticmethod
    async def parse(url, source, parser: Parser = Parser.MIO):
        l = log()
        try:
            if parser is Net.Parser.GREP:
                if os.path.isdir(source) or os.path.isfile(source):
                    stdin = None
                    Net.Parser.GREP.value = Net.Parser.GREP.value + " -R " + source
                else:
                    stdin = source
                returncode, stdout, stderr = await funcs.aiocmd(Net.Parser.GREP.value, stdin=stdin)

                msg = '{}: returncode == {}, {}'.format(url, returncode, '{}'.format(
                    '') if returncode is 0 else 'stderr == {}'.format(stderr.rstrip('\n')), Net.Parser.GREP.value)
                log().i(msg) if int(returncode) is 0 else log().e(msg)

                if int(returncode) is 0 and stdout:
                    return stdout.rstrip("';").rstrip("/")
            elif Net.Parser.MIO:
                return re.findall(r'(?<=href=")[^"]*(?=")', source) + \
                       re.findall(r'(?<=link=")[^"]*(?=")', source)
            elif parser is Net.Parser.REGEX:
                return re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', source) + \
                       re.findall(r'(?i)link=["\']?([^\s"\'<>]+)', source)
            elif parser is Net.Parser.SOUP or parser is Net.Parser.SOUP_TEXT:
                soup = bs4.BeautifulSoup(source, 'html.parser')
                soup.decode('utf-8')
                if parser is Net.Parser.SOUP_TEXT:
                    return soup.get_text()
                return [link.get('href') for link in soup.find_all('a')] + \
                       [link.get('link') for link in soup.find_all('tr')] + \
                       [link.get('href') for link in soup.find_all('link')] + \
                       [link.get('data-href') for link in soup.find_all('div')]
            elif parser is Net.Parser.LXML:
                xml = u'<?xml version="1.0" encoding="utf-8" ?><foo><bar/></foo>'
                xml = bytes(bytearray(xml, encoding='utf-8'))
                lxml.etree.XML(xml)
                tree = lxml.html.fromstring(source)
                return [url_tag.attrib.get('href', '') for url_tag in tree.findall('.//a')] + \
                       [url_tag.attrib.get('link', '') for url_tag in tree.findall('.//tr')] + \
                       [url_tag.attrib.get('href', '') for url_tag in tree.findall('.//link')] + \
                       [url_tag.attrib.get('data-href', '') for url_tag in tree.findall('.//div')]
            else:
                l.c()
                raise AttributeError
        except ValueError as exc:
            if 'Unicode strings with encoding declaration are not supported' in repr(exc):
                l.c('{}: {}, source[{}]'.format(url, repr(exc), source))
        except TypeError as exc:
            if 'expected string or bytes-like object' in repr(exc):
                l.c('{}: {}, source[{}]'.format(url, repr(exc), source))
        except lxml.etree.ParserError as exc:
            if 'Document is empty' in repr(exc):
                l.c('{}: {}, tree_error_log[{}], source[{}]'.format(url, exc.error_log.filter_from_level(
                    lxml.etree.ErrorLevels.WARNING), repr(exc), source))
        except BaseException as exc:
            l.x('{}: {}, source[{}]'.format(url, repr(exc), source))

    @staticmethod
    def config_wget(url=None):
        cmd = 'wget'
        cmd_dir = "{}{}".format(ini[cmd]['dir_prefix'], cmd)
        cmd_log = "{0}/{1}.log".format("/var/log", cmd)
        if url:
            _, url_dom, url_rel, _, _, _ = urllib.parse.urlparse(url)
            url_dir = "/".join(i for i in [cmd_dir, url_dom.strip("/"), url_rel.strip("/")] if i.strip("/"))
            os.system("mkdir -p {}".format(url_dir))
            return url_dir
        else:
            os.system("mkdir -p {}".format(cmd_dir))
            os.system('rm -f {}'.format(cmd_log))
            return cmd, cmd_dir, cmd_log

    @staticmethod
    @contextlib.asynccontextmanager
    async def wget(url, mirror=True, wait=20, tries=20, backups=4, background=True, debug=False, quiet=False,
                   verbose=False, no_clobber=False, cont=True, random_wait=True, no_cache=True,
                   secure_protocol=True, https_only=True, no_check_certificate=True, robots=True,
                   ignore_length=True, timestamping=True, retry_connrefused=True):
        kwargs = locals().items()
        cmd = wget_cmd
        for k, v in kwargs:
            if k is 'robots' and v:
                cmd = '{} --execute robots=off'.format(cmd, k, v)
            elif k is 'cont' and v:
                cmd = '{} --continue'.format(cmd, k, v)
            elif k is 'secure_protocol' and v:
                cmd = '{} --secure-protocol=auto'.format(cmd)
            elif type(v) is int:
                cmd = '{} --{}={}'.format(cmd, k, v)
            elif v is True:
                cmd = '{} --{}'.format(cmd, k.replace('_', '-'))

        _, url_dom, _, _, _, _ = urllib.parse.urlparse(url)
        cmd = "{} {} {} {} {} {} {} {} {} {} {} {}"\
            .format(cmd, "--append-output='{}'".format(wget_log),
                    "--directory-prefix='{}'".format(wget_dir),
                    "--header='{}: {}'".format(*Net.header_content_type.keys(), *Net.header_content_type.values()),
                    "--header='{}: {}'".format(*Net.header_accept_language.keys(),
                                               *Net.header_accept_language.values()),
                    "--header='{}: {}'".format(*Net.header_content_language.keys(),
                                               *Net.header_content_language.values()),
                    "--header='{}: {}'".format(*Net.header_dnt.keys(), *Net.header_dnt.values()),
                    "--header='{}: {}'".format(*Net.header_accept.keys(), *Net.header_accept.values()),
                    "--user-agent='{}'".format(Net.user_agent),
                    "--referer='{}'".format(Net.referer(url_dom)),
                    "--local-encoding='utf-8'"
                    "--accept='*.html,*.php,*.htm' --reject='*.aac,*.abw,*.arc,*.avi,*.azw,*.bin,*.bmp,*.bz,*.bz2,"
                    "*.csh,*.css,*.csv,*.doc,*.docx,*.eot,*.epub,*.es,*.gif,*.ico,*.ics,*.jar,*.jpeg,*.jpg,*.js,"
                    "*.json,*.mid,*.midi,*.mpeg,*.mpkg,*.odt,*.oga,*.ogv,*.ogx,*.otf,*.png,*.pdf,*.ppt,*.pptx,*.rar,"
                    "*.rtf,*.sh,*.svg,*.swf,*.tar,*.tif,*.tiff,*.ts,*.ttf,*.txt,*.vsd,*.wav,*.weba,*.webm,*.webp,"
                    "*.woff,*.woff2,*.xhtml,*.xls,*.xlsx,*.xml,*.xul,*.zip,*.3gp,*.3gp2,*.7z' "
                    "--ignore-tags='img,script' --inet4-only", format(url))
        returncode, stdout, stderr = await funcs.aiocmd(cmd)
        msg = '{}: returncode == {}, {}, {}'.format(url, returncode,
                                                    'stdout == {}'.format(stdout.rstrip('\n')) if returncode is 0
                                                    else 'stderr == {}'.format(stderr.rstrip('\n')), cmd)
        log().i(msg) if int(returncode) is 0 else log().e(msg)

        if background and int(returncode) is 0 and 'Continuing in background, pid ' in stdout:
            while psutil.pid_exists(int(stdout.strip('Continuing in background, pid ').rstrip('.\n'))):
                log().n('Waiting for {}: pid == {}'.format(url, int(stdout.strip('Continuing in background, pid ').
                                                                    rstrip('.\n'))))
                await asyncio.sleep(random.randint(40, 120))
        log().s('{}: pid == {}'.format(url, int(stdout.strip('Continuing in background, pid ').rstrip('.\n'))))

        yield await Net(Net.config_wget(url)).get

    @staticmethod
    @contextlib.asynccontextmanager
    async def file(name, html=True):
        with open(name) as response:
            if html:
                yield response.read()
            else:
                yield [line.rstrip('\n') for line in response.readlines()]

    @staticmethod
    @contextlib.asynccontextmanager
    async def dir(name):
        await Sem().gather(*[Net(os.path.join(root, file)).get for root, _, files in os.walk(name) for file in files])
        yield
    """
        https://topicolist.com/  <tr link=entera
        https://thebitcoinnews.com/ <a href=entera
        https://foundico.com/ <a href=/relativa.html
        https://www.smithandcrown.com/ <a href=/relativa/
        https://icobench.com/ <a href=relativa#trozo_en_relativa (se puede quitar trozo asi coge entera relativa)    
    """

    @staticmethod
    async def update(root_url, t_eurls):
        try:
            extracted_added = 0
            if root_url:
                extracted = await Crawl.aiochild_count(root_url)
                for t_eurl in t_eurls:
                    if await Crawl.aiochild_count(root_url, 'extracted_url', t_eurl) is 0:
                        await Crawl.aiochild_update(root_url, extracted_url=t_eurl)
                extracted_added = await Crawl.aiochild_count(root_url) - extracted

            megagroup = await MegaGroup.aiocount()
            for t_eurl in t_eurls:
                if await MegaGroup.aiocount('url', t_eurl) is 0:
                    await MegaGroup.aioupdate(url=t_eurl)
            megagroup_added = await MegaGroup.aiocount() - megagroup
            return extracted_added, megagroup_added
        except (BrokenPipeError, IOError) as exc:
            log().c('Restarting mysql: {}'.format(repr(exc)))
            returncode, stdout, stderr = await funcs.aiocmd('sudo service mysql restart')
            if returncode is 0:
                log().s('Restarted succesful mysql: {}'.format(repr(exc)))
                await asyncio.sleep(20)
                await Net.update(root_url, t_eurls)
            else:
                raise

    @staticmethod
    async def t(url):
        schema, netloc, path, _, _ = urllib.parse.urlsplit(url)
        return urllib.parse.urlunsplit((schema, netloc, path, _, _))

    def __init__(self, url=None, client: Client = Client.REQUESTS, links=True, firefox: Firefox = Firefox.NONE,
                 firefox_arg=None, firefox_times=1, firefox_real=1, t_eurl=True, headless=True,
                 parser: Parser = Parser.MIO, background=True, site=True, root_url=None):
        """
            print('---------------------------------------------------------------------------------------------')
            n = Net(client=Net.Client.AIOHTTP)
            await n.get
            print('AIOHTTP - ip: ', n.ip)
            print('AIOHTTP - eurl: ', n.eurl)
            print('AIOHTTP - links: ', n.links)
            print('---------------------------------------------------------------------------------------------')
            n = Net()
            await n.get
            print('REQUESTS - ip: ', n.ip)
            print('REQUESTS - eurl: ', n.eurl)
            print('REQUESTS - links: ', n.links)
            print('REQUESTS - ip: ', await Net().get)
            print('REQUESTS - eurl: ', await Net('http://ipecho.net', links=None).get)
            print('REQUESTS - links: ', await Net('http://ipecho.net').get)
            print('---------------------------------------------------------------------------------------------')
            n = Net(client=Net.Client.CURL)
            await n.get
            print('CURL - ip: ', n.ip)
            print('CURL - eurl: ', n.eurl)
            print('CURL - links: ', n.links)
            print('CURL - ip: ', await Net('https://ipecho.net', client=Net.Client.CURL).get)
            print('CURL - eurl: ', await Net('https://ipecho.net', client=Net.Client.CURL, links=None).get)
            print('CURL - links: ', await Net('https://ipecho.net', client=Net.Client.CURL).get)

            print('---------------------------------------------------------------------------------------------')
            n = Net(client=Net.Client.FIREFOX)
            await n.get
            print('FIREFOX - ip: ', n.ip)
            print('FIREFOX - eurl: ', n.eurl)
            print('FIREFOX - links: ', n.links)
            print('FIREFOX - ip: ', await Net(client=Net.Client.FIREFOX).get)
            print('FIREFOX - eurl: ', await Net('http://ipecho.net', Net.Client.FIREFOX, None).get)
            print('FIREFOX - links: ', await Net('http://ipecho.net', client=Net.Client.FIREFOX).get)

            for row in crawl_rows:
                # Para links y t_eurls (self.t_eurls los mete en sql) devuelve links
                if row.url == 'https://tgram.io/topic/51/it/crypto-mining':
                    links = await Net(row.url, Net.Client.FIREFOX, True, row.firefox, row.firefox_arg,
                    row.firefox_times,
                              row.firefox_real).get

        :param url: 1- No url return ip y GET, 2- Si url = dir -> parse ficheros 3- Si url fichero y no HTML -> telegram
        :param client:
        :param links: Si links True return links. False, return eurl
        :param firefox:
        :param firefox_arg:
        :param firefox_times:
        :param firefox_real:
        :param: t_eurl: return links y actualiza extracted y megagroups on los t_eurls extraidos
        :param headless:
        :param parser:
        :param background:
        :param site:
        """
        super().__init__()
        self.root_url = root_url
        self.url = url
        self.name = client

        if self.url:
            self.ip = None
            if os.path.isdir(self.url):
                self.name = Net.Client.DIR
                self.GET = self.dir(self.url)
            elif os.path.isfile(self.url):
                if "htm" in self.url:
                    self.name = Net.Client.FILE
                    self.GET = self.file(self.url)
                else:
                    self.name = Net.Client.NONE
                    self.GET = self.file(self.url, False)
            elif not self.url:
                self.url = ip_url
            elif not self.root_url:
                schema, netloc, rel_url, _, _, _ = urllib.parse.urlparse(self.url)
                count = 0
                for crawl in crawl_rows:
                    if netloc in crawl.url:
                        self.root_url = crawl.url
                        count += 1
                if count > 1:
                    u = urllib.parse.urlunparse((schema, netloc, rel_url, _, _, _))
                    for crawl in crawl_rows:
                        if u in crawl.url:
                            self.root_url = crawl.url
                            break
        else:
            self.url = ip_url
            self.ip = True

        self.text = None
        self.links = links
        self.eurl = None if links else True
        self.parser = parser
        self.firefox = firefox
        self.t_urls = None
        self.t_eurls = t_eurl
        self.headers = self.get_headers(self.url) if self.root_url else 'telegram'

        if self.name is Net.Client.FIREFOX:
            # profile_path = "/home/fp/.mozilla/firefox"
            # profile = selenium.webdriver.FirefoxProfile(profile_path)
            # profile.set_preference("network.proxy.type", 1)
            # profile.set_preference("network.proxy.socks", local_ip)
            # profile.set_preference("network.proxy.socks_port", 9981)
            # profile.set_preference("network.proxy.socks_version", 5)
            # profile.update_preferences()
            # self.client = selenium.webdriver.Firefox(profile=profile, proxy=proxy,
            #                                          service_log_path='/var/log/geckodriver.log', options=options,
            #                                       desired_capabilities=selenium.webdriver.DesiredCapabilities.FIREFOX)
            proxy = selenium.webdriver.common.proxy.Proxy(selenium.webdriver.common.proxy.ProxyType.SYSTEM)
            options = selenium.webdriver.FirefoxOptions()
            options.headless = headless
            self.client = selenium.webdriver.Firefox(service_log_path='/var/log/geckodriver.log', options=options,
                                                     desired_capabilities=selenium.webdriver.DesiredCapabilities.
                                                     FIREFOX, proxy=proxy)
            self.client.implicitly_wait(ini.getint('default', 'browser_implicit_wait'))
            self.firefox = firefox
            if self.firefox is not Firefox.NONE:
                self.firefox_call = getattr(self.client, firefox.value)
                self.firefox_arg = firefox_arg
                self.firefox_times = firefox_times
                self.firefox_real = firefox_real
                self.click = True if 'CLICK' in self.firefox.name else None
            self.GET = executor(functools.partial(self.client.get, self.url))
        elif self.name is Net.Client.WGET:
            self.background = background
            self.site = site
            self.GET = self.wget(self.url, mirror=self.site, background=self.background)
        elif self.name is Net.Client.REQUESTS:
            http.client.HTTPConnection.debuglevel = ini.getint('default', 'HTTP_debug')
            self.client = requests.Session()
            self.client.headers = self.headers
            self.client.adapter = requests.adapters.HTTPAdapter(max_retries=urllib3.util.retry.Retry(
                total=ini.getint('default', 'retry_total'), status_forcelist=[400, 403, 404, 408, 500, 502, 503, 504],
                backoff_factor=ini.getfloat('default', 'retry_backoff_factor')))
            self.client.mount('http://', self.client.adapter)
            self.client.mount('https://', self.client.adapter)
            self.client.verify = True
            self.client.trust_env = True
            self.GET = executor(functools.partial(self.client.get, self.url))
        elif self.name is Net.Client.AIOHTTP:
            # Nota: Probando
            self.connector = aiohttp.TCPConnector(family=socket.AF_INET, ssl=False)
            self.client = aiohttp.ClientSession(headers=self.headers, connector=self.connector, trust_env=True)
            self.GET = self.client.get(self.url)
        elif self.name is Net.Client.CURL:
            self.response = io.BytesIO()
            self.client = pycurl.Curl()
            self.client.setopt(self.client.URL, self.url)
            self.client.setopt(self.client.FOLLOWLOCATION, 1)
            self.client.setopt(self.client.SSL_VERIFYPEER, 0)
            self.client.setopt(self.client.SSL_VERIFYHOST, 0)
            self.client.setopt(self.client.HTTPHEADER, ['{}: {}'.format(key, value)
                                                        for key, value in self.headers.items()])
            self.client.setopt(self.client.WRITEFUNCTION, self.response.write)
            self.client.setopt(self.client.CAINFO, certifi.where())
            self.GET = executor(self.client.perform)

    @property
    async def get(self):
        l = log()
        prefix = '{}({}):'.format(self.name.name, self.url)
        suffix = ''
        try:
            async with self.GET as response:
                if self.name is Net.Client.FIREFOX:
                    await asyncio.sleep(ini.getint('default', 'browser_load_sleep'))
                    tree = lxml.html.fromstring(self.client.page_source)
                    title = tree.xpath('/html/head/title/text()')
                    try:
                        if self.url is not ip_url:
                            if title[0] == 'Server Not Found':
                                l.e('{}({}), {} == {}'.format(self.name.name, self.url, title[0],
                                                              tree.xpath('// *[ @ id = "errorShortDescText"]/text()')[
                                                                  0]))
                    except IndexError as exc:
                        l.e('{}({}), exc == {}, page_source == {}'.format(self.name.name, self.url, repr(exc),
                                                                          self.client.page_source))
                    else:
                        if self.firefox is not Firefox.NONE:
                            for number in range(1, self.firefox_times + 1):
                                try:
                                    if self.click:
                                        self.firefox_call(self.firefox_arg).click()
                                    else:
                                        self.firefox_call(self.firefox_arg)
                                    l.i('{}({}), {} out of {}'.format(self.name.name, self.url, number,
                                                                      self.firefox_times))
                                    await asyncio.sleep(ini.getint('default', 'browser_load_sleep'))
                                except selenium.common.exceptions.NoSuchElementException or \
                                        selenium.common.exceptions.NoSuchWindowException as exc:
                                    if number < self.firefox_real:
                                        l.w('{}({}), {} of {}, exc == {}'.format(self.name.name, self.url, number,
                                                                                 self.firefox_times, repr(exc)))
                                        break
                                except selenium.common.exceptions.WebDriverException as exc:
                                    l.e('{}({}), {} of {}, exc == {}'.format(self.name.name, self.url, number,
                                                                             self.firefox_times, repr(exc)))
                                    break
                        if self.ip:
                            self.text = await Net.parse(self.url, self.client.page_source, Net.Parser.SOUP_TEXT)
                        else:
                            """
                            Alt 1. 
                                # returns the inner HTML as a string
                                self.text = self.client.execute_script("return document.body.innerHTML")
                            Alt 2. 
                                # igual pero sacando el outerHTML
                                http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Scraping_a_Webpage_Rendered_by_Javascript_Using_Python.php
                                https://code.tutsplus.com/tutorials/modern-web-scraping-with-beautifulsoup-and-selenium--cms-30486

                                self.text = elem.get_attribute("outerHTML").replace('%25', '%').replace('%2F', '/').\
                                replace('%26', '&').replace('%3F', '?').replace('%3D', '=').replace('%23', '#').\
                                replace('%25', '%').replace('%3A', ':')

                                lo cambio por:

                                urllib.parse.unquote()
                            """
                            self.text = urllib.parse.unquote(
                                self.client.find_element_by_xpath("//*").get_attribute("outerHTML"))
                        self.eurl = self.client.current_url
                elif self.name is Net.Client.REQUESTS and response.status_code is 200 \
                        and 'text/html' in response.headers.get('content-type'):
                    self.text = response.text
                    self.eurl = response.url
                elif self.name is Net.Client.AIOHTTP and response.status is 200 \
                        and 'text/html' in response.headers.get('content-type'):
                    self.text = await response.text()
                    self.eurl = response.real_url
                elif self.name is Net.Client.CURL and self.client.getinfo(self.client.RESPONSE_CODE) is 200 \
                        and 'text/html' in self.client.getinfo(self.client.CONTENT_TYPE):
                    self.text = self.response.getvalue().decode()
                    self.eurl = self.client.getinfo(self.client.EFFECTIVE_URL)
                elif self.name is not Net.Client.WGET and not Net.Client.DIR and not Net.Client.FILE \
                        and not Net.Client.NONE:
                    raise ConnectionError
        except selenium.common.exceptions.TimeoutException or selenium.common.exceptions.WebDriverException \
                or asyncio.TimeoutError or pycurl.error or ConnectionError as exc:
            suffix = '{}({}): exc == {}'.format(self.name, self.url, repr(exc))
        except UnicodeDecodeError as exc:
            suffix = '{}({}): exc == {}'.format(self.name, self.url, repr(exc))
        except urllib3.exceptions.MaxRetryError as exc:
                suffix = '{}({}): exc == {}'.format(self.name, self.url, repr(exc))
        except requests.exceptions.InvalidSchema as exc:
                suffix = '{}({}): exc == {}'.format(self.name, self.url, repr(exc))
        except requests.exceptions.RetryError as exc:
                suffix = '{}({}): exc == {}'.format(self.name, self.url, repr(exc))
        except requests.exceptions.MissingSchema as exc:
                suffix = '{}({}): exc == {}'.format(self.name, self.url, repr(exc))
        except TypeError as exc:
            if 'expected string or bytes-like object' in repr(exc):
                suffix = '{}({}): exc == {}'.format(self.name, self.url, repr(exc))
        except ConnectionRefusedError as exc:
            if 'expected string or bytes-like object' in repr(exc):
                suffix = '{}({}): exc == {}'.format(self.name, self.url, repr(exc))
        else:
            try:
                if self.ip:
                    self.ip = await Net.ip_ok(self.text)
                    suffix = 'ip == {}'.format(self.ip)
                    return self.ip
                elif self.links and self.name is not Net.Client.DIR and self.name is not Net.Client.WGET:
                    if self.name is Net.Client.FILE or Net.Client.NONE:
                        self.text = response
                    self.links = await Net.parse(self.url, self.text)
                    self.t_urls = {await self.t(link.lower().rstrip('/')) for link in {*self.links}
                                   for t_pattern in Net.t_patterns if t_pattern in link and '.me/share/' not in link}
                    if self.t_eurls and self.t_urls:
                        self.t_eurls = {*await self.gather(*[Net(t_eurl, links=False).get for t_eurl in self.t_urls])}
                        extracted_added, megagroup_added = await self.update(self.root_url, self.t_eurls)
                        suffix = 'links == {}, t_urls == {}, t_eurls == {} - MySQL added({}): extracted == {}, ' \
                                 'megagroup == {}'.format(len(self.links), len(self.t_urls), len(self.t_eurls),
                                                          self.root_url, extracted_added, megagroup_added)
                        return self.links
                    suffix = 'links == {}, t_urls == {}'.format(len(self.links), len(self.t_urls))
                    return self.links
                elif self.eurl:
                    suffix = 'eurl == {}'.format(self.eurl)
                    return self.eurl
            except TypeError as exc:
                suffix = '{}({}): exc == {}'.format(self.name, self.url, repr(exc))
        finally:
            try:
                l.c('{} {}'.format(prefix, suffix)) if 'exc == ' in suffix else l.v('{} {}'.format(prefix, suffix))

                if self.name is Net.Client.AIOHTTP:
                    await self.client.close()
                    self.connector.close()
                elif hasattr(self, 'client'):
                    self.client.close()
                    if self.name is Net.Client.FIREFOX:
                        self.client.quit()
                        self.client.stop_client()
            except TypeError as exc:
                if 'object NoneType can' in repr(exc):
                    suffix = '{}({}): exc == {}'.format(self.name, self.url, repr(exc))
                    l.c(suffix)


wget_cmd, wget_dir, wget_log = Net.config_wget()
