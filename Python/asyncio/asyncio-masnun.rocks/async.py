# http://masnun.rocks/2016/10/06/async-python-the-different-forms-of-concurrency/
print("""
In Syncrhonous operations, the tasks are executed in sync, one after one
In asynchronous operations, tasks may start and complete independent of each other
Concurrency implies that two tasks make progress together.
Parallelism is in fact a form of concurrency. But parallelism is hardware dependent

Quick Recap:
- Sync: Blocking operations.
- Async: Non blocking operations.
- Concurrency: Making progress together.
- Parallelism: Making progress in parallel.


Threads & Processes:
- Threads allow us to run our operations concurrently. 
- But there was/is a problem with the Global Interpreter Lock (GIL) for which the threading could not provide true parallelism.
- However, with multiprocessing, it is now possible to leverage multiple cores with Python.

Threads:
- Let’s see a quick example. In the following code, the worker function will be run on multiple threads, asynchronously and concurrently.

import threading
import time
import random


def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print("I am Worker {}, I slept for {} seconds".format(number, sleep))


for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()

print("All Threads are queued, let's see when they finish!")

""")
import threading
import time
import random


def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print("------ I am Worker {}, I slept for {} seconds".format(number, sleep))

print("""
we start 5 threads, they make progress together and 
when we start the threads (and thus executing the worker function), 
the operation does not wait for the threads to complete before moving on to the next print statement. 
So this is an async operation
""")
for i in range(5):
    print("""we passed a function to the Thread constructor. But if we wanted we could also subclass it and implement the code as a method (in a more OOP way""")
    t = threading.Thread(target=worker, args=(i,))
    t.start()

print("All Threads are queued, let's see when they finish!")
print("""
Global Interpreter Lock (GIL)
- The GIL is a locking mechanism that the Python interpreter runs only one thread at a time
- That is only one thread can execute Python byte code at any given time
- This GIL makes sure that multiple threads DO NOT run in parallel.
- The Python Interpreter switches between threads to allow concurrency
""")
print("""

Processes:
- To get parallelism, Python introduced the multiprocessing module which provides APIs which will feel very similar if you have used Threading before

Here’s the modified version that uses Process instead of Thread.

import multiprocessing
import time
import random


def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print("I am Worker {}, I slept for {} seconds".format(number, sleep))


for i in range(5):
    t = multiprocessing.Process(target=worker, args=(i,))
    t.start()

print("All Processes are queued, let's see when they finish!")
""")
import multiprocessing
import time
import random


def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print("------ I am Worker {}, I slept for {} seconds".format(number, sleep))

print("""
That’s it, really! Now instead of multi threading, 
we are using multiple processes which are running on different core of your CPU (assuming you have multiple cores).
""")
for i in range(5):
    t = multiprocessing.Process(target=worker, args=(i,))
    t.start()

print("All Processes are queued, let's see when they finish!")

print("""
With the Pool class, we can also distribute one function execution across multiple processes for different input values. If we take the example from the official docs
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, [1, 2, 3]))

""")
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    p = Pool(5)
    print("""
    instead of iterating over the list of values and calling f on them one by one, we are actually running the function on different processes.
    One process executes f(1), another runs f(2) and another runs f(3). Finally the results are again aggregated in a list.
    This would allow us to break down heavy computations into smaller parts and run them in parallel for faster calculation
    https://pymotw.com/3/multiprocessing/index.html
    """)
    print('------- ',p.map(f, [1, 2, 3]))

print("""

concurrent.futures module
- packs some really great stuff for writing async codes easily
- favorites are the ThreadPoolExecutor and the ProcessPoolExecutor. These executors maintain a pool of threads or processes.
- We submit our tasks to the pool and it runs the tasks in available thread/process
- A Future object is returned which we can use to query and get the result when the task has completed.

from concurrent.futures import ThreadPoolExecutor
from time import sleep
 
def return_after_5_secs(message):
    sleep(5)
    return message
 
pool = ThreadPoolExecutor(3)
 
future = pool.submit(return_after_5_secs, ("hello"))
print(future.done())
sleep(5)
print(future.done())
print(future.result())
""")
from concurrent.futures import ThreadPoolExecutor
from time import sleep


def return_after_5_secs(message):
    sleep(5)
    return message


