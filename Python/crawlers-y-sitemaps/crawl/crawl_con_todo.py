import asyncio
import re
import signal
import time
import urllib.parse

import aiohttp
import aiotask_context
import tables
import utils
from lxml import html
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException, WebDriverException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from tables import Extracted, MegaGroup, Url
from utils import log


class Browser:
    def __init__(self, row):
        self.url = row.url
        self.click = row.click
        self.times_max = row.times_max
        self.times_real = row.times_real

        self.error = False
        self.error_message = ''
        self.proxy = Proxy()
        self.proxy.proxy_type = ProxyType.MANUAL
        self.proxy.http_proxy = '127.0.0.1:9950'
        self.capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.proxy.add_to_capabilities(self.capabilities)
        self.firefox = webdriver.Firefox(desired_capabilities=self.capabilities)
        self.firefox.implicitly_wait(tables.config.browser_implicit_wait)
        self.browser_load_sleep = tables.config.browser_load_sleep

    def download(self):
        if self.open():
            if self.click() is False:
                self.quit()
                return False
        else:
            self.quit()
            return False
        return self.scroll()

    def get(self):
        l = log()

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

    def source(self):
        l = log()
        action = 'Scroll'
        if self.click:
            action = 'Click'

        for i in range(1, self.times_max):
            try:
                if self.click:
                    self.firefox.find_element_by_link_text(self.click).click()
                else:
                    self.firefox.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                message = '{}: {} out of {} times - url={}'.format(action, i, self.times_max - 1, self.url)
                l.info(message)
            except NoSuchElementException and NoSuchWindowException as exception:
                if i >= self.times_real:
                    return True
                self.error = True
                self.error_message = '{} error: {} out of {} times - url={} - Exception: {}'.\
                    format(action, i, self.times_max - 1, self.url, repr(exception))
                l.error(self.error_message)
                self.quit()
                return False
            except WebDriverException as exception:
                self.error = True
                self.error_message = '{} error: {} out of {} times - url={} - Exception: {}'.\
                    format(action, i, self.times_max - 1, self.url, repr(exception))
                l.error(self.error_message)
                self.quit()
                return False
            finally:
                time.sleep(self.browser_load_sleep)
        page_source = self.firefox.page_source
        self.quit()
        return page_source

    def scroll(self):
        l = log()

        if self.times_max != 0:
            for i in range(1, self.times_max):
                try:
                    self.firefox.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    message = 'Scroll: {} out of {} times - url={}'.format(i, self.times_max - 1, self.url)
                    l.info(message)
                except WebDriverException as exception:
                    self.error = True
                    self.error_message = 'Scrolling error time={} out of {} times with url={} - Exception: {}'.\
                        format(i, self.times_max - 1, self.url, repr(exception))
                    l.error(self.error_message)
                    self.quit()
                    return False
                finally:
                    time.sleep(self.browser_load_sleep)
        page_source = self.firefox.page_source
        self.quit()
        return page_source

    def click(self):
        l = log()
        if self.times_max != 0:
            for i in range(1, self.times_max):
                try:
                    self.firefox.find_element_by_link_text(self.click).click()
                    message = 'Click: {} out of {} times - url={}'.format(i, self.times_max - 1, self.url)
                    l.info(message)
                except NoSuchElementException and NoSuchWindowException as exception:
                    if i >= self.times_real:
                        return True
                    self.error = True
                    self.error_message = 'Click error: {} out of {} times - url={} - Exception: {}'.\
                        format(i, self.times_max - 1, self.url, repr(exception))
                    l.error(self.error_message)
                    self.quit()
                    return False
                except WebDriverException as exception:
                    self.error = True
                    self.error_message = 'Click error: {} out of {} times - url={} - Exception: {}'.\
                        format(i, self.times_max - 1, self.url, repr(exception))
                    l.error(self.error_message)
                    self.quit()
                    return False
                finally:
                    time.sleep(self.browser_load_sleep)
        return True

    def scroll(self):
        l = log()

        if self.times_max != 0:
            for i in range(1, self.times_max):
                try:
                    self.firefox.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    message = 'Scroll: {} out of {} times - url={}'.format(i, self.times_max - 1, self.url)
                    l.info(message)
                except WebDriverException as exception:
                    self.error = True
                    self.error_message = 'Scrolling error time={} out of {} times with url={} - Exception: {}'.\
                        format(i, self.times_max - 1, self.url, repr(exception))
                    l.error(self.error_message)
                    self.quit()
                    return False
                finally:
                    time.sleep(self.browser_load_sleep)
        page_source = self.firefox.page_source
        self.quit()
        return page_source

    def open(self):
        l = log()

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


