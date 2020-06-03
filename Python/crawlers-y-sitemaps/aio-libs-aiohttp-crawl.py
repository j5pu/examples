#!/usr/bin/env python3
    # https://github.com/aio-libs/aiohttp/blob/master/examples/legacy/crawl.py
import urllib.parse
import asyncio
import sys
import logging
import aiohttp
import re
import signal
import curl

class Crawler:

    def __init__(self, rooturl, loop, maxtasks=100):
        self.rooturl = rooturl
        self.loop = loop
        self.todo = set()
        self.busy = set()
        self.done = {}
        self.tasks = set()
        self.sem = asyncio.Semaphore(maxtasks, loop=loop)
        # headers = {
        #     'Referer': 'https://www.google.com/search',
        #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'
        #
        # }
        headers = {'Referer': 'https://www.google.com/search?', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept_Language': 'en', 'DNT': '0', 'Content-Language': 'en-US', 'Content-Type': 'text/html; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'}

        # connector stores cookies between requests and uses connection pool
        self.session = aiohttp.ClientSession(loop=loop, headers=headers, trust_env=True)


    async def run(self):
        t = asyncio.ensure_future(self.addurls([(self.rooturl, '')]),
                                  loop=self.loop)
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
            if (url.startswith(self.rooturl) and
                    url not in self.busy and
                    url not in self.done and
                    url not in self.todo):
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
            import os
            http_proxy = os.getenv('http_proxy', 'NULL')

            resp = await self.session.get(url)
        except Exception as exc:
            print('...', url, 'has error', repr(str(exc)))
            self.done[url] = False
        else:
            print(resp.status)

            if (resp.status == 200 and
                    ('text/html' in resp.headers.get('content-type'))):
                data = (await resp.read()).decode('utf-8', 'replace')
                urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', data)
                print(data)
                await asyncio.Task(self.addurls([(u, url) for u in urls]))

            resp.close()
            self.done[url] = True

        self.busy.remove(url)
        print(len(self.done), 'completed tasks,', len(self.tasks),
              'still pending, todo', len(self.todo))


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


if __name__ == '__main__':
    if '--iocp' in sys.argv:
        from asyncio import events, windows_events
        sys.argv.remove('--iocp')
        logging.info('using iocp')
        el = windows_events.ProactorEventLoop()
        events.set_event_loop(el)

    main()
    main2()