pool = ThreadPoolExecutor(3)

future = pool.submit(return_after_5_secs, ("hello"))
print('------- ', future.done())
sleep(5)
print('------- ', future.done())
print('------- ', future.result())

print("""
https://pymotw.com/3/concurrent.futures/
""")

print("""

----------------------------
Asyncio - Why, What and How?
----------------------------

Why do we need asyncio?
-----------------------
- Processes are costly to spawn.
- Let’s assume that we are using threads for I/O bound operations. 3 threads are doing different I/O tasks
- The interpreter would need to switch between the concurrent threads and give each of them some time in turns. Let’s call the threads - T1, T2 and T3
-
- The three threads have started their I/O operation.
    - T3 completes it first
    - T2 and T1 are still waiting for I/O
    - The Python interpreter switches to T1 but it’s still waiting
    - Fine, so it moves to T2, it’s still waiting
    - and then it moves to T3 which is ready and executes the code.
    
- T3 was ready but the interpreter switched between T2 and T1 first - that incurred switching costs which we could have avoided if the interpreter first moved to T3, right?

What is asyncio?
----------------
- Asyncio provides us an event loop. The event loop tracks different I/O events and switches to tasks which are ready and pauses the ones which are waiting on I/O
- There’s an event loop. And we have functions that run async, I/O operations:
    - We give our functions to the event loop and ask it to run those for us
    - The event loop gives us back a Future object, it’s like a promise that we will get something back in the future.
    - We hold on to the promise, time to time check if it has a value (when we feel impatient) and finally when the future has a value, we use it in some other operations.
    
- Asyncio uses generators and coroutines to pause and resume tasks. You can read these posts for more details:
    - http://masnun.com/2015/11/20/python-asyncio-future-task-and-the-event-loop.html
    - 
    
How do we use asyncio?
----------------------
- 
import asyncio
import datetime
import random


async def my_sleep_func():
    await asyncio.sleep(random.randint(0, 5))


async def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await my_sleep_func()


loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()

""")
import asyncio
import datetime
import random


async def my_sleep_func():
    print("""The await function can wait on other async functions (coroutines) to complete.
    await asyncio.sleep(random.randint(0, 5))

    """)
    await asyncio.sleep(random.randint(0, 5))
    print("""
    Whenever the await call is made, asyncio understands that the function is probably going to need some time.
    So it pauses the execution, starts monitoring any I/O event related to it and allows tasks to run.
    When asyncio notices that paused function’s I/O is ready, it resumes the function""")

