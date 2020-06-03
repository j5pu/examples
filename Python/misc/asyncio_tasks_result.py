#!/usr/py/bin/python3.7
import utils
import asyncio

__package__ = 'tbot'

async def crawl():
    curl = utils.Curl()
    urls = ['https://t.me/thebitcoinnews', 'https://t.me/coinstaker', 'https://t.me/coinstaker']
    tasks = [asyncio.create_task(curl.sem(utils.aiocurl_eurl, turl)) for turl in urls]

    telegrams = await asyncio.gather(*tasks)

    conjunto_tasks = {task.result().result() for task in tasks}
    set_tasks = set(task.result().result() for task in tasks)
    conjunto_set_tasks = set(conjunto_tasks)
    conjunto_telegrams = {telegram.result() for telegram in telegrams}
    set_telegrams = set(telegram.result() for telegram in telegrams)
    conjunto_set_telegrams = set(conjunto_telegrams)

    print('--------------conjunto_tasks: ', conjunto_tasks)
    print('--------------set_tasks: ', set_tasks)
    print('--------------conjunto_set_tasks: ', conjunto_set_tasks)

    print('--------------conjunto_telegrams: ', conjunto_telegrams)
    print('--------------set_telegrams: ', set_telegrams)
    print('--------------conjunto_set_telegrams: ', conjunto_set_telegrams)


if __name__ == '__main__':
    asyncio.run(crawl())