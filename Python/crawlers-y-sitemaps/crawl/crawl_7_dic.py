#!/usr/py/bin/python3.7
from utils import *

megagroup_start = ini['default']['megagroup_start']
"""
Lanzar en tods las combinaciones con firefox etc y con los 3 parsers y con wget a tomar por culo.
y quitar todas las excepcionees. y lanzar con incrementando tiempos de retardo.!

y las efectivas tambien con curl 

y meter el de unix tambien de regex y que meta fichero con lo que extrae tambien ala y ya esta.
y cron

"""

class CrawlMegaGroup(Sem):
    def __init__(self, row: Crawl):
        super().__init__(sem=Sem.Name.CRAWL)
        self.root_url = row.url
        self.site = row.site
        self.firefox = row.firefox
        self.firefox_arg = row.firefox_arg
        self.firefox_times = row.firefox_times
        self.firefox_real = row.firefox_real
        self.done = {}
        self.todo = set()
        self.extracted = Crawl.child_count(self.root_url)
        self.megagroup = MegaGroup.count(self.root_url)
        self.error = 0

        self.todo.add(self.root_url)

    async def is_todo(self, link, url):
        link = urllib.parse.urljoin(link, url)
        link, frag = urllib.parse.urldefrag(link)
        if link.startswith(self.root_url) and link not in self.done and link not in self.todo:
            if '#' in link:
                link = link[:link.find('#')]
            return link

    async def do(self, url=None):
        if self.firefox is not Firefox.NONE:
            links = await Net(url, client=Net.Client.FIREFOX, firefox=self.firefox, firefox_arg=self.firefox_arg,
                              firefox_times=self.firefox_times, firefox_real=self.firefox_real,
                              root_url=self.root_url).get
        else:
            links = await Net(url, root_url=self.root_url).get

        if links:
            if self.site or (self.firefox and self.site):
                do_tasks = []
                for link in links:
                    todo_url = await self.is_todo(link, url)
                    if todo_url:
                        self.todo.add(todo_url)
                        do_tasks.append(self.do(todo_url))
                        if self.firefox:
                            do_tasks.append(Net(todo_url, client=Net.Client.WGET, site=False,
                                                root_url=self.root_url).get)
                            self.site = False
                            self.firefox = Firefox.NONE
                if do_tasks:
                    await self.gather(*do_tasks)
        else:
            self.error += 1

        self.todo.remove(url)
        self.done[url] = True
        extracted = await Crawl.aiochild_count(self.root_url)
        megagroup = MegaGroup.count(self.root_url)
        msg = '{}: tasks == {}, done == {}, error == {}, todo == {} - MySQL added({}): extracted: {}, MEGAGROUP:{}'.\
            format(self.root_url, len(self.tasks), len(self.done), self.error, len(self.todo), url,
                   extracted - self.extracted, megagroup - self.megagroup)
        log().i(msg) if links else log().e(msg)


async def crawl():
    l = log()

    # tasks = [CrawlMegaGroup(row).do(row.url) for row in crawl_rows] + \
    #         [Net(row.url, client=Net.Client.WGET, firefox=row.firefox, firefox_arg=row.firefox_arg,
    #              firefox_times=row.firefox_times, firefox_real=row.firefox_real, site=False, root_url=row.url).get
    #          for row in crawl_rows if row.firefox] + \
    #         [Net(row.url, client=Net.Client.WGET).get for row in crawl_rows if not row.firefox]
    try:
        l.i('CrawlMegaGroup: (-Start-) - megagroups: {})'.format(await MegaGroup.aiocount()))
        await Sem().gather(*[CrawlMegaGroup(row).do(row.url) for row in crawl_rows] +
                            [Net(row.url, client=Net.Client.WGET, firefox=row.firefox, firefox_arg=row.firefox_arg,
                                 firefox_times=row.firefox_times, firefox_real=row.firefox_real, site=False,
                                 root_url=row.url).get for row in crawl_rows if row.firefox is not Firefox.NONE] +
                            [Net(row.url, client=Net.Client.WGET).get for row in crawl_rows
                             if row.firefox is Firefox.NONE])
        l.s('CrawlMegaGroup: (-End-) - megagroups: {})'.format(await MegaGroup.aiocount()))

        l.i('Dir WGET: {}(-Start-) - megagroups: {})'.format(wget_dir, await MegaGroup.aiocount()))
        await Net(wget_dir).get
        l.s('Dir WGET: {}(-End-) - megagroups: {})'.format(wget_dir, await MegaGroup.aiocount()))

        l.i('File Megagroup: {}(-Start-) - megagroups: {})'.format(megagroup_start, await MegaGroup.aiocount()))
        await Net(megagroup_start).get
        l.s('File Megagroup: {}(-End-) - megagroups: {})'.format(megagroup_start, await MegaGroup.aiocount()))
    except KeyError as exc:
        l.x(repr(exc))
    # print('---------------------------------------------------------------------------------------------------------')
    # await Net('https://iconow.net', client=Net.Client.WGET, site=True).get
    # n = Net(client=Net.Client.AIOHTTP)
    # await n.get
    # print('AIOHTTP - ip: ', n.ip)
    # print('AIOHTTP - eurl_direct: ', n.eurl_direct)
    # print('AIOHTTP - links: ', n.links)
    # print('-------------------------------------------------------------------------------------------------------')
    # n = Net()
    # await n.get
    # print('REQUESTS - ip: ', n.ip)
    # print('REQUESTS - eurl_direct: ', n.eurl_direct)
    # print('REQUESTS - links: ', n.links)
    # print('REQUESTS - ip: ', await Net().get)
    # print('REQUESTS - eurl_direct: ', await Net('http://ipecho.net', links=None).get)
    # print('REQUESTS - links: ', await Net('http://ipecho.net').get)
    # print('link-------------------------------------------------------------------------------------------------------')
    # n = Net(client=Net.Client.CURL)
    # await n.get
    # print('CURL - ip: ', n.ip)
    # print('CURL - eurl_direct: ', n.eurl_direct)
    # print('CURL - links: ', n.links)
    # print('CURL - ip: ', await Net('https://ipecho.net', client=Net.Client.CURL).get)
    # print('CURL - eurl_direct: ', await Net('https://ipecho.net', client=Net.Client.CURL, links=None).get)
    # print('CURL - links: ', await Net('https://ipecho.net', client=Net.Client.CURL).get)
    #
    # print('--------------------------------------------------------------------------------------------------------')
    # n = Net(client=Net.Client.FIREFOX)
    # await n.get
    # print('FIREFOX - ip: ', n.ip)
    # print('FIREFOX - eurl_direct: ', n.eurl_direct)
    # print('FIREFOX - links: ', n.links)
    # print('FIREFOX - ip: ', await Net(client=Net.Client.FIREFOX).get)
    # print('FIREFOX - eurl_direct: ', await Net('http://ipecho.net', Net.Client.FIREFOX, None).get)
    # print('FIREFOX - links: ', await Net('http://ipecho.net', client=Net.Client.FIREFOX).get)
    #
    #
    # for row in crawl_rows:
    #     # Para links y t_eurls (self.t_eurls los mete en sql) devuelve links
    #     if row.url == 'https://tgram.io/topic/51/it/crypto-mining':
    #         links = await Net(row.url, Net.Client.FIREFOX, True, row.firefox, row.firefox_arg, row.firefox_times,
    #                   row.firefox_real).get

if __name__ == '__main__':
    run(crawl)
