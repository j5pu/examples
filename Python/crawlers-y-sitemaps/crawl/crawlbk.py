from utils import log
import utils
import aiohttp
import asyncio
from __init__ import config, Url, Extracted, MegaGroup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.proxy import Proxy, ProxyType
import os
import urllib.parse
import json
import re
import time
import aioify


class Crawl(utils.Sem):
    def __init__(self, row):
        super().__init__()
        self.row = row
        self.url = self.row.url
        self.site = self.row.site
        if self.site:
            self.first = True
        else:
            self.first = False
        self.browser = self.row.browser

        self.retry = True
        self.retry_times = 4
        self.retry_codes = [400, 403, 404, 408, 500, 502, 503, 504]

        self.patterns = ['http://t.me/', 'https://t.me/', 'http://www.t.me/', 'https://www.t.me/',
                         'http://telegram.me/', 'https://telegram.me/', 'http://www.telegram.me/',
                         'https://www.telegram.me/']

        # region Browser
        self.proxy = Proxy()
        self.proxy.proxy_type = ProxyType.MANUAL
        self.proxy.http_proxy = os.getenv('privoxy_host_port', 'NULL')
        self.capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.proxy.add_to_capabilities(self.capabilities)
        self.browser_load_sleep = config.browser_load_sleep
        self.click = self.row.click
        self.times_max = self.row.times_max
        self.times_real = self.row.times_real

        self.client = webdriver.Firefox(desired_capabilities=self.capabilities)

        self.aioget = aioify.aioify(self.client.get)
        self.quit = self.client.quit
        self.close = self.client.close

        self.client.implicitly_wait(config.domain_sleep)
        self.log = self.client.get_log
        self.source = self.client.page_source
        self.command = self.client.find_element_by_link_text(self.click).click() if self.click else \
            self.client.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # endregion Browser

        # region Aiohttp
        if not self.browser:
            self.headers = {'Referer': 'https://www.google.com/search?',
                            'Accept': 'text/html,application/xhtml+xml, application/xml;q=0.9,*/*;q=0.8',
                            'Accept_Language': 'en', 'DNT': 0, 'Content-Language': 'en-US',
                            'Content-Type': 'text/html; charset=utf-8',
                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, '
                                          'like Gecko) Version/5.1.3 Safari/534.53.10'}
            self.client = aiohttp.ClientSession(headers=self.headers, trust_env=True)
            self.aioget = self.client.get
            self.quit = self.client.close
        # endregion Aiohttp

        self.error = 0
        self.todo = set()
        self.busy = set()
        self.done = {}
        self.retries = {}
        self.extracted = {}
        self.megagroups = None

    async def check(self, url, status, headers):
        l = log()
        l.m(msg='status:  == {} - url == {}'.format(status, url))

        if status == 200:
            if 'text/html' in headers:
                return True
            else:
                l.e(msg='status:  == {} - url == {} - text/html not in headers == {}'.format(status, url, headers))

        if status in self.retry_codes:
            if self.retry and self.retries[url] < self.retry_times:
                l.w(msg='resp.status:  == {} - retry == {} : {} out of {} - url == {}'.
                    format(status, self.retry, self.retries[url], self.retry_times, url))
                self.retries[url] += 1
                return False
            else:
                l.e(msg='resp.status:  == {} - retry == {} : {} out of {} - url == {}'.
                    format(status, self.retry, self.retries[url], self.retry_times, url))

        if status != 200 not in self.retry_codes:
            l.e(msg='resp.status:  == {} - url == {}'.format(status, url))

    async def get(self, url):
        url = 'http://ipecho.net/plain'

        l = log()
        error = None
        action_error = None
        status = True
        close = aioify.aioify(self.client.close)
        try:
            response = await self.aioget(url)
            if self.browser:
                print(url)
                response = await aioify.aioify(self.client.get)(url)
                har_response = json.loads(self.log('har')[0]['message'])['log']['entries'][0]['response']
                status = await self.check(url, har_response['status'], har_response['headers'])
                if status:
                    for i in range(1, self.times_max):
                        try:
                            # self.command()
                            l.d(msg='Browser: {} out of {} times - url={}'.format(i, self.times_max, self.url))
                        except NoSuchElementException and NoSuchWindowException:
                            if i < self.times_real:
                                action_error = True
                        except WebDriverException:
                            action_error = True
                        finally:
                            if action_error:
                                l.e(msg='Browser error: {} out of {} times - url={}'.
                                    format(i, self.times_max, self.url), ctx=True)
                                break
                        time.sleep(self.browser_load_sleep)
                    self.done[url] = True
                    return self.source
            else:
                print(url)

                async with self.client.get(url) as response:
                    close = response.release
                    status = await self.check(url, response.status, response.headers.get('content-type'))
                    if status:
                        return (await response.read()).decode('utf-8', 'replace')
        except WebDriverException as exception:
            error = True
            l.e(msg='Error opening url={} - Exception: {}'.format(url, repr(exception)))
        finally:
            if error or action_error or status is None:
                self.error += 1
                self.done[url] = True
            if status is False:
                self.done[url] = False

            self.busy.remove(url)
            await close()

    async def process(self, url):
        l = log()

        self.todo.remove(url)
        self.busy.add(url)

        source = await self.get(url)
        if source:
            urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', source)

            curl = utils.Curl()
            tasks = [asyncio.create_task(curl.sem(utils.aiocurl_eurl, turl)).result() for turl in urls for pattern in
                     self.patterns if
                     pattern in turl]

            await Url.aiochild_add(url, set(await asyncio.gather(*tasks, return_exceptions=True)))
            self.extracted[url] = True

            self.megagroups = await Url.aiochild_count(url)

            """
            Si browser y site y es la primera vez que entro entonces si que agrega las urls para que 
            vuelva
            """
            if self.first:
                await asyncio.Task(self.add([(u, url) for u in urls]))
                if self.browser and self.first:
                    self.first = False

        l.i(msg='Crawl: {} - url: {} - completed: {} - pending: {} - todo: {} - error: {} - extracted: {} - ' \
               'megagroups: {}'.format(self.url, url, len(self.done), len(self.tasks), len(self.todo), self.error,
                                       len(self.extracted), self.megagroups))

    async def add(self, urls):
        for url, parenturl in urls:
            url = urllib.parse.urljoin(parenturl, url)
            url, frag = urllib.parse.urldefrag(url)
            if (url.startswith(self.url) and
                    url not in self.busy and
                    url not in self.done and
                    url not in self.todo):
                self.todo.add(url)
                self.retries[url] = self.retry_times
                await self.sem(self.get, url)

    async def start(self):
        l = log()

        t = asyncio.create_task(self.add([(self.url, '')]))

        await asyncio.sleep(1)
        while self.busy:
            await asyncio.sleep(1)

        await t

        l.s(msg='Crawl: {} - completed: {} - pending: {} - todo: {} - error: {} - extracted: {} - megagroups: {}'
            .format(self.url, len(self.done), len(self.tasks), len(self.todo), self.error, len(self.extracted),
                    self.megagroups))

        await self.quit()


