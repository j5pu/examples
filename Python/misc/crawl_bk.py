from lib.log import logger
import asyncio
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from dataclasses import dataclass
import sqlite3
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, Bundle
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import inspect
from sqlalchemy import MetaData
from sqlalchemy.engine import reflection

import concurrent.futures
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.selector import Selector
from scrapy.utils.python import to_native_str
from six.moves.urllib.parse import urljoin
from twisted.internet import reactor, defer
from random import randint
from lxml import html
log = logger()

class Browser:
    def __init__(self, url, click_text='', click_times=0, click_delay=3, scroll_times=0, scroll_delay=3):
        self.url = url
        self.click_text = click_text
        self.click_times = click_times
        self.click_delay = click_delay
        self.scroll_times = scroll_times
        self.scroll_delay = scroll_delay
        self.error = False
        self.error_message = ''
        self.proxy = Proxy()
        self.proxy.proxy_type = ProxyType.MANUAL
        self.proxy.http_proxy = '127.0.0.1:9950'
        self.capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.proxy.add_to_capabilities(self.capabilities)
        self.firefox = webdriver.Firefox(desired_capabilities=self.capabilities)
        self.firefox.implicitly_wait(30)

    def download(self):
        if self.open():
            if self.click() is False:
                self.quit()
                return False
        else:
            self.quit()
            return False
        return self.scroll()

    def click(self):
        l = log.child()
        if self.click_times != 0:
            for i in range(1, self.click_times):
                try:
                    self.firefox.find_element_by_link_text(self.click_text).click()
                    message = 'Click: {} out of {} times - url={}'.\
                        format(i, self.click_times - 1, self.url)
                    l.info(message)
                except NoSuchElementException and NoSuchWindowException as exception:
                    if self.url == "https://icorating.com/ico/all/" and i >= 161:
                        return True
                    self.error = True
                    self.error_message = 'Click error: {} out of {} times - url={} - Exception: {}'. \
                        format(i, self.click_times - 1, self.url, repr(exception))
                    l.error(self.error_message)
                    self.quit()
                    return False
                except WebDriverException as exception:
                    self.error = True
                    self.error_message = 'Click error: {} out of {} times - url={} - Exception: {}'.\
                        format(i, self.click_times - 1, self.url, repr(exception))
                    l.error(self.error_message)
                    self.quit()
                    return False
                finally:
                    time.sleep(self.click_delay)
        return True

    def scroll(self):
        l = log.child()

        if self.scroll_times != 0:
            for i in range(1, self.scroll_times):
                # Nota: hacer un try?
                try:
                    self.firefox.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    message = 'Scroll: {} out of {} times - url={}'.\
                        format(i, self.scroll_times - 1, self.url)
                    l.info(message)
                except WebDriverException as exception:
                    self.error = True
                    self.error_message = 'Scrolling error time={} out of {} times with url={} - Exception: {}'.\
                        format(i, self.scroll_times - 1, self.url, repr(exception))
                    l.error(self.error_message)
                    self.quit()
                    return False
                finally:
                    time.sleep(self.scroll_delay)
        page_source = self.firefox.page_source
        self.quit()
        return page_source

    def open(self):
        l = log.child()

        try:
            self.firefox.get(self.url)
        except WebDriverException as exception:
            self.error = True
            self.error_message = 'Error opening url={} - Exception: {}'.format(self.url, repr(exception))
            l.error(self.error_message)
        finally:
            tree = html.fromstring(self.firefox.page_source)
            title = tree.xpath('/html/head/title/text()')
            try:
                if title[0] == 'Server Not Found':
                    error = tree.xpath('// *[ @ id = "errorShortDescText"]/text()')

                    self.error = True
                    self.error_message = '{0} - {2} - url={1}'.format(title[0], self.url, error[0])
                    l.error(self.error_message)
            except IndexError as exception:
                self.error = True
                self.error_message = 'Invalid url={} - Exception: {}'.format(self.url, repr(exception))
                l.error(self.error_message)
            if self.error:
                self.quit()
                return False
            else:
                return True

    def close(self):
        self.firefox.close()

    def quit(self):
        self.firefox.quit()


