import asyncio

"""
Getting Multiple Pages Asynchronously - With Time Savings
We want to take advantage of the asynchronous nature of get_page() and save time. We modify our client to use a list with four instances of a task. 
This allows us to send out requests for all pages we want to retrieve without waiting for the answer before asking for the next page:
"""
"""Get "web pages.

Waiting until one pages is download before getting the next."
"""

import asyncio
from contextlib import closing
import time

from async_page import get_page


def get_multiple_pages(host, port, waits, show_time=True):
    """Get multiple pages.
    """
    start = time.perf_counter()
    pages = []
    tasks = []
    with closing(asyncio.get_event_loop()) as loop:
        for wait in waits:
            tasks.append(get_page(host, port, wait))
        pages = loop.run_until_complete(asyncio.gather(*tasks))
    duration = time.perf_counter() - start
    sum_waits = sum(waits)
    if show_time:
        msg = 'It took {:4.2f} seconds for a total waiting time of {:4.2f}.'
        print(msg.format(duration, sum_waits))
    return pages

if __name__ == '__main__':

    def main():
        """Test it.
        """
        pages = get_multiple_pages(host='localhost', port='8000',
                                   waits=[1, 5, 3, 2])
        for page in pages:
            print(page)

    main()


"""
The interesting part is in this loop:

with closing(asyncio.get_event_loop()) as loop:
    for wait in waits:
        tasks.append(get_page(host, port, wait))
    pages = loop.run_until_complete(asyncio.gather(*tasks))
"""
"""
We append all return values of get_page() to our lits of tasks. 
This allows us to send out all request, in our case four, without waiting for the answers. 
After sending all of them, we wait for the answers, using:

loop.run_until_complete(asyncio.gather(*tasks))
"""

"""
We used loop.run_until_complete() already for each call to get_page() in the previous section. 
The difference here is the use of asyncio.gather() that is called with all our tasks in the list tasks as arguments. 
The asyncio.gather(*tasks) means for our example with four list entries:

asyncio.gather(tasks[0], tasks[1], tasks[2], tasks[3])

"""

"""
So, for a list with 100 tasks it would mean:

asyncio.gather(tasks[0], tasks[1], tasks[2],
               # 96 more tasks here
               tasks[99])

"""