print("""# We have an async function display_date which takes a number (as an identifier) and the event loop as parameters""")
print("""async def display_date(num, loop):""")
async def display_date(num, loop):
    end_time = loop.time() + 50.0
    print("""
    # The function has an infinite loop that breaks after 50 secs
    end_time = loop.time() + 50.0
    """)
    print("""
    # But during this 50 sec period, 
    while True:
    """)
    while True:
        print("""it repeatedly prints out the time and takes a nap
                print("Loop: {} Time: {}".format(num, datetime.datetime.now()))""")

        print("------- Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        print("""and takes a nap
        await my_sleep_func()
        """)
        await my_sleep_func()


loop = asyncio.get_event_loop()
print("""
We pass the function to event loop (using the ensure_future method).
We start running the event loop""")
asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()

print("""
-----------------------
Making the Right Choice
-----------------------

We have walked through the most popular forms of concurrency.
But the question remains - when should choose which one? It really depends on the use cases.
From my experience (and reading), I tend to follow this pseudo code:

if io_bound:
    if io_very_slow:
        print("Use Asyncio")
    else:
       print("Use Threads")
else:
    print("Multi Processing")


- CPU Bound => Multi Processing
- I/O Bound, Fast I/O, Limited Number of Connections => Multi Threading
- I/O Bound, Slow I/O, Many connections => Asyncio

""")


print("""
-----------------------------------------------
PYTHON ASYNCIO: FUTURE, TASK AND THE EVENT LOOP
-----------------------------------------------
http://masnun.com/2015/11/20/python-asyncio-future-task-and-the-event-loop.html

Event Loop:
-----------
- On any platform, when we want to do something asynchronously, it usually involves an event loop
- An event loop is a loop that can register tasks to be executed
    - execute them,
    - delay
    - or even cancel them
    - and handle different events related to these operations
- Generally, we schedule multiple async functions to the event loop
    - The loop runs one function
        - while that function waits for IO
        - it pauses it and runs another
    - When the first function completes IO
        - it is resumed
        - Thus two or more functions can co-operatively run together.
    
    - This the main goal of an event loop
    
- The event loop can also pass resource intensive functions to a thread pool for processing.
    -------------------------------------------------------------------------------------------------------------------------------------
    We just need to remember that the event loop is the mechanism through which we can schedule our async functions and get them executed
    -------------------------------------------------------------------------------------------------------------------------------------
    
Future/Tasks:
-------------
- A Future is an object that is supposed to have a result in the future.
- A Task is a subclass of Future that wraps a coroutine
- When the coroutine finishes, the result of the Task is realized

Coroutines:
-----------
- Coroutines is a way of pausing a function and returning a series of values periodically.
    - A coroutine can pause the execution of the function by using the yield yield from or await (python 3.5+) keywords in an expression. 
    - The function is paused until the yield statement actually gets a value.


Fitting Event Loop and Future/Task Together
-------------------------------------------
- We need an event loop and we need to register our future/task objects with the event loop
    1. The loop will schedule and run them
    2. We can add callbacks to our future/task objects so that we can be notified when a future has it’s results

- Very often we choose to use coroutines for our work.
    1. We wrap a coroutine in Future and get a Task object
        -. When a coroutine yields, it is paused.
        -. When it has a value, it is resumed
        -. When it returns, the Task has completed and gets a value
        -. Any associated callback is run
        -. If the coroutine raises an exception, the Task fails and not resolved.

import asyncio
 
 
@asyncio.coroutine
def slow_operation():
    # yield from suspends execution until
    # there's some result from asyncio.sleep
 
    yield from asyncio.sleep(1)
 
    # our task is done, here's the result
    return 'Future is done!'
 
 
def got_result(future):
    print(future.result())
 
 
# Our main event loop
loop = asyncio.get_event_loop()
 
# We create a task from a coroutine
task = loop.create_task(slow_operation())
 
# Please notify us when the task is complete
task.add_done_callback(got_result)
 
# The loop will close when the task has resolved
loop.run_until_complete(task)

""")
import asyncio

print("""
# @asyncio.coroutine declares it as a coroutine
@asyncio.coroutine
def slow_operation():
""")

@asyncio.coroutine
def slow_operation():
    # yield from suspends execution until
    # there's some result from asyncio.sleep

    yield from asyncio.sleep(1)

    # our task is done, here's the result
    return 'Future is done!'


def got_result(future):
    print('------- ', future.result())


# Our main event loop
loop = asyncio.get_event_loop()

print("""
# loop.create_task(slow_operation()) creates a task from the coroutine returned by slow_operation()
# We create a task from a coroutine
task = loop.create_task(slow_operation())
""")
# We create a task from a coroutine
task = loop.create_task(slow_operation())

print("""
# task.add_done_callback(got_result) adds a callback to our task
# Please notify us when the task is complete
task.add_done_callback(got_result)

""")
# Please notify us when the task is complete
task.add_done_callback(got_result)

print("""
# loop.run_until_complete(task) runs the event loop until the task is realized. As soon as it has value, the loop terminates
# The loop will close when the task has resolved
loop.run_until_complete(task)
""")

print("""
# The run_until_complete function is a nice way to manage the loop. 
# The loop will close when the task has resolved
loop.run_until_complete(task)
""")
# The loop will close when the task has resolved
loop.run_until_complete(task)


print("""
Of course we could do this:
---------------------------
import asyncio
 
 
async def slow_operation():
    await asyncio.sleep(1)
    return 'Future is done!'
 
 
def got_result(future):
    print(future.result())
 
    # We have result, so let's stop
    loop.stop()
 
 
loop = asyncio.get_event_loop()
task = loop.create_task(slow_operation())
task.add_done_callback(got_result)

# We run forever
loop.run_forever()

1. Here we make the loop run forever and from our callback
2. we explicitly shut it down when the future has resolved.
""")
import asyncio


async def slow_operation():
    await asyncio.sleep(1)
    print("""
    await asyncio.sleep(1)
    # 2. we explicitly shut it down when the future has resolved.
    return 'Future is done!'
""")
    return 'Future is done!'


def got_result(future):
    print('------- ', future.result())

    # We have result, so let's stop
    loop.stop()


loop = asyncio.get_event_loop()
task = loop.create_task(slow_operation())
task.add_done_callback(got_result)

print("""
# 1. Here we make the loop run forever and from our callback
""")
loop.run_forever()

# We run forever
loop.run_forever()


print("""
-----------------------------------------------------------------
PYTHON: GENERATORS, COROUTINES, NATIVE COROUTINES AND ASYNC/AWAIT
-----------------------------------------------------------------
http://masnun.com/2015/11/13/python-generators-coroutines-native-coroutines-and-async-await.html

Generators:
-----------
- Generators are functions that generates values
- A function usually returns a value and then the underlying scope is destroyed
- When we call again, the function is started from scratch
- It’s one time execution

    - But a generator function can yield a value and pause the execution of the function
    - The control is returned to the calling scope
    - Then we can again resume the execution when we want and get another value (if any)
    
def simple_gen():
    yield "Hello"
    yield "World"
 
 
gen = simple_gen()
print(next(gen))
print(next(gen))
""")

def simple_gen():
    yield "Hello"
    yield "World"

print("""

# a generator function doesn’t directly return any values 
# but when we call it, we get a generator object which is like an iterable (gen)
# gen = simple_gen()

""")
gen = simple_gen()
print("""

# So we can call next() on a generator object to iterate over the values. Or run a for loop.
print(next(gen))
""")
print('------- ', next(gen))
print('------- ', next(gen))

print("""
So how’s generators useful?

- Let’s say your boss has asked you to write a function to generate a sequence of number up to 100 (a super secret simplified version of range()).
    - You wrote it. You took an empty list and kept adding the numbers to it and then returned the list with the numbers.
    - But then the requirement changes and it needs to generate up to 10 million numbers.
    - If you store these numbers in a list, you will soon run out of memory. 
    - In such situations generators come into aid. 
- You can generate these numbers without storing them in a list. Just like this:

def generate_nums():
    num = 0
    while True:
        yield num
        num = num + 1
 
 
nums = generate_nums()
 
for x in nums:
    print(x)
 
    if x > 9:
        break
""")


def generate_nums():
    num = 0
    while True:
        yield num
        num = num + 1


nums = generate_nums()

for x in nums:
    print('------- ', x)

    if x > 9:
        break

print("""
- We didn’t dare run after the number hit 9. But if you try it on console, you will see how it keeps generating numbers one after one.
- And it does so by pausing the execution and resuming – back and forth into the function context.

Summary: 
--------
- A generator function is a function that can pause execution and generate multiple values instead of just returning one value.
- When called, it gives us a generator object which acts like an iterable.
- We can use (iterate over) the iterable to get the values one by one
""")

print("""

Coroutines:
-----------
In the last section we have seen that using generators we can pull data from a function context (and pause execution). 

What if we wanted to push some data too? 
- That’s where coroutines comes into play
    1.- The yield keyword we use to pull values can also be used as an expression (on the right side of “=”) inside the function
    2.- We can use the send() method on a generator object to pass values back into the function
    3.- This is called “generator based coroutines”. Here’s an example:
    
def coro():
    hello = yield "Hello"
    yield hello
 
 
c = coro()
print(next(c))
print(c.send("World"))


""")


def coro():
    print("""
    # 2.- This comes to yield "Hello" and we get “Hello”
    hello = yield "Hello"
    yield hello
    """)
    hello = yield "Hello"
    yield hello

print("""

OK, so what’s happening here?:

""")
c = coro()
print("""
# 1.- We first take the value as usual – using the next() function. 
print(next(c))
""")
print('------- ', next(c))
print("""
# 3.- Then we send in a value using the send() method.
print(c.send("World"))
""")
print('------- ', c.send("World"))

print("""
#    4.- It resumes the function and assigns the value we send to hello and moves on up to the next line and executes the statement. 
#    5.- So we get “World” as a return value of the send() method.

- When we’re using generator based coroutines, by the terms “generator” and “coroutine” we usually mean the same thing. 
- Though they are not exactly the same thing, it is very often used interchangeably in such cases. 
- However, with Python 3.5 we have async/await keywords along with native coroutines. We will discuss those later in this post.

Async I/O and the asyncio module
--------------------------------
- We have the new asyncio module which provides nice APIs for general async programming.
- We can use coroutines with the asyncio module to easily do async io. Here’s an example from the official docs

import asyncio
import datetime
import random
 
 
@asyncio.coroutine
def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        yield from asyncio.sleep(random.randint(0, 5))
 
 
loop = asyncio.get_event_loop()
 
asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))
 