def browser():
    crawl_url = "https://tgram.io/topic/29/it/cryptocurrency"
    page = Browser(url=crawl_url, scroll_times=12)
    page_source = page.download()
    if page_source is False:
        log.error('Error downloading page source for url: {}'.format(crawl_url))
    else:
        log.info('Success: source code for url: {}'.format(crawl_url))
        file = 'cryptocurrency.html'
        try:
            with open(file, 'w') as f:
                f.write(format(page_source))
            log.info('Success: source code for url: {} - saved to {}'.format(crawl_url, file))
        except:
            log.info('Error: source code for url: {} - not saved to {}'.format(crawl_url, file))

    crawl_url = "https://tgram.io/topic/51/it/crypto-mining"
    page = Browser(url=crawl_url, scroll_times=2)
    page_source = page.download()
    if page_source is False:
        log.error('Error downloading page source for url: {}'.format(crawl_url))
    else:
        log.info('Success: source code for url: {}'.format(crawl_url))
        file = 'crypto-mining.html'
        try:
            with open(file, 'w') as f:
                f.write(format(page_source))
            log.info('Success: source code for url: {} - saved to {}'.format(crawl_url, file))
        except:
            log.info('Error: source code for url: {} - not saved to {}'.format(crawl_url, file))

    crawl_url = "https://icorating.com/ico/all/"
    page = Browser(url=crawl_url, click_text='Show more', click_times=180)
    page_source = page.download()
    if page_source is False:
        log.error('Error downloading page source for url: {}'.format(crawl_url))
    else:
        log.info('Success: source code for url: {}'.format(crawl_url))
        file = 'corating.html'
        try:
            with open(file, 'w') as f:
                f.write(format(page_source))
            log.info('Success: source code for url: {} - saved to {}'.format(crawl_url, file))
        except:
            log.info('Error: source code for url: {} - not saved to {}'.format(crawl_url, file))


class Scrapy(scrapy.Spider):
    name = 'icobench'
    start_urls = ['https://icobench.com/icos', ]
    custom_settings = scrapy_settings_icobench
    def __init__(self):
        super(Scrapy, self).__init__(self)
        self.class_groups_count = 0
        self.class_groups_urls = set()

    def parse(self, response):
        # follow links to ico pages
        # <a href="/ico/chimaera-1" class="image" style="background-image:url('/images/icos/icons/chimaera-1.jpg');"> </a>

        # 1.- Cada pagina de https://icobench.com/icos:
        # Primer for: tiene que ir al enlace de la ICO (response.follow) y el resultado en parse_ico
        for ico in response.css('div.image_box a.image::attr(href)').extract():

            yield response.follow(ico, self.parse_ico)

        # follow pagination links
        # <a class="next" href="/icos?page=2">Next»</a>
        # 2.- Cada pagina de https://icobench.com/icos:
        # Segundo for: mira la siguiente pagina con lista de ICOs y vuelve a (parse)  tratarla.
        for a in response.css('div.pages a.next::attr(href)').extract():

            yield response.follow(a, callback=self.parse)

    # Viene del primer for: con contenido de la ICO (response.follow) y aqui saca los grupos
    def parse_ico(self, response):
        # <a onclick="ga('send', 'event', 'ICOprofile', 'Telegram', 'XAYA');" rel="nofollow" href="https://t.me/xaya_en" target="_blank" title="XAYA on Telegram" class="telegram">Telegram</a>
        ico_tg_url = response.css('div.socials a.telegram::attr(href)').extract_first()

        if ico_tg_url is not None:

            self.class_groups_count += 1
            self.class_groups_urls.update(ico_tg_url)

            log.info('{} : {} - URL : {}'.format(type(self).__name__, self.class_groups_count, ico_tg_url))

        global icobench_urls
        global icobench_count
        icobench_urls = self.class_groups_urls
        icobench_count = self.class_groups_count