async def crawl():
    l = log()

    l.i(msg='STARTING: crawl(extract)'.format(await Extracted.aiocount()))
    extract = await asyncio.gather([await Crawl(row).start() for row in await Url.aioall()], return_exceptions=True)
    # Nota: No va a ir porque es el objeto de uno no de todos, creo
    l.s(msg='COMPLETED: Crawl({}).rum() - tasks: {} - done: {} - ok: {} - todo: {} - busy: {} - error: {} - '
            'extracted: {} - megagroups: {}'.format(extract.url, len(extract.tasks), len(extract.done),
                                                    sum(extract.done.values()), len(extract.todo),
                                                    len(extract.busy), extract.error, len(extract.extracted),
                                                    extract.megagroups))

    extract.cancel()
    l.i(msg='COMPLETED: crawl(extract.cancel())')
    l.s(msg='COMPLETED: crawl(extract: {})'.format(await Extracted.aiocount()))

    l.i(msg='STARTING: crawl(megagroup)'.format(await MegaGroup.aiocount()))
    megagroup = await MegaGroup.aioall()
    update = await asyncio.gather([MegaGroup.aioupdate(url=row.extracted_url) for row in await Extracted.aioall() if
                                   row.extracted_url not in megagroup], return_exceptions=True)
    update.cancel()
    l.i(msg='COMPLETED: crawl(update.cancel())')
    l.s(msg='COMPLETED: crawl(megagroup: {})'.format(await MegaGroup.aiocount()))


if __name__ == '__main__':
    utils.start(crawl)
