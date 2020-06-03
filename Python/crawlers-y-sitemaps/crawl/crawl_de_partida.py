from utils import log
import aioify
import urllib.parse
import asyncio
import aiohttp
import re
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.proxy import Proxy, ProxyType
import os
import utils
from __init__ import config, Url, Extracted, MegaGroup


class Crawl(utils.Browser, utils.Aiohttp, utils.Sem):
    def __init__(self, row):
        super().__init__()
        self.url = row.url
        self.click = row.click
        self.times_max = row.times_max
        self.times_real = row.times_real

        self.semaphore = asyncio.Semaphore(8)

        # region retry
        # self.retry = True
        # self.retry_times = 4
        # self.retry_codes = [400, 403, 404, 408, 500, 502, 503, 504]
        # self.retries = {}
        # endregion retry
        # region tasks
        self.todo = set()
        self.busy = set()
        self.done = {}
        self.extracted = {}
        self.tasks = set()
        self.megagroups = None
        self.error = 0
        # endregion tasks
        # region extract
        self.patterns = ['http://t.me/', 'https://t.me/', 'http://www.t.me/', 'https://www.t.me/',
                         'http://telegram.me/', 'https://telegram.me/', 'http://www.telegram.me/',
                         'https://www.telegram.me/']
        # endregion extract
        # region Aiohttp
        # self.headers = {"Referer": "https://www.google.com/search?",
        #                 "Accept": "text/html,application/xhtml+xml, application/xml;q=0.9,*/*;q=0.8",
        #                 "Accept_Language": "en", "DNT": "0", "Content-Language": "en-US",
        #                 "Content-Type": "text/html; charset=utf-8",
        #                 "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) "
        #                               "AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10"}
        # self.aiohttp = aiohttp.ClientSession(headers=self.headers, trust_env=True)
        # endregion Aiohttp
        # region Browser
        # self.proxy = Proxy()
        # self.proxy.proxy_type = ProxyType.MANUAL
        # self.proxy.http_proxy = os.getenv('privoxy_host_port', 'NULL')
        # self.capabilities = webdriver.DesiredCapabilities.FIREFOX
        # self.proxy.add_to_capabilities(self.capabilities)
        # self.browser_load_sleep = config.browser_load_sleep
        # self.browser = webdriver.Firefox(desired_capabilities=self.capabilities)
        # self.browser.implicitly_wait(config.browser_implicit_wait)
        self.log = self.browser.get_log
        self.source = self.browser.page_source
        self.aioget = aioify.aioify(self.browser.get)
        self.quit = self.browser.quit
        self.close = self.browser.close
        self.command = self.browser.find_element_by_link_text(
            self.click).click() if self.click else self.browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        # endregion Browser

    async def run(self):
        # t = asyncio.create_task(self.addurls([(self.url, '')]))

        async with utils.Aiohttp():
            await asyncio.create_task(self.addurls([(self.url, '')]))


        # await asyncio.sleep(1)
        # while self.busy:
        #     await asyncio.sleep(1)
        #
        # await t
        # await self.aiohttp.close()

    async def addurls(self, urls):
        print('urls: ', urls)
        for url, parenturl in urls:
            print('url: ', url)
            print('parenturl: ', parenturl)

            url = urllib.parse.urljoin(parenturl, url)
            print('url: ', url)

            url, frag = urllib.parse.urldefrag(url)
            print('url: ', url)

            print('frag: ', frag)
            print('url.startswith({}): {}'.format(self.url, url.startswith(self.url)))

            # if (url.startswith(self.rooturl) and url not in self.busy and url not in self.done and
            #         url not in self.todo and 'DependencyHandler' not in url and url[-4:] != '.png' and
            #         url[-4:] != '.svg'):
            if (url.startswith(self.url) and url not in self.busy and url not in self.done and
                    url not in self.todo):
                self.todo.add(url)
                self.retries[url] = 0
                await self.semaphore.acquire()
                task = asyncio.ensure_future(self.process(url))
                task.add_done_callback(lambda t: self.semaphore.release())
                task.add_done_callback(self.tasks.remove)
                self.tasks.add(task)

    async def process(self, url):
        self.todo.remove(url)
        self.busy.add(url)

        try:
            async with self.aiohttp.get(url, allow_redirects=True) as resp:
                self.done[url] = True

                if resp.status != 200 and resp.status in self.retry_codes:
                    print('resp.status:  == {} - url == {}'.format(resp.status, url))
                    if self.retry and self.retries[url] < self.retry_times:
                        print('resp.status:  == {} - retry: {} - url == {}'.format(resp.status, self.retry_times, url))
                        self.done[url] = False
                        self.retries[url] += 1

                if resp.status == 200 and ('text/html' in resp.headers.get('content-type')):
                    print('resp.status:  == {} - url == {}'.format(resp.status, url))
                    source = (await resp.read()).decode('utf-8', 'replace')
                    await self.parse(url, source)

                if resp.status != 200 and resp.status not in self.retry_codes:
                    print('resp.status:  == {} - url == {}'.format(resp.status, url))
                    self.error += 1

            resp.close()
            self.busy.remove(url)
        except Exception as exc:
            print('{}: {} - {}'.format(url, 'has error', repr(str(exc))))
            self.done[url] = False
            self.error += 1
            raise
        finally:
            print('Tasks: {} - completed: {} - pending: {} - todo: {} - error: {} - extracted: {} - megagroups:{}'
                  .format(self.url, len(self.done), len(self.tasks), len(self.todo), self.error,
                          len(self.extracted), self.megagroups))

    async def parse(self, url, source):
        urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', source)

        sem = utils.Sem()

        # unique (set) extracted urls = {urls}
        results = await utils.gather(*[sem.run(utils.aiocurl_eurl, turl) for turl in {urls}
                                       for pattern in self.patterns if pattern in turl])
        # unique (set) telegram extracted urls = {result[0] for result in results}
        extracted = await Url.aiochild_get(url)
        await utils.gather(*[Url.aiochild_update(url, extracted_url=telegram)
                             for telegram in {result[0] for result in results} if telegram not in extracted])

        self.extracted[url] = True
        self.megagroups = await Url.aiochild_count(url)

        if not self.times_max or self.times_real:
            if self.times_real:
                self.times_real = None
            await asyncio.create_task(self.addurls([(u, url) for u in urls]))

        # if self.first:
        #     # await asyncio.Task(self.addurls([(u, url) for u in urls]))
        #     await asyncio.create_task(self.addurls([(u, url) for u in urls]))
        #     if self.browser and self.first:
        #         self.first = False


async def crawl():
    l = log()

    l.s(msg='START: crawl(Url) == {}'.format(await Extracted.aiocount()))
    await utils.gather(*[Crawl(row).run() for row in await Url.aioall()])
    l.s(msg='END: crawl(Url) == {}'.format(await Extracted.aiocount()))

    l.s(msg='START: crawl(Megagroup) == {}'.format(await MegaGroup.aiocount()))
    megagroup = await MegaGroup.aioall()
    await utils.gather(*[MegaGroup.aioupdate(url=row.extracted_url) for row in await Extracted.aioall() if
                         row.extracted_url not in megagroup])
    l.s(msg='END: crawl(Megagroup) == {})'.format(await MegaGroup.aiocount()))

if __name__ == '__main__':
    asyncio.run(crawl())
