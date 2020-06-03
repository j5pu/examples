#!/usr/bin/env python3.7
"""
https://www.roguelynn.com/words/asyncio-we-did-it-wrong-pt-4/

Notice! This requires:
 - attrs==18.1.0
"""

import asyncio
import functools
import logging
import random
import signal
import string
import uuid

import attr


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s,%(msecs)d %(levelname)s: %(message)s',
    datefmt='%H:%M:%S',
)


@attr.s
class PubSubMessage:
    instance_name = attr.ib()
    message_id    = attr.ib(repr=False)
    hostname = attr.ib(repr=False, init=False)

    def __attrs_post_init__(self):
        self.hostname = f'{self.instance_name}.example.net'


async def publish(queue):
    choices = string.ascii_lowercase + string.digits
    while True:
        msg_id = str(uuid.uuid4())
        host_id = ''.join(random.choices(choices, k=4))
        instance_name = f'cattle-{host_id}'
        msg = PubSubMessage(message_id=msg_id, instance_name=instance_name)
        # put the item in the queue
        await queue.put(msg)
        logging.debug(f'Published message {msg}')

        # simulate randomness of publishing messages
        await asyncio.sleep(random.random())


async def restart_host(msg):
    # unhelpful simulation of i/o work
    await asyncio.sleep(random.randrange(1,3))
    logging.info(f'Restarted {msg.hostname}')


async def save(msg):
    # unhelpful simulation of i/o work
    await asyncio.sleep(random.random())
    logging.info(f'Saved {msg} into database')


async def cleanup(msg, event):
    # this will block the rest of the coro until `event.set` is called
    await event.wait()
    # unhelpful simulation of i/o work
    await asyncio.sleep(random.random())
    logging.info(f'Done. Acked {msg}')


async def extend(msg, event):
    while not event.is_set():
        logging.info(f'Extended deadline by 3 seconds for {msg}')
        # want to sleep for less than the deadline amount
        await asyncio.sleep(2)


def handle_results(results):
    for result in results:
        if isinstance(result, Exception):
            logging.error(f'Caught exception: {result}')


async def handle_message(msg):
    event = asyncio.Event()

    asyncio.create_task(extend(msg, event))
    asyncio.create_task(cleanup(msg, event))

    results = await asyncio.gather(
        save(msg), restart_host(msg), return_exceptions=True)
    handle_results(results)
    event.set()


async def consume(queue):
    while True:
        msg = await queue.get()
        logging.info(f'Pulled {msg}')
        asyncio.create_task(handle_message(msg))


async def handle_exception(coro, loop):
    try:
        await coro
    except Exception:
        logging.error('Caught exception')
        loop.stop()


async def shutdown(signal, loop):
    logging.info(f'Received exit signal {signal.name}...')
    logging.info('Closing database connections')
    logging.info('Nacking outstanding messages')
    tasks = [t for t in asyncio.all_tasks() if t is not
             asyncio.current_task()]

    [task.cancel() for task in tasks]

    logging.info('Canceling outstanding tasks')
    await asyncio.gather(*tasks)
    loop.stop()
    logging.info('Shutdown complete.')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # May want to catch other signals too
    signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT)
    for s in signals:
        loop.add_signal_handler(
            s, lambda s=s: asyncio.create_task(shutdown(s, loop)))

    queue = asyncio.Queue()
    publisher_coro = handle_exception(publish(queue), loop)
    consumer_coro = handle_exception(consume(queue), loop)

    try:
        loop.create_task(publisher_coro)
        loop.create_task(consumer_coro)
        loop.run_forever()
    finally:
        logging.info('Cleaning up')
        loop.stop()