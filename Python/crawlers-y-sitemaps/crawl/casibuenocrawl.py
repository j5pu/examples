import asyncio
import inspect
import io
import os
import pycurl
import socket
import time
from utils import log
from tables import config, Url, Extracted, MegaGroup
import aiohttp
from aioify import aioify
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import utils
import re
import urllib.parse
from selenium.common.exceptions import WebDriverException
import funcs
import aiotask_context

class Crawl(utils.Sem):
    def __init__(self, row):
        super().__init__(name=utils.Sem.names[3])
        self.url = row.url
        self.site = row.site
        self.browser = row.browser
        self.click = row.click
        self.times_max = row.times_max
        self.times_real = row.times_real
        self.loop = aiotask_context.get('loop_{}'.format(utils.Sem.names[3]))
        asyncio.set_event_loop(self.loop)
        super().__init__(name=utils.Sem.names[3])

        self.sem = asyncio.Semaphore(self.max, loop=self.loop)
        self.todo = set()
        self.busy = set()
        self.done = {}
        self.extracted = {}
        self.tasks = set()
        self.megagroups = None
        self.error = 0

        self.patterns = ['http://t.me/', 'https://t.me/', 'http://www.t.me/', 'https://www.t.me/',
                         'http://telegram.me/', 'https://telegram.me/', 'http://www.telegram.me/',
                         'https://www.telegram.me/']

    # async def start(self):
    #     # t = asyncio.create_task(self.addurls([(self.url, '')]))
    #
    #     async with utils.Aiohttp() as self.client:
    #         t = asyncio.create_task(self.addurls([(self.url, '')]))
    #
    #         await asyncio.sleep(1)
    #         while self.busy:
    #             await asyncio.sleep(1)
    #
    #         await t
    #     # await self.aiohttp.close()
    async def add(self, urls):
        # print('urls: ', urls)
        for url, parenturl in urls:
            # print('url: ', url)
            # print('parenturl: ', parenturl)
            url = urllib.parse.urljoin(parenturl, url)
            # print('url: ', url)
            url, frag = urllib.parse.urldefrag(url)
            # print('url: ', url)
            #
            # print('frag: ', frag)
            # print('url.startswith({}): {}'.format(self.url, url.startswith(self.url)))
            # if (url.startswith(self.rooturl) and url not in self.busy and url not in self.done and
            #         url not in self.todo and 'DependencyHandler' not in url and url[-4:] != '.png' and
            #         url[-4:] != '.svg'):
            if (url.startswith(self.url) and url not in self.busy and url not in self.done and
                    url not in self.todo):
                self.todo.add(url)
                await self.run(self.process, url)

    async def process(self, url):
        l = log()
        self.todo.remove(url)
        # self.busy.add(url)
        try:
            if self.browser:
                async with utils.Browser.get(url, self.click, self.times_max, self.times_real) as source:
                    await self.parse(url, source)
            else:
                async with utils.Url.get(url) as source:
                    await self.parse(url, source)
            self.done[url] = True
        except WebDriverException as exception:
            l.e(msg='Error opening url={} - Exception: {}'.format(url, repr(exception)))
            self.error += 1
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
        if source:
            urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', source)

            sem = utils.Sem(utils.Sem.names[3])
            results = await utils.gather(*[sem.run(utils.Curl.url, turl) for turl in {*urls}
                                           for pattern in self.patterns if pattern in turl])
            extracted = await Url.aiochild_get(url)
            await utils.gather(*[Url.aiochild_update(url, extracted_url=telegram)
                                 for telegram in {*results} if telegram not in extracted])

            self.extracted[url] = True
            self.megagroups = await Url.aiochild_count(url)

            if self.site or self.browser:
                if self.browser:
                    self.browser = False
                await asyncio.create_task(self.add([(u, url) for u in urls]))
        else:
            self.error += 1


async def crawl():
    l = log()

    l.s(msg='START: crawl(Url) == {}'.format(await Extracted.aiocount()))
    await utils.gather(*[Crawl(row).add([(row.url, '')]) for row in await Url.aioall()])
    l.s(msg='END: crawl(Url) == {}'.format(await Extracted.aiocount()))

    l.s(msg='START: crawl(Megagroup) == {}'.format(await MegaGroup.aiocount()))
    megagroup = await MegaGroup.aioall()
    await utils.gather(*[MegaGroup.aioupdate(url=row.extracted_url) for row in await Extracted.aioall() if
                         row.extracted_url not in megagroup])
    l.s(msg='END: crawl(Megagroup) == {})'.format(await MegaGroup.aiocount()))

if __name__ == '__main__':
    utils.start(crawl)