class Icoinsider(scrapy.Spider):
    name = 'icoinsider'
    start_urls = [
        'http://icoinsider.tech/crypto-telegram-groups-channels',
        'https://icoinsider.tech/crypto-telegram-groups-channels-chinese',
    ]
    custom_settings = scrapy_settings_icoinsider

    def __init__(self):
        super(Icoinsider, self).__init__(self)
        self.class_groups_count = 0
        self.class_group_urls = set()

    def parse(self, response):
        random_ip_change()

        # ico_name_list = response.css('div.td-page-content a::text').extract()
        ico_tg_url_list = response.css(
            'div.td-page-content a::attr(href)').extract()

        for ico_tg_url in ico_tg_url_list:
            if ico_tg_url is not None \
               and 'icoinsider' not in ico_tg_url \
               and '/cdn-cgi' not in ico_tg_url:

                self.class_groups_count += 1
                self.class_group_urls.update(ico_tg_url)

                log.info('{} : {} - URL : {}'.format(type(self).__name__, self.class_groups_count, ico_tg_url))

            global icoinsider_urls
            global icoinsider_count
            icoinsider_urls = self.class_group_urls
            icoinsider_count = self.class_groups_count
# https://stackoverflow.com/questions/39776377/cant-get-scrapy-to-parse-and-follow-301-302-redirects
class Icorating(scrapy.Spider):
    name = 'icorating'
#    start_urls = ['https://icorating.com/ico',
#                  'https://icoratings.com/ico?url=https:%3A%2F%icorating.com/ico%2F']
    start_urls = ['https://icorating.com/ico',
                  'https://icoratings.com/ico?url=https://icorating.com/ico']
    custom_settings = scrapy_settings_icorating
    handle_httpstatus_list = [301, 302]

    def __init__(self):
        super(Icorating, self).__init__(self)
        self.class_groups = 0

    def parse(self, response):
        print('------------------------------- location ')
        print(location)
        log.info("got response %d for %r" % (response.status, response.url))
        if response.status >= 300 and response.status < 400:
            # HTTP header is ascii or latin1, redirected url will be percent-encoded utf-8
            location = to_native_str(response.headers['location'].decode('latin1'))
            print('------------------------------- location ')
            print(location)
            # get the original request
            request = response.request
            # and the URL we got redirected to
            redirected_url = urljoin(request.url, location)
            print('------------------------------- redirected_url ')
            print(redirected_url)
            if response.status in (301, 307) or request.method == 'HEAD':
                redirected = request.replace(url=redirected_url)
                print('------------------------------- redirected HEAD 301 307')
                print(redirected)
                yield redirected
            else:
                redirected = request.replace(url=redirected_url, method='GET', body='')
                redirected.headers.pop('Content-Type', None)
                redirected.headers.pop('Content-Length', None)
                print('------------------------------- redirected GET')
                print(redirected)
                yield redirected
        print('------------------------------- response ')
        print(response)

        bodies = response.selector.xpath('//tbody').extract()
        print('------------------------------- bodies ')
        print(bodies)
        txt = '//tr/@data-href'
        print('------------------------------- txt ')
        print(txt)
        ico_url_list = Selector(text=bodies[1]).xpath(txt).extract()
        print('------------------------------- ico_url_list ')
        print(ico_url_list)
        tmp_list = Selector(text=bodies[2]).xpath(txt).extract()
        print('------------------------------- tmp_list ')
        print(tmp_list)
        ico_url_list.extend(tmp_list)

        # follow links to ico pages
        for ico in ico_url_list:
            print('------------------------------- ico ')
            print(ico)
            random_ip_change()
            yield response.follow(ico, self.parse_ico)

    def parse_ico(self, response):

        # ico_name = response.css('div.h1 h1::text').extract_first()
        txt = 'div.uk-child-width-expand.uk-grid-small.uk-text-center'
        print('------------------------------- txt ')
        print(txt)
        social = response.css(txt).extract_first()
        print('------------------------------- social ')
        print(social)
        tmp_list = Selector(text=social).xpath('//a').extract()
        print('------------------------------- tmp_list ')
        print(tmp_list)
        tg_list = [x for x in tmp_list if 'Telegram' in x]
        print('------------------------------- tg_list ')
        print(tg_list)
        txt = '//@href'

        if len(tg_list):
            print('------------------------------- text=tg_list[0] ')
            print(text=tg_list[0])
            ico_tg_url = Selector(text=tg_list[0]).xpath(txt).extract_first()
            self.class_groups += 1
            log.info('{} : {} - URL : {}'.format(type(self).__name__, self.class_groups, ico_tg_url))
            groups_list.append(ico_tg_url)

        global icorating
        icorating = self.class_groups


