# from logger import logger
# from funcs import aiocurl
# from ip import rotate
from __init__ import Url, session
import urllib.parse
import asyncio
import aiohttp
import re
import random
import threading

# log = logger()


# class Crawl:
#     def __init__(self, rooturl):
#         self.rooturl = rooturl
#         # self.loop = loop
#         self.todo = set()
#         self.busy = set()
#         self.done = {}
#         self.extracted = {}
#         self.tasks = set()
#         self.telegram = set()
#         self.headers = crawl_headers
#         self.timeout = aiohttp.ClientTimeout(total=(int(crawl_defaults['aiohttp_timeout'])))
#         self.trust_env = bool(crawl_defaults['aiohttp_trust_env'])
#         self.allow_redirects = bool(crawl_defaults['aiohttp_allow_redirects'])
#         self.max_redirects = int(crawl_defaults['aiohttp_max_redirects'])
#         self.aiohttp_semaphore = asyncio.Semaphore(int(crawl_defaults['aiohttp_semaphore']))
#         self.aiocurl_semaphore = int(crawl_defaults['aiocurl_semaphore'])
#         self.min_delay = int(crawl_defaults['min_delay'])
#         self.max_delay = int(crawl_defaults['max_delay'])
#         self.busy_delay = int(crawl_defaults['busy_delay'])
#         self.retry_enabled = bool(crawl_defaults['retry_enabled'])
#         self.retry_times = int(crawl_defaults['retry_times'])
#         self.crawl_retry_codes = crawl_retry_codes
#         self.error = 0
#
#         # connector stores cookies between requests and uses connection pool
#         self.client = aiohttp.ClientSession(headers=self.headers, timeout=self.timeout, trust_env=self.trust_env)
#
#
#     async def run(self):
#         log.child()
#
#         t = asyncio.create_task(self.addurls([(self.rooturl.url, '')]))
#
#         await asyncio.sleep(random.randint(self.min_delay, self.max_delay))
#         while self.busy:
#             await asyncio.sleep(self.busy_delay)
#
#         await t
#         await self.client.close()
#
#     async def addurls(self, urls):
#         log.child()
#
#         for url, parenturl in urls:
#             url = urllib.parse.urljoin(parenturl, url)
#             url, frag = urllib.parse.urldefrag(url)
#             if (url.startswith(self.rooturl.url) and
#                     url not in self.busy and
#                     url not in self.done and
#                     url not in self.todo):
#                 self.todo.add(url)
#                 await self.aiohttp_semaphore.acquire()
#                 task = asyncio.ensure_future(self.process(url))
#                 task.add_done_callback(lambda t: self.aiohttp_semaphore.release())
#                 task.add_done_callback(self.tasks.remove)
#                 self.tasks.add(task)
#
#     async def process(self, url):
#         l = log.child()
#
#         self.todo.remove(url)
#         self.busy.add(url)
#
#         try:
#             async with self.client.get(url, allow_redirects=self.allow_redirects, max_redirects=self.max_redirects) as resp:
#                 if resp.status != 200 and resp.status in self.crawl_retry_codes:
#                     l.w('resp.status:  == {} - url == {}'.format(resp.status, url))
#                     if self.retry_enabled and self.retry_times >= 0:
#                         l.w('resp.status:  == {} - retry: {} - url == {}'.format(resp.status, self.retry_times, url))
#                         self.done[url] = False
#                         self.retry_times -= 1
#                     else:
#                         l.e('resp.status:  == {} - url == {}'.format(resp.status, url))
#                         self.done[url] = True
#                         self.error += 1
#
#                 if resp.status == 200 and ('text/html' in resp.headers.get('content-type')):
#                     l.i('resp.status:  == {} - url == {}'.format(resp.status, url))
#                     data = (await resp.read()).decode('utf-8', 'replace')
#                     urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', data)
#
#
#                     tasks = [asyncio.create_task(aiocurl(turl, log=l)) for turl in urls for pattern in
#                                 crawl_telegram.values() if pattern in turl]
#                     # tasks_direct = [direct(crawl) for crawl in session.query(Crawl) if crawl.direct == True]
#                     # tasks_page = [executor(functools.partial(scrapy, crawl), None, log) for crawl in session.query(Crawl) if
#                     #               crawl.direct == False]
#                     # tasks_multi = [executor(functools.partial(browser, crawl), None, log) for crawl in session.query(Crawl) if
#                     #                crawl.direct == None]
#
#                     self.telegram = set(await asyncio.gather(*tasks, return_exceptions=True))
#                     print(self.telegram)
#                     # self.telegram = set(await aiocurl(turl, log=l) for turl in urls for pattern in
#                     #                     crawl_telegram.values()
#                     #                     if pattern in turl)
#                     self.extracted[url] = True
#
#                     if self.rooturl.direct is not True:
#                         await asyncio.Task(self.addurls([(u, url) for u in urls]))
#                     self.done[url] = True
#                 else:
#                     l.e('resp.status:  == {} - text/html != {} - url == {}'.format(resp.status,
#                                                                                    resp.headers.get('content-type'),
#                                                                                    url))
#                     self.done[url] = True
#                     self.error += 1
#
#                 if resp.status != 200 and resp.status not in self.crawl_retry_codes:
#                     l.e('resp.status:  == {} - url == {}'.format(resp.status, url))
#                     self.done[url] = True
#                     self.error += 1
#
#             resp.close()
#             self.busy.remove(url)
#         except Exception as exc:
#             l.e('{}: {} - {}'.format(url, 'has error', repr(str(exc))))
#             self.done[url] = False
#
#             raise
#         finally:
#             l.i('Tasks: {} - completed: {} - pending: {} - todo: {} - error: {} - extracted: {} - telegram:{}'
#                 .format(self.rooturl.url, len(self.done), len(self.tasks), len(self.todo), self.error,
#                         len(self.extracted), len(self.telegram)))
#
#
# async def direct(queue):
#     l = log.child()
#     while True:
#         url = await queue.get()
#
#         l.i(url.url)
#         #loop = asyncio.get_event_loop()
#         c = Crawl(url)
#         await asyncio.Task(c.run())
#         # asyncio.ensure_future(c.run(), loop=loop)
#         #
#         # try:
#         #     loop.add_signal_handler(signal.SIGINT, loop.stop)
#         # except RuntimeError:
#         #     pass
#         # loop.run_forever()
#
#         print('todo:', len(c.todo))
#         print('busy:', len(c.busy))
#         print('done:', len(c.done), '; ok:', sum(c.done.values()))
#         print('tasks:', len(c.tasks))
#         print('error:', c.error)
#         print('extracted:', len(c.extracted))
#         print('telegram:', len(c.telegram))
#
#         queue.task_done()
#
#
# async def page(queue):
#     l = log.child()
#     while True:
#         url = await queue.get()
#         l.i(url.url)
#         # c = Crawl(url)
#         # task = asyncio.create_task(c.run())
#         #
#         # await task
#         #
#         # print('todo:', len(c.todo))
#         # print('busy:', len(c.busy))
#         # print('done:', len(c.done), '; ok:', sum(c.done.values()))
#         # print('tasks:', len(c.tasks))
#
#         queue.task_done()
#
#
# async def multi(queue):
#     l = log.child()
#     while True:
#         url = await queue.get()
#         l.i(url.url)
#
#         queue.task_done()


