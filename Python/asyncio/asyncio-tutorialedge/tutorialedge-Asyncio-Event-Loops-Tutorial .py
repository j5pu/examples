#
import asyncio

# prueba: 1 - simple event loop
"""
Let’s take a quick look at how you can define a very simple event loop. 
In order to instantiate an event loop we’ll use asyncio.get_event_loop(), 
we’ll then start a try... finally and within the body of our try we’ll 
specify that we want our newly instantiated event loop to run until it 
has completed our myCoroutine() function.
"""
# Define a coroutine that takes in a future
async def mycoroutine1():
    print("My coroutine1")

# Spin up a quick and simple event loop
# and run until completed
loop1 = asyncio.get_event_loop()
try:
    loop1.run_until_complete(mycoroutine1())
finally:
#    loop1.close()
    pass

"""

"""

# prueba: 2 - run_until_complete() method
"""
Running Options
We have a number of options for running our event loops, we can either call 
run_forever() which will subsequently run our event loop until the stop() 
function is called, or we can call run_until_complete(future) and only run 
our event loop until whatever future object we’ve passed in has completed it’s execution.

The run_until_complete() method
Let’s take a quick look at the run_until_complete() function. 
In this example we’ll define our myWork() coroutine which we will then 
pass into our run_until_complete function and subsequently we should see our 
event loop run until this myWork() coroutine is finished it’s execution.

"""
import time

async def mywork2():
    print("Starting Work2")
    time.sleep(5)
    print("Finishing Work2")

loop2 = asyncio.get_event_loop()
try:
    loop2.run_until_complete(mywork2())
finally:
#    loop2.close()
    pass

"""

"""


# prueba: 3 - run_forever() method
"""
The run_forever() method
The alternative way of starting up your event loop is to call the run_forever() method 
which will subsequently start your asyncio based event loop and have it run indefinitely 
until the program comes to an end or the stop() method is called. It should be noted 
that calling this causes our main thread to block indefinitely.

Let’s take a look at a quick example which showcases the use of this method. 
We’ll first define our work() coroutine which will feature a while 
loop that will run indefinitely and simply print out Task Executed in 1 second intervals.
"""
async def work3():
    while True:
        await asyncio.sleep(1)
        print("Task Executed 3")

loop3 = asyncio.get_event_loop()
try:
    # prueba: asyncio coge el primer loop que esta corriendo o sea realmente est yendo por el loop1
    asyncio.ensure_future(work3())
    loop3.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop 3")
    # loop3.close()
    pass

"""

"""


# prueba: 4 - Running Multiple coroutines:

"""
Running Multiple coroutines:
If you wanted to run multiple coroutines indefinitely in parallel 
then you can do that by creating your x number of coroutines and 
have them run a while loop each. You would then call asyncio.ensure_future(function()) 
in order to enqueue them onto the loop and they would run indefinitely after that point.

"""
import time


async def firstworker4():
    while True:
        await asyncio.sleep(1)
        print("First Worker Executed 4")


async def secondworker4():
    while True:
        await asyncio.sleep(1)
        print("Second Worker Executed 4")


loop4 = asyncio.get_event_loop()
try:
    asyncio.ensure_future(firstworker4())
    asyncio.ensure_future(secondworker4())
    loop4.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop4")
    loop4.close()

"""

"""


if __name__ == '__main__':
    # prueba: 1 -


    # prueba: 2 -


    # prueba: 3 -


    # prueba: 4 -

    exit(0)