class Icorating(scrapy.Spider):
    name = 'icorating'
    start_urls = ['https://icorating.com/ico', ]
    custom_settings = scrapy_settings_icorating

    def __init__(self):
        super(Icorating, self).__init__(self)
        self.class_groups = 0

    def parse(self, response):
        print('------------------------------- response ')
        print(response)

        bodies = response.selector.xpath('//tbody').extract()
        print('------------------------------- bodies ')
        print(bodies)
        txt = '//tr/@data-href'
        print('------------------------------- txt ')
        print(txt)
        ico_url_list = Selector(text=bodies[1]).xpath(txt).extract()
        print('------------------------------- ico_url_list ')
        print(ico_url_list)
        tmp_list = Selector(text=bodies[2]).xpath(txt).extract()
        print('------------------------------- tmp_list ')
        print(tmp_list)
        ico_url_list.extend(tmp_list)

        # follow links to ico pages
        for ico in ico_url_list:
            print('------------------------------- ico ')
            print(ico)
            random_ip_change()
            yield response.follow(ico, self.parse_ico)

    def parse_ico(self, response):

        # ico_name = response.css('div.h1 h1::text').extract_first()
        txt = 'div.uk-child-width-expand.uk-grid-small.uk-text-center'
        print('------------------------------- txt ')
        print(txt)
        social = response.css(txt).extract_first()
        print('------------------------------- social ')
        print(social)
        tmp_list = Selector(text=social).xpath('//a').extract()
        print('------------------------------- tmp_list ')
        print(tmp_list)
        tg_list = [x for x in tmp_list if 'Telegram' in x]
        print('------------------------------- tg_list ')
        print(tg_list)
        txt = '//@href'

        if len(tg_list):
            print('------------------------------- text=tg_list[0] ')
            print(text=tg_list[0])
            ico_tg_url = Selector(text=tg_list[0]).xpath(txt).extract_first()
            self.class_groups += 1
            log.info('{} : {} - URL : {}'.format(type(self).__name__, self.class_groups, ico_tg_url))
            groups_list.append(ico_tg_url)

        global icorating
        icorating = self.class_groups

class Icotracker(scrapy.Spider):
    name = 'icotracker'
    start_urls = [
        'https://icotracker.net/current',
        'https://icotracker.net/upcoming',
        'https://icotracker.net/past',
    ]
    custom_settings = scrapy_settings_icotracker

    def __init__(self):
        super(Icotracker, self).__init__(self)
        self.class_groups_count = 0
        self.class_group_urls = set()

    def parse(self, response):
        random_ip_change()

        content = response.css('div.card.card-project').extract()

        for ico in content:
            a_list = Selector(text=ico).xpath('//a').extract()

            tg_list = [x for x in a_list if 'Telegram' in x]

            if len(tg_list):
                txt = 'a::attr(href)'
                ico_tg_url = Selector(text=tg_list[0]).css(txt).extract_first()

                self.class_groups_count += 1
                self.class_group_urls.update(ico_tg_url)

                log.info('{} : {} - URL : {}'.format(type(self).__name__, self.class_groups_count, ico_tg_url))

            global icotracker_urls
            global icotracker_count
            icotracker_urls = self.class_group_urls
            icotracker_count = self.class_groups_count


