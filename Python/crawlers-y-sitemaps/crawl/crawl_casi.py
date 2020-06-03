#!/usr/py/bin/python3.7
import functools
import http.client
import urllib.parse

import lxml.etree
import lxml.html
import selenium.common.exceptions
import selenium.webdriver
import selenium.webdriver.common.proxy
from bs4 import BeautifulSoup
from utils import *

aiohttp_connector = aiohttp.TCPConnector(family=socket.AF_INET, ssl=False)
t_patterns = ['http://t.me/', 'https://t.me/', 'http://www.t.me/', 'https://www.t.me/', 'http://telegram.me/',
              'https://telegram.me/', 'http://www.telegram.me/', 'https://www.telegram.me/']


class CrawlMegaGroup(Sem):
    def __init__(self, crawl: Crawl):
        super().__init__(sem=Sems.CRAWL)
        self.root_url = crawl.url
        self.site = crawl.site
        self.browser = crawl.browser
        self.browser_action = crawl.browser_action
        self.browser_maximum = crawl.browser_maximum
        self.browser_real = crawl.browser_real
        self.done = {}
        self.extracted = {}
        self.megagroups = None
        self.error = 0

        self.connector = aiohttp.TCPConnector(family=socket.AF_INET, ssl=False)

        self.todo = set(self.root_url)
        self.do(self.root_url)

    async def info(self, process_url, process_point='-Start-', process_error=False):
        l = log()
        self.megagroups = await Crawl.aiochild_count(self.root_url)
        msg = '({}) - {}({}) tasks: {}, done: {}, ERROR: {}, todo: {}, extracted: {}, megagroups:{}'.format(
            process_point, self.root_url, process_url, len(self.tasks), len(self.done), self.error, len(self.todo),
            len(self.extracted), self.megagroups)
        if process_error:
            l.w(msg)
        elif process_point == '-Start-':
            l.v(msg)
        else:
            l.i(msg)

    @staticmethod
    async def update(url, t_eurl):
        await Crawl.aiochild_update(url, extracted_url=t_eurl)
        megragroup = await MegaGroup.aioall()
        if t_eurl not in megragroup:
            """
            Se ha colado esta en megagroup http://vasexperts.ru/test/blocked.php
            y encima habia 500 en ambos: extracted y megagroups, y en orden alfabetico, raro, raro.
            y hay urls que tienen lo de ?, igual hacer antes quitar los fragmentos antes de probar y tambien
            lo de php y htm que tenia este hombre en el pysitemap, y a lo mejor quitar los duplciados antes de mandar a
            probarlas y cambiar los que sean telegram.me por t.me y quitar www, y ponerlas en https para que asi haya 
              menos duplicados
            Y QUIERO COGER UN PUTO BOT Y PROBAR LOS GRUPOS COÑO
            
            """
            await MegaGroup.aioupdate(url=t_eurl)

    async def is_do(self, crawl_url, page_url):
        crawl_url = urllib.parse.urljoin(crawl_url, page_url)
        crawl_url, frag = urllib.parse.urldefrag(crawl_url)
        if crawl_url.startswith(self.root_url) and crawl_url not in self.done and crawl_url not in self.todo:
            if '#' in crawl_url:
                crawl_url = crawl_url[:crawl_url.find('#')]
            return crawl_url

    @staticmethod
    async def eurl(t_url):
        """
        # print((await executor(
        # functools.partial(requests.get, 'http://techtv.mit.edu/videos/1585-music-session-02/download.source'))).url)
        # print((await executor(functools.partial(requests.get, 'http://ipecho.net/plain'))).content.decode())
        # print((await executor(functools.partial(requests.get, 'http://ipecho.net/plain'))).content.decode())
        # print(requests.get('https://tgram.io/topic/29/it/cryptocurrency').text)
        # print(requests.get('https://tgram.io/topic/29/it/cryptocurrency').links.items())

        :param t_url:
        :return:
        """
        return (await executor(functools.partial(requests.get, t_url))).url

    async def add_t(self, urls):
        for url in urls:
            url, frag = urllib.parse.urldefrag(url)

        t_eurl_tasks = await Sem(Sems.CRAWL).gather(
            *[self.eurl(href) for href in {*urls} for t_pattern in self.t_patterns if t_pattern in href])
        extracted = await Crawl.aiochild_get(self.root_url)
        await Sem().gather(
            *[self.update(self.root_url, t_eurl) for t_eurl in {t_eurl_task.result() for t_eurl_task in t_eurl_tasks} if
              t_eurl not in extracted])



    @staticmethod
    async def parse_regex(url, url_text):
        l = log()
        # hrefs = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', source)

        """
        1.- TEXT_STRING = requests.response.text - (HEADER+BODY en una linea: str object)
                requests.response.text.split('\n') = firefox.page.source 
                firefox.page_source = request.response.text.split('\n')
            A.- En una linea, se usa (asume que el href si es suya esta partido o tiene # para saca url final:
                tree = lxml.html.fromstring(TEXT_STRING)
                for link_tag in tree.findall('.//a'):
                    link = link_tag.attrib.get('href', '')
        2.- CONTENT = requests.response.content = aiohttp.response.read().decode() - (NO HTML: bytes-like object)
            A.- (este no se lo que asume!!, si lo hara con las tres combinaciones: a) partido, b) enterno, c) #
                urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', content)
                def add_url(parenturl, url for url in urls):
                    # Parece que el urljoin es listo y hace lo del # y si es relativo.
                    url = urllib.parse.urljoin(parenturl, url)
                    url, frag = urllib.parse.urldefrag(url)
                    # startswitch compara que son del mismo dominio
                    if url.startswith(self.url)

        https://topicolist.com/  <tr link=entera
        https://thebitcoinnews.com/ <a href=entera
        https://foundico.com/ <a href=/relativa.html
        https://www.smithandcrown.com/ <a href=/relativa/
        https://icobench.com/ <a href=relativa#trozo_en_relativa (se puede quitar trozo asi coge entera relativa)
        """
        # if self.browser:
        #     try:
        #         tree = lxml.html.fromstring(source)
        #     except ValueError as e:
        #         self.errlog(repr(e))
        #         tree = lxml.html.fromstring(source)
        #     for link_tag in tree.findall('.//a'):
        #         link = link_tag.attrib.get('href', '')
        #         newurl = urllib.parse.urljoin(self.url, link)
        #         # print(newurl)
        #         if self.is_valid(newurl):
        #             self.visited.update([newurl])
        #             self.urls.update([newurl])
        # else:
        #     urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', source)
        try:
            return re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', url_text) + \
                   re.findall(r'(?i)link=["\']?([^\s"\'<>]+)', url_text)
        except BaseException as exc:
            error = '{}: {} - source[{}]'.format(url, repr(exc), url_text)
        if error:
            l.x(error)
        # t_eurl_tasks = await Sem(Sems.CRAWL).gather(
        #     *[self.eurl(href) for href in {*todo_urls} for t_pattern in self.t_patterns if t_pattern in href])
        # extracted = await Crawl.aiochild_get(self.root_url)
        # await Sem().gather(*[self.update(self.root_url, t_eurl)
        #                      for t_eurl in {t_eurl_task.result() for t_eurl_task in t_eurl_tasks}
        #                      if t_eurl not in extracted])

    @staticmethod
    async def parse_soup(url, url_text):
        l = log()
        # hrefs = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', source)

        """
        1.- TEXT_STRING = requests.response.text - (HEADER+BODY en una linea: str object)
                requests.response.text.split('\n') = firefox.page.source 
                firefox.page_source = request.response.text.split('\n')
            A.- En una linea, se usa (asume que el href si es suya esta partido o tiene # para saca url final:
                tree = lxml.html.fromstring(TEXT_STRING)
                for link_tag in tree.findall('.//a'):
                    link = link_tag.attrib.get('href', '')
        2.- CONTENT = requests.response.content = aiohttp.response.read().decode() - (NO HTML: bytes-like object)
            A.- (este no se lo que asume!!, si lo hara con las tres combinaciones: a) partido, b) enterno, c) #
                urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', content)
                def add_url(parenturl, url for url in urls):
                    # Parece que el urljoin es listo y hace lo del # y si es relativo.
                    url = urllib.parse.urljoin(parenturl, url)
                    url, frag = urllib.parse.urldefrag(url)
                    # startswitch compara que son del mismo dominio
                    if url.startswith(self.url)

        https://topicolist.com/  <tr link=entera
        https://thebitcoinnews.com/ <a href=entera
        https://foundico.com/ <a href=/relativa.html
        https://www.smithandcrown.com/ <a href=/relativa/
        https://icobench.com/ <a href=relativa#trozo_en_relativa (se puede quitar trozo asi coge entera relativa)
        """
        # if self.browser:
        #     try:
        #         tree = lxml.html.fromstring(source)
        #     except ValueError as e:
        #         self.errlog(repr(e))
        #         tree = lxml.html.fromstring(source)
        #     for link_tag in tree.findall('.//a'):
        #         link = link_tag.attrib.get('href', '')
        #         newurl = urllib.parse.urljoin(self.url, link)
        #         # print(newurl)
        #         if self.is_valid(newurl):
        #             self.visited.update([newurl])
        #             self.urls.update([newurl])
        # else:
        #     urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', source)
        try:
            soup = BeautifulSoup(url_text, 'html.parser')
            return [link.get('href') for link in soup.find_all('a')] + \
                   [link.get('link') for link in soup.find_all('tr')]
        except BaseException as exc:
            error = '{}: {} - source[{}]'.format(url, repr(exc), url_text)

        if error:
            l.x(error)

    @staticmethod
    async def parse_lxml(url, url_text):
        l = log()
        """
        1.- TEXT_STRING = requests.response.text - (HEADER+BODY en una linea: str object)
                requests.response.text.split('\n') = firefox.page.source 
                firefox.page_source = request.response.text.split('\n')
            A.- En una linea, se usa (asume que el href si es suya esta partido o tiene # para saca url final:
                tree = lxml.html.fromstring(TEXT_STRING)
                for link_tag in tree.findall('.//a'):
                    link = link_tag.attrib.get('href', '')
        2.- CONTENT = requests.response.content = aiohttp.response.read().decode() - (NO HTML: bytes-like object)
            A.- (este no se lo que asume!!, si lo hara con las tres combinaciones: a) partido, b) enterno, c) #
                urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', content)
                def add_url(parenturl, url for url in urls):
                    # Parece que el urljoin es listo y hace lo del # y si es relativo.
                    url = urllib.parse.urljoin(parenturl, url)
                    url, frag = urllib.parse.urldefrag(url)
                    # startswitch compara que son del mismo dominio
                    if url.startswith(self.url)

        https://topicolist.com/  <tr link=entera
        https://thebitcoinnews.com/ <a href=entera
        https://foundico.com/ <a href=/relativa.html
        https://www.smithandcrown.com/ <a href=/relativa/
        https://icobench.com/ <a href=relativa#trozo_en_relativa (se puede quitar trozo asi coge entera relativa)
        """
        # if self.browser:
        #     try:
        #         tree = lxml.html.fromstring(source)
        #     except ValueError as e:
        #         self.errlog(repr(e))
        #         tree = lxml.html.fromstring(source)
        #     for link_tag in tree.findall('.//a'):
        #         link = link_tag.attrib.get('href', '')
        #         newurl = urllib.parse.urljoin(self.url, link)
        #         # print(newurl)
        #         if self.is_valid(newurl):
        #             self.visited.update([newurl])
        #             self.urls.update([newurl])
        # else:
        #     urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', source)
        try:
            xml = u'<?xml version="1.0" encoding="utf-8" ?><foo><bar/></foo>'
            xml = bytes(
                bytearray(xml, encoding='utf-8'))  # ADDENDUM OF THIS LINE (when unicode means utf-8, e.g. on Linux)
            lxml.etree.XML(xml)
            tree = lxml.html.fromstring(url_text)
            return [url_tag.attrib.get('href', '') for url_tag in tree.findall('.//a')] + [
                    url_tag.attrib.get('link', '') for url_tag in tree.findall('.//tr')]
        except ValueError as exc:
            if 'Unicode strings with encoding declaration are not supported' in repr(exc):
                l.x('{}: {} - source[{}]'.format(url, repr(exc), url_text))
        except TypeError as exc:
            if 'expected string or bytes-like object' in repr(exc):
                l.x('{}: {} - source[{}]'.format(url, repr(exc), url_text))
        except lxml.etree.ParserError as exc:
            if 'Document is empty' in repr(exc):
                l.x('{}: {} - tree_error_log[{}], source[{}]'.format(url, exc.error_log.filter_from_level(
                    lxml.etree.ErrorLevels.WARNING), repr(exc), url_text))

    @staticmethod
    async def get_aiohttp(url):
        l = log()
        """
        Para: [Get(-Aiohttp-) https://icolink.com/ico-list.html - exc: 'Cannot connect to host 
        icolink.com:443 
               ssl:None [None]']
        https://github.com/aio-libs/aiohttp/issues/2522
            # Create client session that will ensure we dont open new connection
            # per each request.
            async with aiohttp.ClientSession(connector=conn) as session:
        """
        try:
            async with aiohttp.ClientSession(headers=funcs.headers(url), connector=aiohttp_connector, trust_env=True) as session:
                async with session.get(url) as resp:
                    if resp.status is 200 and resp.headers.get('content-type'):
                        return await Crawl.parse_regex(url, await resp.text())
        except asyncio.TimeoutError as exc:
            l.x('{} - exc: {}'.format(url, repr(str(exc))))
        except Exception as exc:
            l.x('{} - exc: {}'.format(url, repr(str(exc))))

    @staticmethod
    async def get_requests(url):
        """
        # print((await executor(
        # functools.partial(requests.get, 'http://techtv.mit.edu/videos/1585-music-session-02/download.source'))).url)
        # print((await executor(functools.partial(requests.get, 'http://ipecho.net/plain'))).content.decode())
        # print((await executor(functools.partial(requests.get, 'http://ipecho.net/plain'))).content.decode())
        # print(requests.get('https://tgram.io/topic/29/it/cryptocurrency').text)
        # print(requests.get('https://tgram.io/topic/29/it/cryptocurrency').links.items())

        :param process_url:
        :return:
        """
        l = log()

        http.client.HTTPConnection.debuglevel = 0
        try:
            resp = await executor(functools.partial(requests.get, url, trust_env=True, headers=funcs.headers(url),
                                                    proxies={'http': os.getenv('http_proxy', 'NULL')}))

            if resp.status_code is 200 and resp.headers.get('content-type'):
                return await Crawl.parse_regex(url, resp.text)
        # except requests.exceptions.SSLError as exc:
        #     l.w(repr(exc))
        except BaseException as exc:
            l.x('{} - exc: {}'.format(url, repr(str(exc))))

    @staticmethod
    async def get_firefox(url, get_action, get_action_info, get_action_times, get_action_real):
        l = log()
        proxy = selenium.webdriver.common.proxy.Proxy()
        proxy.proxy_type = selenium.webdriver.common.proxy.ProxyType.MANUAL
        proxy.http_proxy = os.getenv('PROXY_DOMAIN_PORT', 'NULL')
        proxy.add_to_capabilities(selenium.webdriver.DesiredCapabilities.FIREFOX)
        firefox = selenium.webdriver.Firefox(desired_capabilities=selenium.webdriver.DesiredCapabilities.FIREFOX,
                                             service_log_path='/var/log/geckodriver.log')
        firefox.implicitly_wait(config.ini.getint('default', 'browser_implicit_wait'))
        firefox.start_client()
        try:
            firefox.get(url)
        except selenium.common.exceptions.TimeoutException as exc:
            l.e('{} - exc: {}'.format(url, repr(exc)))
        except selenium.common.exceptions.WebDriverException as exc:
            l.e(' {} - exc: {}'.format(url, repr(exc)))
        else:
            tree = lxml.html.fromstring(firefox.page_source)
            title = tree.xpath('/html/head/title/text()')
            try:
                if title[0] == 'Server Not Found':
                    l.e('{} - {}: {}'.
                        format(url, title[0], tree.xpath('// *[ @ id = "errorShortDescText"]/text()')[0]))
            except IndexError as exc:
                l.e('{} - exc: {}'.format(url, repr(exc)))
            else:
                for i in range(1, get_action_times):
                    try:
                        if get_action == GetAction.CLICK_ELEMENT_LINK_TEXT:
                            firefox.find_element_by_link_text(get_action_info).click()
                        elif get_action == GetAction.EXECUTE_SCRIPT:
                            firefox.execute_script(get_action_info)
                        elif get_action == GetAction.CLICK_ELEMENT_CLASS_NAME:
                            firefox.find_element_by_class_name(get_action_info).click()
                        elif get_action == GetAction.CLICK_ELEMENT_CSS_SELECTOR:
                            firefox.find_element_by_css_selector(get_action_info).click()
                        elif get_action == GetAction.CLICK_ELEMENT_XPATH:
                            firefox.find_element_by_xpath(get_action_info).click()
                        l.i('{} - {} out of {}'.format(url, i, get_action_times - 1))
                        await asyncio.sleep(config.ini.getint('default', 'browser_load_sleep'))
                    except selenium.common.exceptions.NoSuchElementException \
                            and selenium.common.exceptions.NoSuchWindowException as exc:
                        if i < get_action_real:
                            l.w('{} - {} out of {}, exc: {}'.
                                format(url, i, get_action_times - 1, repr(exc)))
                            break
                    except selenium.common.exceptions.WebDriverException as exc:
                        l.e('{} - {} out of {}, exc: {}'.
                            format(url, i, get_action_times - 1, repr(exc)))
                        break
        finally:
            firefox.close()
            firefox.quit()
            firefox.stop_client()

            l.d('End: {}'.format(url))
            if firefox.find_element_by_css_selector("a"):
                return [element.get_attribute('href') for element in
                        firefox.find_elements_by_css_selector("a")] + \
                        [element.get_attribute('link') for element in
                        firefox.find_elements_by_css_selector("tr")]
                # source = firefox.page_source

    async def do(self, url=None):
        l = log()
        await self.info(url, '-Start-')

        if self.browser:
            urls = await self.get_firefox(url, self.browser, self.browser_action, self.browser_maximum,
                                               self.browser_real)
        else:
            urls = await self.get_requests(url)


        if urls:
            await self.add_t(urls)

            urls = await self.add_do(url, urls)
            if urls:
                await self.gather(*[])
        else:
            self.error += 1

        # try:
        #     self.todo.remove(get_url)
        # except KeyError as exc:
        #     if "coinstaker" in str(exc):
        #         l.x('coinstaker')
        self.todo.remove(url)
        self.done[url] = True
        self.extracted[url] = True

        await self.info(url, '-End-', False)


async def crawl():
    l = log()
    await Sem().gather(*[Crawl(crawl) for crawl in crawl_rows])
    l.s('(-End-) - megagroups: {})'.format(await MegaGroup.aiocount()))


if __name__ == '__main__':
    run(crawl)