class Crawler:
    def __init__(self, rooturl, loop, maxtasks=100):
        self.rooturl = rooturl
        self.loop = loop
        self.todo = set()
        self.busy = set()
        self.done = {}
        self.tasks = set()
        self.sem = asyncio.Semaphore(maxtasks, loop=loop)
        headers = {"Referer": "https://www.google.com/search?",
                   "Accept": "text/html,application/xhtml+xml, application/xml;q=0.9,*/*;q=0.8",
                   "Accept_Language": "en", "DNT": "0", "Content-Language": "en-US",
                   "Content-Type": "text/html; charset=utf-8",
                   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) "
                                 "AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10"}

        self.session = aiohttp.ClientSession(loop=loop, headers=headers, trust_env=True)

    async def run(self):
        t = asyncio.ensure_future(self.addurls([(self.rooturl, '')]), loop=self.loop)
        await asyncio.sleep(1, loop=self.loop)
        while self.busy:
            await asyncio.sleep(1, loop=self.loop)

        await t
        await self.session.close()
        self.loop.stop()

    async def addurls(self, urls):
        for url, parenturl in urls:
            url = urllib.parse.urljoin(parenturl, url)
            url, frag = urllib.parse.urldefrag(url)
            if (url.startswith(
                    self.rooturl) and url not in self.busy and url not in self.done and url not in self.todo):
                self.todo.add(url)
                await self.sem.acquire()
                task = asyncio.ensure_future(self.process(url), loop=self.loop)
                task.add_done_callback(lambda t: self.sem.release())
                task.add_done_callback(self.tasks.remove)
                self.tasks.add(task)

    async def process(self, url):
        print('processing:', url)

        self.todo.remove(url)
        self.busy.add(url)
        try:
            resp = await self.session.get(url)
            a = resp.url
        except Exception as exc:
            print('...', url, 'has error', repr(str(exc)))
            self.done[url] = False
        else:
            print(resp.status)

            if resp.status == 200 and 'text/html' in resp.headers.get('content-type'):
                data = (await resp.read()).decode('utf-8', 'replace')
                urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', data)
                print(data)
                await asyncio.Task(self.addurls([(u, url) for u in urls]))

            resp.close()
            self.done[url] = True

        self.busy.remove(url)
        print(len(self.done), 'completed tasks,', len(self.tasks), 'still pending, todo', len(self.todo))


def main():
    loop = asyncio.get_event_loop()

    c = Crawler('https://www.icohotlist.com/', loop)
    asyncio.ensure_future(c.run(), loop=loop)

    try:
        loop.add_signal_handler(signal.SIGINT, loop.stop)
    except RuntimeError:
        pass
    loop.run_forever()
    print('todo:', len(c.todo))
    print('busy:', len(c.busy))
    print('done:', len(c.done), '; ok:', sum(c.done.values()))
    print('tasks:', len(c.tasks))


def main2():
    loop = asyncio.get_event_loop()

    c = Crawler('http://ipecho.net/plain', loop)
    asyncio.ensure_future(c.run(), loop=loop)

    try:
        loop.add_signal_handler(signal.SIGINT, loop.stop)
    except RuntimeError:
        pass
    loop.run_forever()
    print('todo:', len(c.todo))
    print('busy:', len(c.busy))
    print('done:', len(c.done), '; ok:', sum(c.done.values()))
    print('tasks:', len(c.tasks))


def browser():
    l = log()

    crawl_url = "https://tgram.io/topic/29/it/cryptocurrency"
    page = Browser(url=crawl_url, scroll_times=12)
    page_source = page.download()
    if page_source is False:
        l.e(msg='Error downloading page source for url: {}'.format(crawl_url))
    else:
        l.i(msg='Success: source code for url: {}'.format(crawl_url))
        file = 'cryptocurrency.html'
        try:
            with open(file, 'w') as f:
                f.write(format(page_source))
            l.i(msg='Success: source code for url: {} - saved to {}'.format(crawl_url, file))
        except:
            l.i(msg='Error: source code for url: {} - not saved to {}'.format(crawl_url, file))

    crawl_url = "https://tgram.io/topic/51/it/crypto-mining"
    page = Browser(url=crawl_url, scroll_times=2)
    page_source = page.download()
    if page_source is False:
        l.e(msg='Error downloading page source for url: {}'.format(crawl_url))
    else:
        l.i(msg='Success: source code for url: {}'.format(crawl_url))
        file = 'crypto-mining.html'
        try:
            with open(file, 'w') as f:
                f.write(format(page_source))
            l.i(msg='Success: source code for url: {} - saved to {}'.format(crawl_url, file))
        except:
            l.i(msg='Error: source code for url: {} - not saved to {}'.format(crawl_url, file))

    crawl_url = "https://icorating.com/ico/all/"
    page = Browser(url=crawl_url, click='Show more', click_times=180)
    page_source = page.download()
    if page_source is False:
        l.e(msg='Error downloading page source for url: {}'.format(crawl_url))
    else:
        l.i(msg='Success: source code for url: {}'.format(crawl_url))
        file = 'corating.html'
        try:
            with open(file, 'w') as f:
                f.write(format(page_source))
            l.i(msg='Success: source code for url: {} - saved to {}'.format(crawl_url, file))
        except:
            l.i(msg='Error: source code for url: {} - not saved to {}'.format(crawl_url, file))


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

    async def add(self, urls):
        for url, parenturl in urls:
            url = urllib.parse.urljoin(parenturl, url)
            url, frag = urllib.parse.urldefrag(url)
            if url.startswith(self.url) and url not in self.busy and url not in self.done and url not in self.todo:
                self.todo.add(url)
                await self.run(self.process, url)

    async def process(self, url):
        l = log()
        self.todo.remove(url)
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
            print(
                'Tasks: {} - completed: {} - pending: {} - todo: {} - error: {} - extracted: {} - megagroups:{}'.format(
                    self.url, len(self.done), len(self.tasks), len(self.todo), self.error, len(self.extracted),
                    self.megagroups))

    async def parse(self, url, source):
        if source:
            urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', source)

            sem = utils.Sem(utils.Sem.names[3])
            results = await utils.gather(
                *[sem.run(utils.Curl.url, turl) for turl in {*urls} for pattern in self.patterns if pattern in turl])
            extracted = await Url.aiochild_get(url)
            await utils.gather(*[Url.aiochild_update(url, extracted_url=telegram) for telegram in {*results} if
                                 telegram not in extracted])

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
    browser()
    main()
    main2()
    utils.start(crawl)
