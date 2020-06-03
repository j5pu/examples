import random
from time import sleep
import asyncio
import time


def tic(start):
    return 'at %1.11f seconds' % (time.time() - start)


def task(pid, start):
    """Synchronous non-deterministic task."""
    print('task started work: {}'.format(tic(start)))
    sleep(random.randint(0, 2) * 0.001)
    print('Task %s done' % pid)
    print('task ended work: {}'.format(tic(start)))

async def task_coro(pid, start):
    """Coroutine non-deterministic task"""
    print('task_coro started work: {}'.format(tic(start)))
    await asyncio.sleep(random.randint(0, 2) * 0.001)
    print('Task %s done' % pid)
    print('task_coro ended work: {}'.format(tic(start)))


def synchronous(start):
    print('synchronous started work: {}'.format(tic(start)))
    for i in range(1, 10):
        task(i, start)
    print('synchronous ended work: {}'.format(tic(start)))


async def asynchronous(start):
    print('asynchronous started work: {}'.format(tic(start)))
    tasks = [task_coro(i, start) for i in range(1, 10)]
    await asyncio.gather(*tasks)
    print('asynchronous ended work: {}'.format(tic(start)))


print('Synchronous:')
synchronous(time.time())

print('Asynchronous:')
asyncio.run(asynchronous(time.time()))
import time
print(time.process_time_ns())