class Tgramio(scrapy.Spider):
    name = 'tgramio'
    start_urls = [
        'https://tgram.io/topic/29/it/cryptocurrency',
        'https://tgram.io/topic/51/it/crypto-mining',
    ]
    custom_settings = scrapy_settings_tgramio

    def __init__(self):
        super(Tgramio, self).__init__(self)
        self.class_groups_count = 0
        self.class_group_urls = set()

    def parse(self, response):
        random_ip_change()

        ico_name_list = response.css('h3.h6 a::text').extract()

        ico_tg_url_list = response.css(
            'a.btn.btn-outline-danger::attr(href)').extract()

        for idx, ico_name in enumerate(ico_name_list):
            if ico_tg_url_list[idx] is not None:
                self.class_groups_count += 1
                self.class_group_urls.update(ico_tg_url_list[idx])

                log.info('{} : {} - URL : {}'.format(type(self).__name__, self.class_groups_count, ico_tg_url_list[idx]))

            global tgramio_urls
            global tgramio_count
            tgramio_urls = self.class_group_urls
            tgramio_count = self.class_groups_count


class Tokenmarket(scrapy.Spider):
    name = 'tokenmarket'
    start_urls = [
        'https://tokenmarket.net/ico-calendar',
        'https://tokenmarket.net/ico-calendar/upcoming',
        'https://tokenmarket.net/ico-calendar/past',
    ]
    custom_settings = scrapy_settings_tokenmarket

    def __init__(self):
        super(Tokenmarket, self).__init__(self)
        self.class_groups_count = 0
        self.class_group_urls = set()

    def parse(self, response):

        # follow links to ico pages
        txt = 'td.col-asset-name div a::attr(href)'
        for ico in response.css(txt).extract():
            random_ip_change()

            yield response.follow(ico, self.parse_ico)

    def parse_ico(self, response):
        random_ip_change()

        # Nota: Cambio esta
        #div_list = response.css('div.col-md-6').extract()
        #
        # link_list = [x for x in div_list if 'Links' in x]
        # if not len(link_list):
        #     return
        #
        # td_list = Selector(text=link_list[0]).css('td').extract()
        # txt = 'a::attr(href)'
        # tg_list = [x for x in td_list if 'Telegram chat' in x
        #            and 'not available' not in x]
        #
        div_list = response.css('div.communications-wrapper').extract()

        a_list = Selector(text=div_list[0]).css('a').extract()
        txt = 'a::attr(href)'
        tg_list = [x for x in a_list if 'Telegram chat' in x
                   and 'not available' not in x]
        if len(tg_list):
            ico_tg_url = Selector(text=tg_list[0]).css(txt).extract_first()

            self.class_groups_count += 1
            self.class_group_urls.update(ico_tg_url)

            log.info('{} : {} - URL : {}'.format(type(self).__name__, self.class_groups_count, ico_tg_url))


        global tokenmarket_urls
        global tokenmarket_count
        tokenmarket_urls = self.class_group_urls
        tokenmarket_count = self.class_groups_count



class Trackico(scrapy.Spider):
    name = 'trackico'
    start_urls = ['https://www.trackico.io', ]
    custom_settings = scrapy_settings_trackico

    def __init__(self):
        super(Trackico, self).__init__(self)
        self.class_groups_count = 0
        self.class_group_urls = set()

    def parse(self, response):
        # follow links to ico pages

        for ico in response.css('a.card-body::attr(href)').extract():
            random_ip_change()

            yield response.follow(ico, self.parse_ico)

        # follow pagination links

        # Nota: cambio este
        # txt = 'a.btn.btn-w-sm.btn-light::attr(href)'
        txt = 'a.page-link::attr(href)'

        next_list = response.css(txt).extract()
        if len(next_list) == 1:
            next = next_list[0]
        else:
            next = next_list[1]

        random_ip_change()

        yield response.follow(next, callback=self.parse)

    def parse_ico(self, response):
        random_ip_change()

        # Nota cambio este
        # txt = 'a.btn.azm-social.azm-btn.azm-twitter'
        # ico_tgtw_list = response.css(txt).extract()
        # ico_tg_list = [x for x in ico_tgtw_list if 'Telegram' in x]
        # ico_tg_url = None
        # if len(ico_tg_list):
        #     ico_tg_url = Selector(text=ico_tg_list[0]).css(
        #         'a::attr(href)').extract_first()


        txt = 'a.btn.btn-square.btn-telegram::attr(href)'
        # txt = 'a.btn.btn-square.btn-telegram.m-1.text-white::attr(href)'
        ico_tg_url = response.css(txt).extract_first()

        if ico_tg_url is not None:
            self.class_groups_count += 1
            self.class_group_urls.update(ico_tg_url)

            log.info('{} : {} - URL : {}'.format(type(self).__name__, self.class_groups_count, ico_tg_url))

        global trackico_urls
        global trackico_count
        trackico_urls = self.class_group_urls
        trackico_count = self.class_groups_count


