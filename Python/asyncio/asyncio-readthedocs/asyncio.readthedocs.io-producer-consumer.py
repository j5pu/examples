import asyncio

# prueba 1 - Simple example
import random


async def produce(queue, n):
    for x in range(1, n + 1):
        # produce an item
        print('producing {}/{}'.format(x, n))
        # simulate i/o operation using sleep
        await asyncio.sleep(random.random())
        item = str(x)
        # put the item in the queue
        await queue.put(item)

    # indicate the producer is done
    await queue.put(None)


async def consume(queue):
    while True:
        # wait for an item from the producer
        item = await queue.get()
        if item is None:
            # the producer emits None to indicate that it is done
            break

        # process the item
        print('consuming item {}...'.format(item))
        # simulate i/o operation using sleep
        await asyncio.sleep(random.random())


loop = asyncio.get_event_loop()
queue = asyncio.Queue(loop=loop)
producer_coro = produce(queue, 10)
consumer_coro = consume(queue)
loop.run_until_complete(asyncio.gather(producer_coro, consumer_coro))
#loop.close()


# prueba 2 - Using task_done() and Queue.join
async def produce(queue, n):
    for x in range(n):
        # produce an item
        print('producing {}/{}'.format(x, n))
        # simulate i/o operation using sleep
        await asyncio.sleep(random.random())
        item = str(x)
        # put the item in the queue
        await queue.put(item)


async def consume(queue):
    while True:
        # wait for an item from the producer
        item = await queue.get()

        # process the item
        print('consuming {}...'.format(item))
        # simulate i/o operation using sleep
        await asyncio.sleep(random.random())

        # Notify the queue that the item has been processed
        queue.task_done()


async def run(n):
    queue = asyncio.Queue()
    # schedule the consumer
    consumer = asyncio.ensure_future(consume(queue))
    # run the producer and wait for completion
    await produce(queue, n)
    # wait until the consumer has processed all items
    await queue.join()
    # the consumer is still awaiting for an item, cancel it
    consumer.cancel()


loop = asyncio.get_event_loop()
loop.run_until_complete(run(10))
loop.close()