loop.run_forever()

""")
import asyncio
import datetime
import random

print("""

# 2. We create a coroutine display_date(num, loop) which takes an identifier (number)
@asyncio.coroutine
def display_date(num, loop):

""")
@asyncio.coroutine
def display_date(num, loop):
    print("""
    # 3. and an event loop and continues to print the current time
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
    """)
    end_time = loop.time() + 50.0
    while True:
        print("'------- ', Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        print("""
        # 4. Then it used the yield from keyword to await results from asyncio.sleep() function call.
        yield from asyncio.sleep(random.randint(0, 5))
        # 4.1.- The function is a coroutine which completes after a given seconds. So we pass random seconds to it
        # 7.1.- When we use yield from, the event loop knows that it’s going to be busy for a while so it pauses execution of the coroutine and runs another
        yield from asyncio.sleep(random.randint(0, 5))

        """)
        yield from asyncio.sleep(random.randint(0, 5))

print("""
# 1.-The code is pretty self explanatory.
loop = asyncio.get_event_loop()
""")
loop = asyncio.get_event_loop()

print("""
# 5.- Then we use asyncio.ensure_future() to schedule the execution of the coroutine in the default event loop
asyncio.ensure_future(display_date(1, loop))
 """)
asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))
print("""
# 6.- Then we ask the loop to keep running.
loop.run_forever()
 """)
loop.run_forever()
print("""
# 7.- If we see the output, we shall see that the two coroutines are executed concurrently