def scrapy():
    # Nota: Alt 1 secuencial
    # @log_exc
    # @defer.inlineCallbacks
    # def crawl(runner):
    #     global counter
    #     global groups
    #     groups = []
    #     site_groups = []
    #     counter = 0
    #
    #     log.info('Start Crawling: {}'.format('Icobench'))
    #
    #     yield runner.crawl(Icobench)
    #
    #     sleep(5)
    #     num_site_groups = len(site_groups)
    #     groups.append(site_groups)
    #     num_groups = len(groups)
    #     log.info('Commpleted Crawling: {} with {} groups - Total: {}'.format('IpEcho1',  num_groups - num_site_groups, num_groups))
    #
    #     reactor.stop()
    #
    # @log_exc
    # def groups():
    #     # NOTA: NUnca cambiar el orden de estos tres
    #     runner = CrawlerRunner()
    #     crawl(runner)
    #     reactor.run()

    runner = CrawlerRunner()

    #    runner.crawl(Icobench)
    #    runner.crawl(Icoinsider)
    #    runner.crawl(Icotracker)
    runner.crawl(Scrapy)
    #    runner.crawl(Tokenmarket)
    #    runner.crawl(Trackico)

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run()  # the script will block here until all crawling jobs are finished


def blocking_io():
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    with open('/dev/urandom', 'rb') as f:
        return f.read(100)


def cpu_bound():
    # CPU-bound operations will block the event loop:
    # in general it is preferable to run them in a
    # process pool.
    return sum(i * i for i in range(10 ** 7))


async def crawl():
    l = log.child()

    loop = asyncio.get_running_loop()

    # Options:
    # Use functools.partial() to pass keyword arguments to func.

    # 1. Run in the default loop's executor:
    result = await loop.run_in_executor(
        None, groups)
    print('default thread pool', result)

    # 2. Run in a custom thread pool:
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, groups)
        print('custom thread pool', result)

    # 3. Run in a custom process pool:
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, groups)
        print('custom process pool', result)


@dataclass
class Url:
    key: int
    url: str
    steps: str
    click_text: str
    click_class : str
    click_times: int
    click_times_real: int
    click_delay: int
    scroll_times : int
    scroll_times_real: int
    scroll_delay: int
    extract_text: str
    extract_class : str
    urls: int
    urls_previous: int
    urls_visited: int
    urls_visited_previous : int
    url_errors: int
    url_errors_previous: int
    groups: int
    groups_previous : int

    def __init__(self):
        self.__conn = sqlite3.connect('tbot.db')



        cursor = self.__conn.cursor()

        cursor.execute('SELECT * FROM crawl_urls')
        rows = cursor.fetchall()
        for row in rows:
            print(row)


def crawl():
    l = log.child()


conn = sqlite3.connect('tbot.db')

cursor = conn.cursor()

cursor.execute('SELECT * FROM crawl_urls')
rows = cursor.fetchall()
for row in rows:
    print(row[1])



Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine("sqlite:///tbot.db", echo=True)

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
urls = Base.classes.crawl_urls

session = Session(engine)

# for row in session.query(urls.key).all()[1:20]:
#     print(row)
inspector = inspect(engine)

# Get table information
print(inspector.get_table_names())

# Get column information
print(inspector.get_columns('crawl_urls'))

# Create a MetaData instance
metadata = MetaData()
print(metadata.tables)

# reflect db schema to MetaData
metadata.reflect(bind=engine)
print(metadata.tables)

# Create MetaData instance
metadata = MetaData(engine, reflect=True)
print(metadata.tables)

# Get Table
ex_table = metadata.tables['crawl_urls']
print(ex_table)
insp = reflection.Inspector.from_engine(engine)
print(insp.get_table_names())

inspector = inspect(engine)

