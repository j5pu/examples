# https://tutorialedge.net/python/concurrency/asyncio-tasks-tutorial/
import asyncio


# prueba: 1 - Tasks
"""
Tasks
Tasks within Asyncio are responsible for the execution of coroutines within an event loop. 
These tasks can only run in one event loop at one time and in order to achieve parallel execution you would have to run multiple event loops over multiple threads.

I like to think of tasks within asyncio in a similar regard to how we’d think of tasks when used 
in conjunction with executors or pools like we’ve demonstrated in previous chapters.

In this section we’ll look at some of the key functions that we can use in order to work with tasks within our asyncio based programs.

A Simple Example
One of the key things to note about tasks in Asyncio is that you don’t directly create them, you instead use the ensure_future() function or the AbstractEventLoop.create_task() method. 
Let’s take a quick look at how we can use a task generator function in order to generate 5 distinct tasks for our event loop to process.
"""
import time

async def myTask1():
    time.sleep(1)
    print("Processing Task 1")

async def myTaskGenerator1():
    for i in range(5):
        asyncio.ensure_future(myTask1())

loop = asyncio.get_event_loop()
loop.run_until_complete(myTaskGenerator1())
print("Completed All Tasks 1")
#loop.close()
# prueba: 2 - all_tasks() method
"""
Let’s now take a look at how we can retrieve all of our tasks using the all_tasks() method.

The all_tasks(loop=None) method
Being able to ascertain what tasks are currently pending can be important for systems in production needing to be able to anticipate things such as workload etc. 
The all_tasks() method gives us some incite as to what tasks are currently in a pending state before they are executed by our event loop.
"""
import time

async def myTask2():
    time.sleep(1)
    print("Processing Task 2")

async def main2():
    for i in range(5):
        asyncio.ensure_future(myTask2())
    pending = asyncio.Task.all_tasks()
    print(pending)

loop = asyncio.get_event_loop()
loop.run_until_complete(main2())
print("Completed All Tasks 2")
#loop.close()

# prueba: 3 - The cancel() function
"""
The cancel() function
Being able to effectively cancel pending tasks can be useful in scenarios where you are rate limiting the 
number of tasks being executed, or if you are trying to perform a graceful shutdown of your application. T
hankfully the asyncio API provides the necessary functionality for this to be done relatively easily.

"""

async def myTask3():
    time.sleep(1)
    print("Processing Task 3")

    for task in asyncio.Task.all_tasks():
        print(task)
        task.cancel()
        print(task)


async def main3():
    for i in range(5):
        asyncio.ensure_future(myTask3())


loop = asyncio.get_event_loop()
loop.run_until_complete(main3())
print("Completed All Tasks 3")
#loop.close()

"""
This should then print out the following in the console. Note that all tasks apart from the main() task go from pending to cancelling once we’ve called task.cancel().

"""


# prueba: 4 - The as_completed() function

"""
Task Functions
So we’ve looks at how we can interact with individual tasks but let’s now take a step back and look at how we can interact with them as a collective.

The as_completed() function
"""
async def myWorker4(number):
    return number * 2

async def main4(coros):
    for fs in asyncio.as_completed(coros):
        print(await fs, '4')

coros = [myWorker4(i) for i in range(5)]

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main4(coros))
except KeyboardInterrupt:
    pass
finally:
#    loop.close()
    pass

# prueba: 5 - The gather() function

"""
The gather() function
The gather() function returns one single future that aggregates all of the results from the given coroutines or futures passed into it. 
You should note that the results aren’t returned in the order they were submitted 
so if you care about order then you’ll have to implement some admin functionality to reorder results.
"""
async def myWorker5():
    print("Hello World 5")

async def main5():
    print("My Main 5")

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*[myWorker5() for i in range(5)]))
except KeyboardInterrupt:
    pass
finally:
    #    loop.close()
    pass

# prueba: 6 - The wait() function

"""
The wait() function
The wait() function simply blocks until the Future instances passed into it complete, upon completion this will 
then returned a named 2-tuple of sets. The first set contains futures that have completed, the second gives the uncompleted futures. 
This can be useful in scenarios where you have to process a task within a given time, say you 
were making a number of REST API calls or pulling messages from a queue on a broker, 
if they failed to complete within the given timeout you could possibly try to process them in a different way.
"""
async def myWorker6():
    print("Hello World 6")

async def main6():
    print("My Main 6")

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([myWorker6() for i in range(5)], timeout=2))
except KeyboardInterrupt:
    pass
finally:
    loop.close()

if __name__ == '__main__':
    # prueba: 1 -


    # prueba: 2 -


    # prueba: 3 -


    # prueba: 4 -

    exit(0)