import asyncio
from asyncio import CancelledError, as_completed
import time
'''
Simpler Task Management
Along the same lines, there’s a new asyncio.create_task() function that helps make tasks
that inside the current loop, instead of having to get the loop first and calling create task on top of it.
While it makes code shorter and more readable, it also makes the loop selection implicit, so you’ll have to keep that in mind when scanning through code.

We also see the addition of current_task() and all_tasks() to the base asyncio module.
They make reasoning about async code a bit easier, especially since both the functions
take a loop argument to explicitly express the loop on which we’re operating.
These were previously class methods under the asyncio.Task class, but are now deprecated.
If you manage a package that depends on asyncio, you’ll want to start thinking about moving
any current_task() or all_tasks() calls to these new interfaces.

A common use case to illustrate the change is when canceling tasks on your way out of an async block:
'''
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print('asyncio.current_task:', asyncio.current_task)
    print('asyncio.all_tasks:', asyncio.all_tasks)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))
    print('asyncio.current_task:', asyncio.current_task)
    print('asyncio.all_tasks:', asyncio.all_tasks)

    task2 = asyncio.create_task(
        say_after(2, 'world'))
    print('asyncio.current_task:', asyncio.current_task)
    print('asyncio.all_tasks:', asyncio.all_tasks)

    print('started at', time.strftime('%X'))

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    print('asyncio.current_task:', asyncio.current_task)
    print('asyncio.all_tasks:', asyncio.all_tasks)

    await task2
    print('asyncio.current_task:', asyncio.current_task)
    print('asyncio.all_tasks:', asyncio.all_tasks)

    print('finished at', time.strftime('%X'))

asyncio.run(main())

'''
Futures

There is a dedicated section about the asyncio Future object, but the concept is fundamental to asyncio so it needs a brief introduction in this section.

A Future is a special low-level awaitable object that represents an eventual result of an asynchronous operation. 
Future objects in asyncio are needed to allow callback-based code to be used with async/await.

Normally, there is no need to create Future objects at the application level code.

Future objects, sometimes exposed by libraries and some asyncio APIs, should be awaited:
'''
async def nested():
    return 42

async def main():
    # await function_that_returns_a_future_object()
    print(await nested())

    # this is also valid:
    # await asyncio.gather( function_that_returns_a_future_object(), some_python_coroutine())
    await asyncio.gather(nested())

'''
Running Tasks Concurrently
awaitable asyncio.gather(*fs, loop=None, return_exceptions=False)
Run awaitable objects in the fs sequence concurrently.

If any awaitable in fs is a coroutine, it is automatically scheduled as a Task.

If all awaitables are completed successfully, the result is an aggregate list of returned values. The order of result values corresponds to the order of awaitables in fs.

If return_exceptions is True, exceptions are treated the same as successful results, and aggregated in the result list. Otherwise, the first raised exception is immediately propagated to the task that awaits on gather().

If gather is cancelled, all submitted awaitables (that have not completed yet) are also cancelled.

If any Task or Future from the fs sequence is cancelled, it is treated as if it raised CancelledError – the gather() call is not cancelled in this case. This is to prevent the cancellation of one submitted Task/Future to cause other Tasks/Futures to be cancelled.

Example:
'''
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

asyncio.run(main())

'''
Shielding Tasks From Cancellation
awaitable asyncio.shield(fut, *, loop=None)
Protect an awaitable object from being cancelled.

fut can be a coroutine, a Task, or a Future-like object. If fut is a coroutine it is automatically scheduled as a Task.

The statement:
res = await shield(something())
is equivalent to:

res = await something()
except that if the coroutine containing it is cancelled, the Task running in something() is not cancelled. From the point of view of something(), the cancellation did not happen. Although its caller is still cancelled, so the “await” expression still raises a CancelledError.

If something() is cancelled by other means (i.e. from within itself) that would also cancel shield().

If it is desired to completely ignore cancellation (not recommended) the shield() function should be combined with a try/except clause, as follows:
'''
async def main5():
    try:
        res = await asyncio.shield(nested())
        print('shield:', res)

    except CancelledError:
        res = None
        print('shield:', res)


asyncio.run(main5())
'''
Timeouts
coroutine asyncio.wait_for(fut, timeout, *, loop=None)
Wait for the fut awaitable to complete with a timeout.

If fut is a coroutine it is automatically scheduled as a Task.

timeout can either be None or a float or int number of seconds to wait for. If timeout is None, block until the future completes.

If a timeout occurs, it cancels the task and raises asyncio.TimeoutError.

To avoid the task cancellation, wrap it in shield().

The function will wait until the future is actually cancelled, so the total wait time may exceed the timeout.

If the wait is cancelled, the future fut is also cancelled.

The loop argument is deprecated and scheduled for removal in Python 4.0.

Example:
'''
async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())

'''
Waiting Primitives
coroutine asyncio.wait(fs, *, loop=None, timeout=None, return_when=ALL_COMPLETED)
Run awaitable objects in the fs sequence concurrently and block until the condition specified by return_when.

If any awaitable in fs is a coroutine, it is automatically scheduled as a Task.

Returns two sets of Tasks/Futures: (done, pending).

The loop argument is deprecated and scheduled for removal in Python 4.0.

timeout (a float or int), if specified, can be used to control the maximum number of seconds to wait before returning.

Note that this function does not raise asyncio.TimeoutError. Futures or Tasks that aren’t done when the timeout occurs are simply returned in the second set.

return_when indicates when this function should return. It must be one of the following constants:

Constant	Description
FIRST_COMPLETED	The function will return when any future finishes or is cancelled.
FIRST_EXCEPTION	The function will return when any future finishes by raising an exception. If no future raises an exception then it is equivalent to ALL_COMPLETED.
ALL_COMPLETED	The function will return when all futures finish or are cancelled.
Unlike wait_for(), wait() does not cancel the futures when a timeout occurs.

Usage:
'''

# async def main7():
#     done, pending = await asyncio.wait(nested)
#     print('done:', done)
#     print('pending:', pending)
#
#
# asyncio.run(main7())
'''
asyncio.as_completed(fs, *, loop=None, timeout=None)¶
Run awaitable objects in the fs set concurrently. Return an iterator of Future objects. Each Future object returned represents the earliest result from the set of the remaining awaitables.

Raises asyncio.TimeoutError if the timeout occurs before all Futures are done.

Example:

for f in as_completed(fs):
    earliest_result = await f
'''
# async def main9():
#      for f in as_completed(nested):
#          earliest_result = await f
#          print('earliest_result:', earliest_result)
#
# asyncio.run(main9())

'''
Scheduling From Other Threads
asyncio.run_coroutine_threadsafe(coro, loop)
Submit a coroutine to the given event loop. Thread-safe.

Return a concurrent.futures.Future to wait for the result from another OS thread.

This function is meant to be called from a different OS thread than the one where the event loop is running. Example:
'''
timeout = 2
# Create a coroutine
loop = asyncio.new_event_loop()

coro = asyncio.sleep(1, result=3)

# Submit the coroutine to a given loop
future = asyncio.run_coroutine_threadsafe(coro, loop)

# Wait for the result with an optional timeout argument
assert future.result(timeout) == 3

# If an exception is raised in the coroutine, the returned Future will be notified. It can also be used to cancel the task in the event loop:
try:
    result = future.result(timeout)
except asyncio.TimeoutError:
    print('The coroutine took too long, cancelling the task...')
    future.cancel()
except Exception as exc:
    print('The coroutine raised an exception: {!r}'.format(exc))
else:
    print('The coroutine returned: {!r}'.format(result))