async def crawl():
    # log.child()
    #
    # # base = await executor(functools.partial(automap_base), 'thread')
    # # l.d('Executor thread:  automap_base == {} - Base  == {}'.format(automap_base, base))
    # #
    # # await executor(functools.partial(base.prepare, engine, reflect=True), 'thread')
    # # l.d('Executor thread:  base.prepare == {} - engine  == {}'.format(base.prepare, engine))
    # #
    # # crawl_urls = await executor(functools.partial(base.classes.crawl_urls), 'thread')
    # # l.d('Executor thread:  base.classes.crawl_urls == {} - crawl_urls  == {}'
    # #     .format(base.classes.crawl_urls, crawl_urls))
    # direct_queue = asyncio.Queue()
    # page_queue = asyncio.Queue()
    # multi_queue = asyncio.Queue()

    print(session.query(Url))

    # for url in session.query(Url):
    #     if url.direct:
    #         direct_queue.put_nowait(url)
    #     elif url.direct is False:
    #         page_queue.put_nowait(url)
    #     elif url.direct is None:
    #         multi_queue.put_nowait(url)
    #     else:
    #         raise ValueError

    # direct_tasks = []
    # for i in range(int(crawl_defaults['direct_workers'])):
    #     task = asyncio.create_task(direct(direct_queue))
    #     direct_tasks.append(task)
    #
    # page_tasks = []
    # for i in range(int(crawl_defaults['page_workers'])):
    #     task = asyncio.create_task(page(page_queue))
    #     page_tasks.append(task)
    #
    # multi_tasks = []
    # for i in range(int(crawl_defaults['multi_workers'])):
    #     task = asyncio.create_task(multi(multi_queue))
    #     multi_tasks.append(task)
    #
    # # tasks_direct = [direct(crawl) for crawl in session.query(Crawl) if crawl.direct == True]
    # # tasks_page = [executor(functools.partial(scrapy, crawl), None, log) for crawl in session.query(Crawl) if
    # #               crawl.direct == False]
    # # tasks_multi = [executor(functools.partial(browser, crawl), None, log) for crawl in session.query(Crawl) if
    # #                crawl.direct == None]
    # await direct_queue.join()
    # await page_queue.join()
    # await multi_queue.join()
    # for task in direct_tasks:
    #     task.cancel()
    # for task in page_tasks:
    #     task.cancel()
    # for task in multi_tasks:
    #     task.cancel()
    # await asyncio.gather(*direct_tasks, *page_tasks, *multi_tasks, return_exceptions=True)

    # for row in engine.connect().execute(crawl_urls.__table__.select()):
    #     if row['steps'] == 'multi':
    #         l.d("Processing:  row['url'] == {} - row['steps']  == {}".format(row['url'], row['steps']))
    #         tasks_multi.append(executor(functools.partial(scrapy, row), 'thread'))
    #         # task = asyncio.create_task(executor(functools.partial(scrapy, row), 'thread'))
    #         # await executor(functools.partial(scrapy, row), 'thread')
    #
    #     elif row['steps'] == 'page':
    #         l.d("Processing:  row['url'] == {} - row['steps']  == {}".format(row['url'], row['steps']))
    #         tasks_page.append(executor(functools.partial(scrapy, row), 'thread'))
    #
    #         # task = asyncio.create_task(executor(functools.partial(browser, row), 'thread'))
    #         # await executor(functools.partial(browser, row), 'thread')
    #     elif row['steps'] == 'direct':
    #         l.d("Processing:  row['url'] == {} - direct  == {}".format(row['url'], row['steps']))
    #         tasks_direct.append(executor(functools.partial(scrapy, row), 'thread'))
    #
    #         # task = asyncio.create_task( extract(row))
    #         #await extract(row)
    #     else:
    #         raise ValueError
    #
    # await asyncio.gather(*tasks_multi)
    # await asyncio.gather(*tasks_page)
    # await asyncio.gather(*tasks_direct)
    #
    #

if __name__ == '__main__':
    asyncio.run(crawl())

    # stop_event = threading.Event()
    # p = threading.Thread(target=rotate, args=(stop_event, log))
    # p.start()
    # try:
    #     asyncio.run(crawl())
    # except:
    #     stop_event.set()
    #     raise
    # finally:
    #     stop_event.set()

