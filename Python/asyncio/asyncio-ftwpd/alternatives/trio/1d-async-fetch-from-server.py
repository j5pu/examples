import time
import urllib.request
import trio
import asks
from tracer import Tracer

asks.init('trio')

URL = 'https://api.github.com/events'
MAX_CLIENTS = 3
results = {}

def fetch_sync(url):
    print('Fetch sync process {} started'.format(url))
    start = time.time()
    response = urllib.request.urlopen(url).read().decode()
    #datetime = response.getheader('Date')

    print('Process {}: {}, took: {:.2f} seconds'.format(
        url, response, time.time() - start))

    # NOTA LO METO YO TENER RESULTADOS
    results[url] = response


async def fetch_async(url):
    print('Fetch async process {} started'.format(url))
    start = time.time()
    response = (await asks.get(url)).content.decode()
    #datetime = response.headers.get('Date')

    print('Process {}: {}, took: {:.2f} seconds'.format(
        url, response, time.time() - start))

    # NOTA LO METO YO TENER RESULTADOS
    results[url] = response


def synchronous():
    start = time.time()
    urls = ['http://ipecho.net/plain', 'http://ipecho.net/plain', 'https://ipecho.net/plain']

    for url in urls:
        fetch_sync(url)
    print("Process took: {:.2f} seconds".format(time.time() - start))


async def asynchronous():
    start = time.time()
    urls = ['http://ipecho.net/plain', 'http://ipecho.net/plain', 'https://ipecho.net/plain']
    async with trio.open_nursery() as nursery:
        for url in urls:
            nursery.start_soon(fetch_async, url, name=url)
            print('Result from url={} - response={}'.format(url, results[url]))
    print("Process took: {:.2f} seconds".format(time.time() - start))


print('Synchronous:')
synchronous()

print('Asynchronous:')
trio.run(asynchronous)
import time
print(time.process_time_ns())