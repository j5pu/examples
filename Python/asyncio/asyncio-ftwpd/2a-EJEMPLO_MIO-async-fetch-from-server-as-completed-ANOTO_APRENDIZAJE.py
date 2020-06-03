import time
import random
import asyncio
import aiohttp

URL = 'https://api.github.com/events'
MAX_CLIENTS = 3


async def aiohttp_get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response


async def fetch_async(pid):
    start = time.time()
    sleepy_time = random.randint(2, 5)
    print('Fetch async process {} started, sleeping for {} seconds'.format(
        pid, sleepy_time))

    await asyncio.sleep(sleepy_time)

    response = await aiohttp_get(URL)
    datetime = response.headers.get('Date')

    response.close()
    return 'Process {}: {}, took: {:.2f} seconds'.format(
        pid, datetime, time.time() - start)

async def main():
    start = time.time()
    futures = [fetch_async(i) for i in range(1, MAX_CLIENTS + 1)]
    for i, future in enumerate(asyncio.as_completed(futures)):
        result = await future
        """
        OJO: as completed es un iterador que devuelve corrutinas no las lanza entonces.!!!
             Future es la funcion que se ejecutara, pero no se ejecuta hasta que: await future
        Aqui a medida que acaban va haciendo la siguiente linea

        """
        print('{} {}'.format(">>" * (i + 1), result))

    print("Process took: {:.2f} seconds".format(time.time() - start))

async def impri(v):
    print(time.time())
    print('Imprimire en: {}', v)
    await asyncio.sleep(v)
    print(time.time())
    print('Imprimido en: {}', v)

async def main1():
    futures = [impri(1), impri(2)]
    future = asyncio.create_task(futures)
    print('No espero')
    result = await future


async def main2():
    print(time.time())
    print('Comienzo')

    # Nota: create_task empieza en el momento
    future = asyncio.create_task(impri(0))

    print('Trabajo: No espero')

    # Nota: y aqui la espero
    await future
    # NOTA: CONCLUSION:
    # NOTA: 1.- Si async def() todo y siempre que llamo espero entonces es como llamar normal. TONTERIA!!!!
    # NOTA                                        async def tonto(): return 1
    # NOTA                                        valor = await tonto()
    # NOTA                                            ¡ ES UNA TONTERIA ! No hago nada mientras y no bloquea.
    # NOTA: 2.- resultado = asyncio.create_task - async def() INMEDIATO y devuelve futuro donde AWAIT resultado.
    # NOTA                                        O SEA, ¡SI SENTIDO HACIENDO COSAS EN MEDIO!
    # NOTA: 3.- asyncio.gather - para cada coro o fut lanza y agrupa en un GRAN FUT.
    # NOTA:                                       ¡SI SENTIDO PORQUE LAS LANZA EN PARALELO!
    # NOTA:                                           - PARA ADELANTAR mejor AS_COMPLETED si hacer cosas justo despues
    # NOTA:                                             del gather para ir adelantando antes de acabar funcion.
    # NOTA:                                           - si no al final el gather es el que bloquea. GATHER mejor cuando acaba funcion
    # NOTA:                                             O si dependo de todos para hacer algo
    # NOTA: mi utils.gather es como asyncio.wait(ALL_COMPLETED, en esta crea el futuro!) Su entrada esta mejor con (fs, *, ) y set que llama a _wait
    # NOTA:                    es como si yo en el helper que tiene _wait lo hubiera llamado SEM y cuando crea en:
    # NOTA                            asyncio._wait(): waiter = loop.create_future() = utils.Sem.run(): task = asyncio.create_task(coro)
    # NOTA                            asyncio._wait(): await waiter = utils.Sem.run(): await task
    # NOTA                                      lo unnico que el tiene el _wait para poner el resultado de las otras 2 que no son ALL_COMPLLETED
    # NOTA                                      SERIA LO MISMO SI antes sem.acquire() -> await waiter -> sem.release() despues.
    # NOTA                      El gather = wait(ALL_COMPLETED) pero el gather agrupa los resultados y el ALL_COMPLETED, NO.
    # NOTA                           A.- para que fueran iguales, de hecho devuelve: done, pending = wait, done es set que tendra resultado de cada una me imagino done[0].result()
    # NOTA                               done, pending = asyncio.wait(coros):
    # NOTA                               for resultado in done
    # NOTA                                   print(resultado.result())
    # NOTA                           B.- es lo mismo creo que:
    # NOTA                               resultados = utils.gather(coros)
    # NOTA                               for resultado in resultados:
    # NOTA                                   print(resultado) - LA DIFERENCIA ES QUE YO HE METIDO EL SEMAFORO
    # NOTA                           C.- resultados = asyncio.gather()
    # NOTA                               LA DIFERENCIA QUE resultados.result() da todos los resultados. O SEA BUENO PARA LO DE eurl() como yo...


    """
    """
asyncio.run(main())
asyncio.run(main2())

import time
print(time.process_time_ns())