#!/usr/bin/env python3
# Copyright (c) 2018 Lynn Root
"""
Working with threadpool executors.

Notice! This requires:
 - google-cloud-pubsub==0.35.4

You probably also want to run the Pub/Sub emulator to avoid calling/
setting up production Pub/Sub. For more details, see
https://cloud.google.com/pubsub/docs/emulator
"""

import asyncio
import concurrent.futures
import json
import logging
import os
import random
import signal
import string

from google.cloud import pubsub


# NB: Using f-strings with log messages may not be ideal since no matter
# what the log level is set at, f-strings will always be evaluated
# whereas the old form ('foo %s' % 'bar') is lazily-evaluated.
# But I just love f-strings.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s,%(msecs)d %(levelname)s: %(message)s',
    datefmt='%H:%M:%S',
)


TOPIC = 'projects/europython18/topics/ep18-topic'
SUBSCRIPTION = 'projects/europython18/subscriptions/ep18-sub'
PROJECT = 'europython18'
CHOICES = string.ascii_lowercase + string.digits


def get_publisher():
    """Get Google Pub/Sub publisher client."""
    client = pubsub.PublisherClient()
    try:
        client.create_topic(TOPIC)
    except Exception as e:
        # already created
        pass

    return client


def get_subscriber():
    """Get Google Pub/Sub subscriber client."""
    client = pubsub.SubscriberClient()
    try:
        client.create_subscription(SUBSCRIPTION, TOPIC)
    except Exception:
        # already created
        pass
    return client


def publish_sync():
    """Publish messages to Google Pub/Sub."""
    publisher = get_publisher()
    rand_max = random.randrange(1, 6)
    for msg in range(1, rand_max):
        msg_data = {'msg_id': ''.join(random.choices(CHOICES, k=4))}
        bytes_message = bytes(json.dumps(msg_data), encoding='utf-8')
        publisher.publish(TOPIC, bytes_message)
        logging.debug(f'Published {msg_data["msg_id"]}')


def consume_sync():
    """Consume messages from Google Pub/Sub."""
    client = get_subscriber()
    def callback(msg):
        msg.ack()
        data = json.loads(msg.data.decode('utf-8'))
        logging.info(f'Consumed {data["msg_id"]}')

    client.subscribe(SUBSCRIPTION, callback)


async def publish(executor):
    """Simulates an external publisher of messages.

    Args:
        executor (concurrent.futures.Executor): Executor to run sync
            functions in.
    """
    loop = asyncio.get_running_loop()
    while True:
        await loop.run_in_executor(executor, publish_sync)
        await asyncio.sleep(.11)


async def run_pubsub():
    """Entrypoint to run pub/sub coroutines."""
    loop = asyncio.get_running_loop()
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

    consume_coro = loop.run_in_executor(executor, consume_sync)

    asyncio.ensure_future(consume_coro)
    loop.create_task(publish(executor))


async def run_something_else():
    """Example of concurrency when using executors."""
    while True:
        logging.info('Running something else')
        await asyncio.sleep(.1)


async def run():
    """Entrypoint to run main coroutines."""
    coros = [run_pubsub(), run_something_else()]
    await asyncio.gather(*coros)


async def shutdown(signal, loop):
    """Simplified shutdown coroutine function."""
    logging.info(f'Received exit signal {signal.name}...')
    loop.stop()
    logging.info('Shutdown complete.')


if __name__ == '__main__':
    assert os.environ.get('PUBSUB_EMULATOR_HOST'), 'You should be running the emulator'

    loop = asyncio.get_event_loop()

    # for simplicity, probably want to catch other signals too
    loop.add_signal_handler(
        signal.SIGINT,
        lambda: asyncio.create_task(shutdown(signal.SIGINT, loop))
    )

    try:
        loop.create_task(run())
        loop.run_forever()
    finally:
        logging.info('Cleaning up')
        loop.stop()