print(inspector.get_columns('crawl_urls'))
print(inspector.get_indexes('crawl_urls'))
print(inspector.get_primary_keys('crawl_urls'))
print(inspector.get_sorted_table_and_fkc_names())
print(inspector.get_pk_constraint('crawl_urls'))
print(inspector.get_foreign_keys('crawl_urls'))
print(inspector.default_schema_name)
print(inspector.get_schema_names())
print(inspector.get_table_names())
print(inspector.get_table_options('crawl_urls'))
print(inspector.get_temp_table_names())
print(inspector.get_temp_view_names())
print(inspector.get_unique_constraints('crawl_urls'))
print(inspector.get_view_definition(inspector.get_view_names()))
print(inspector.get_view_names())
meta = MetaData()
table = Table('crawl_urls', meta)
print(inspector.reflecttable(table, None))
print(session.__repr__())
for row, o in session.query(urls.key, urls.url).all():
    print(row, o)
for row in urls.__table__.columns.keys():
    print(row)


def test_orm_full_objects_list():
    """Load fully tracked ORM objects into one big list()."""

    sess = Session(engine)
    objects = list(sess.query(urls).limit(500))
    return objects
print(test_orm_full_objects_list())

def test_orm_full_objects_chunks():
    """Load fully tracked ORM objects a chunk at a time using yield_per()."""

    sess = Session(engine)
    for obj in sess.query(urls).yield_per(1000).limit(500):
        print(obj)

print(test_orm_full_objects_chunks())

def test_orm_bundles():
    """Load lightweight "bundle" objects using the ORM."""

    sess = Session(engine)
    bundle = Bundle('url', urls.key, urls.url)
    for row in sess.query(bundle).yield_per(10000).limit(500):
        print(row)

print(test_orm_bundles())

def test_orm_columns():
    """Load individual columns into named tuples using the ORM."""

    sess = Session(engine)
    for row in sess.query(urls.key, urls.url).yield_per(10000).limit(500):
        print(row)

print(test_orm_columns())

def test_core_fetchall():
    """Load Core result rows using fetchall."""

    with engine.connect() as conn:
        result = conn.execute(urls.__table__.select().limit(500)).fetchall()
        for row in result:
            print(row)

            data = row['key'], row['url']
            print(data)

print(test_core_fetchall())

def test_core_fetchmany_w_streaming():
    """Load Core result rows using fetchmany/streaming."""

    with engine.connect() as conn:
        result = conn.execution_options(stream_results=True).execute(urls.__table__.select().limit(500))
        while True:
            chunk = result.fetchmany(10000)
            if not chunk:
                break
            for row in chunk:
                print(row)
                data = row['key'], row['url']
                print(data)

print(test_core_fetchmany_w_streaming())

def test_core_fetchmany():
    """Load Core result rows using Core / fetchmany."""

    with engine.connect() as conn:
        result = conn.execute(urls.__table__.select().limit(500))

        print(result)
        while True:
            chunk = result.fetchmany(10000)
            if not chunk:
                break
            for row in chunk:
                print(row)

                data = row['key'], row['url']
                print(data)

print(test_core_fetchmany())

def mia():
    """Load Core result rows using Core / fetchmany."""

    with engine.connect() as conn:
        result = conn.execute(urls.__table__.select())
        for row in result:
            print(row)
            data = row['key'], row['url']
            print(data)

print(mia())

def mia1():
    """Load Core result rows using Core / fetchmany."""
    for row in engine.connect().execute(urls.__table__.select()):
        print(row)


mia1()
# DeclarativeBase = declarative_base()
# metadata = DeclarativeBase.metadata
# metadata.bind = engine
#
#
# # configure Session class with desired options
# Session = sessionmaker()
#
# # associate it with our custom Session class
# Session.configure(bind=engine)
#
# # work with the session
# session = Session()
# d = {k: metadata.tables[k].columns.keys() for k in metadata.tables.keys()}
# print(d)
# rudimentary relationships are produced
# session.add(Address(email_address="foo@bar.com", user=User(name="foo")))
# session.commit()

# collection-based relationships are by default named
# "<classname>_collection"
if __name__ == '__main__':
    #asyncio.run(crawl())
    crawl()