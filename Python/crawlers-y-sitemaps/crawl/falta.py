import re
import urllib.parse

import aiohttp
import functools
import lxml.html
import selenium.common.exceptions
import selenium.webdriver
import selenium.webdriver.common.proxy
from utils import *


class Crawl(Sem):
    def __init__(self):
        super().__init__(sem=Sems.CRAWL)
        self.url = 'https://coinspectator.com/projects'
        self.site = False
        self.browser = Browser.CLASS
        self.browser_action = 'icon.icon-chevron-with-circle-down'
        self.browser_maximum = 7
        self.browser_real = 5
        self.todo = set()
        self.busy = set()
        self.done = {}
        self.extracted = {}
        self.megagroups = None
        self.error = 0
        self.patterns = ['http://t.me/', 'https://t.me/', 'http://www.t.me/', 'https://www.t.me/',
                         'http://telegram.me/', 'https://telegram.me/', 'http://www.telegram.me/',
                         'https://www.telegram.me/']

    async def add(self, urls):
        for url, parenturl in urls:
            url = urllib.parse.urljoin(parenturl, url)
            url, frag = urllib.parse.urldefrag(url)
            if url.startswith(self.url) and url not in self.busy and url not in self.done and url not in self.todo:
                self.todo.add(url)
                # functools.partial(self.source)
                source = await self.run(coro=await self.process(url))
                await self.parse(url, source)

    async def process(self, url):
        l = log()
        l.i(msg='Start process: url: {}, browser: {})'.format(url, self.browser))
        source = None
        error = ''
        self.todo.remove(url)
        if self.browser is None:
            headers = {"Referer": "https://www.google.com/search?",
                       "Accept": "text/html,application/xhtml+xml, application/xml;q=0.9,*/*;q=0.8",
                       "Accept_Language": "en", "DNT": "0", "Content-Language": "en-US",
                       "Content-Type": "text/html; charset=utf-8",
                       "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) "
                                     "AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10"}
            try:
                async with aiohttp.ClientSession(headers=headers, trust_env=True) as session:
                    async with session.get(url) as response:
                        if response.status is 200 and ('text/html' in response.headers.get('content-type')):
                            source = (await response.read()).decode('utf-8', 'replace')
                        else:
                            error = 'Aiohttp: url: {}, status: {}'.format(url, response.status)
            except asyncio.TimeoutError:
                print('timeout!')
            except Exception as exc:
                error = 'Aiohttp: url: {}, exception: {}'.format(url, repr(str(exc)))
                raise
            finally:
                if error:
                    l.e(msg=error)
                else:
                    l.s(msg='End process: url: {}, browser: {})'.format(url, self.browser))
        else:
            proxy = selenium.webdriver.common.proxy.Proxy()
            proxy.proxy_type = selenium.webdriver.common.proxy.ProxyType.MANUAL
            proxy.http_proxy = os.getenv('privoxy_host_port', 'NULL')
            proxy.add_to_capabilities(selenium.webdriver.DesiredCapabilities.FIREFOX)
            firefox = selenium.webdriver.Firefox(desired_capabilities=selenium.webdriver.DesiredCapabilities.FIREFOX)
            firefox.implicitly_wait(params.browser_implicit_wait)
            try:
                firefox.get(url)
            except selenium.common.exceptions.TimeoutException as exception:
                error = 'Browser - opening - url: {}, exception: {}'.format(url, repr(exception))
            except selenium.common.exceptions.WebDriverException as exception:
                error = 'Browser - opening - url: {}, exception: {}'.format(url, repr(exception))
            finally:
                tree = lxml.html.fromstring(firefox.page_source)
                title = tree.xpath('/html/head/title/text()')
                try:
                    if title[0] == 'Server Not Found':
                        error = 'Browser - {0} - {2} - url: {1}'.format(
                            title[0], url, tree.xpath('// *[ @ id = "errorShortDescText"]/text()')[0])
                except IndexError as exception:
                    error = 'Browser - invalid - url: {}, exception: {}'.format(url, repr(exception))
                finally:
                    if error:
                        l.e(msg=error)
                    else:
                        for i in range(1, self.browser_maximum):
                            try:
                                if self.browser == Browser.CLICK:
                                    firefox.find_element_by_link_text(self.browser_action).click()
                                elif self.browser == Browser.SCROLL:
                                    firefox.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                elif self.browser == Browser.CLASS:
                                    firefox.find_element_by_class_name(self.browser_action).click()
                                elif self.browser == Browser.CSS:
                                    firefox.find_element_by_css_selector(self.browser_action).click()
                                elif self.browser == Browser.XPATH:
                                    firefox.find_element_by_xpath(self.browser_action).click()
                            except selenium.common.exceptions.NoSuchElementException and \
                                    selenium.common.exceptions.NoSuchWindowException as exception:
                                if i < self.browser_real:
                                    error = 'Browser: {} - {} out of {} times - url: {}, exception: {}'.format(
                                        self.browser, i, self.browser_maximum - 1, url,
                                        repr(exception))
                            except selenium.common.exceptions.WebDriverException as exception:
                                error = 'Browser: {} - {} out of {} times - url: {}, exception: {}'.format(
                                    self.browser, i, self.browser_maximum - 1, url, repr(exception))
                            finally:
                                if error:
                                    l.e(msg=error)
                                else:
                                    l.i(msg='Browser: {} - {} out of {} times - url:{}'.format(
                                        self.browser, i, self.browser_maximum - 1, url))
                                    await asyncio.sleep(params.browser_load_sleep)
                        if not error:
                            l.s(msg='End source: url: {}, browser: {})'.format(url, self.browser))
                            source = firefox.page_source()
                firefox.quit()
        self.done[url] = True
        print('Tasks: {} - completed: {} - pending: {} - todo: {} - error: {} - extracted: {} - megagroups:{}'.format(
            self.url, len(self.done), len(self.tasks), len(self.todo), self.error, len(self.extracted),
            self.megagroups))
        return source

    async def parse(self, url, source):
        l = log()
        if source:
            l.i(msg='Start parse: url: {}'.format(url))

            urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', source)

            results = await Sem(Sems.CRAWL).gather(
                *[Curl.url(turl) for turl in {*urls} for pattern in self.patterns if pattern in turl])
            extracted = await Url.aiochild_get(url)
            await Sem().gather(*[Url.aiochild_update(url, extracted_url=telegram) for telegram in {*results} if
                                 telegram not in extracted])

            self.extracted[url] = True
            self.megagroups = await Url.aiochild_count(url)

            if self.site or self.browser:
                if self.browser:
                    self.browser = None
                await asyncio.create_task(self.add([(u, url) for u in urls]))
            l.s(msg='End parse: url: {}'.format(url))

        else:
            self.error += 1


async def crawl():
    l = log()

    l.s(msg='START: crawl(Url) == {}'.format(await Extracted.aiocount()))

    await asyncio.create_task(Crawl().add([('https://coinspectator.com/projects', '')]))
    l.s(msg='END: crawl(Url) == {}'.format(await Extracted.aiocount()))
    #
    # l.s(msg='START: crawl(Megagroup) == {}'.format(await MegaGroup.aiocount()))
    # megagroup = await MegaGroup.aioall()
    # await Sem().gather(*[MegaGroup.aioupdate(url=row.extracted_url) for row in await Extracted.aioall() if
    #                      row.extracted_url not in megagroup])
    # l.s(msg='END: crawl(Megagroup) == {})'.format(await MegaGroup.aiocount()))


if __name__ == '__main__':
    run(crawl)
