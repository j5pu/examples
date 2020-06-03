from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query'),
    Service('ipecho_redirect_json', 'http://ipinfo.io/json', 'ip'),
    Service('ipecho', 'http://ipecho.net/json', 'ip')

)


async def aiohttp_get_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_ip(service):
    start = time.time()
    print('Fetching IP from {}'.format(service.name))

    json_response = await aiohttp_get_json(service.url)
    ip = json_response[service.ip_attr]

    return '{} finished with result: {}, took: {:.2f} seconds'.format(
        service.name, ip, time.time() - start)


async def main():
    futures = [fetch_ip(service) for service in SERVICES]
    done, pendings = await asyncio.wait(
        futures, return_when=FIRST_COMPLETED)
    print('main: ',format(done.pop().result()))

    # NOTA: ESTA LINEA LA HE ÑADIDO YO EVITAR CERRAR BLUCLE Y QUE SALIA QUE ESTABAN ACTIVAS!!!!!. QUE ORGULLOSO
    for pending in pendings:
        await asyncio.shield(pending)

async def main1():
    futures = [fetch_ip(service) for service in SERVICES]
    done, pendings = await asyncio.wait(
        futures, return_when=FIRST_COMPLETED)

    print('main1: ',format(done.pop().result()))
    # NOTA: ESTA LINEA LA HE ÑADIDO YO EVITAR CERRAR BLUCLE Y QUE SALIA QUE ESTABAN ACTIVAS!!!!!. QUE ORGULLOSO
    for pending in pendings:
        pending.cancel()

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(main())
ioloop.stop()
#ioloop.close()

# NOTA: Como el otro loop cerrado entonces NEW porque si no dice que no esta wait el main.
loop = asyncio.new_event_loop()
loop.run_until_complete(main1())
loop.close()
import time
print(time.process_time_ns())