# 7.2.- Thus two coroutines run concurrently (but not in parallel since the event loop is single threaded).

# 8.- Just so you know, yield from is a nice syntactic sugar for
for x in asyncio.sleep(random.randint(0, 5)): yield x making async codes cleaner.
""")


print("""

Native Coroutines and async/await:
----------------------------------
Remember, we’re still using generator based coroutines?. 

In Python 3.5 we got the new native coroutines which uses the async/await syntax
- The previous function can be written this way:

""")

print("""-------------------------""")
print("""
import asyncio
import datetime
import random
""")
import asyncio
import datetime
import random

print("""
# 1.- We must define a native coroutine with the async keyword before the def keyword
async def display_date(num, loop, ):

""")
async def display_date(num, loop, ):
    print("""
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
    """)
    end_time = loop.time() + 50.0
    while True:
        print('------- ', "Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        print("""
        # 2.- Inside a native coroutine, we use the await keyword instead of yield from
        await asyncio.sleep(random.randint(0, 5))
        """)
        await asyncio.sleep(random.randint(0, 5))

print("""
loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()
""")
loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()

print("""

Native vs Generator Based Coroutines: Interoperability:
-------------------------------------------------------
There’s no functional differences between the Native and Generator based coroutines except the differences in the syntax
- It is not permitted to mix the syntaxes. We can not use:
    1.- await inside a generator based coroutine or
    2.- yield/yield from inside a native coroutine.

Despite the differences, we can interoperate between those.
- We just need to add @types.coroutine decorator to old generator based ones. Then we can use one from inside the other type
    1.- That is we can await from generator based coroutines inside a native coroutine and
    2.- yield from native coroutines when we are inside generator based coroutines.

Here’s an example:

import asyncio
import datetime
import random
import types
 
 
@types.coroutine
def my_sleep_func():
    yield from asyncio.sleep(random.randint(0, 5))
 
 
async def display_date(num, loop, ):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await my_sleep_func()
 
 
loop = asyncio.get_event_loop()
 
asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))
 
loop.run_forever()

""")

import asyncio
import datetime
import random
import types


@types.coroutine
def my_sleep_func():
    yield from asyncio.sleep(random.randint(0, 5))


async def display_date(num, loop, ):
    end_time = loop.time() + 50.0
    while True:
        print('------- ', "Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await my_sleep_func()


loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()
