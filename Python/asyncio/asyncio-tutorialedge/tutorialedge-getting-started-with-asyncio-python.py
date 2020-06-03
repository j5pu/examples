# https://tutorialedge.net/python/concurrency/getting-started-with-asyncio-python/
import asyncio
import random
# prueba A: 1 - @asyncio.coroutine = async def.
# prueba A: 2 - yield from = await.
# prueba A: 3 - "@asyncio.coroutine" (decoras como asyncio a viejas) y "yield from" JUNTOS - "async def" y "await" JUNTOS

# https://docs.python.org/3/library/asyncio-task.html
# prueba:  event_loop: solo 1 tarea, para mas tareas mas event loop
# prueba:              lanza 1 tarea para ver futures.
# prueba:  task: espera a futures a que acabe.

# prueba: 1 - Getting Started
async def mycoroutine():
    print("Simple Event Loop Example")


def main1():
    # Define an instance of an event loop
    loop1 = asyncio.get_event_loop()
    # Tell this event loop to run until all the tasks assigned
    # to it are complete. In this example just the execution of
    # our myCoroutine() coroutine.
    loop1.run_until_complete(mycoroutine())
    # Tidying up our loop by calling close()
#    loop1.close()


# prueba: 2 - Coroutines

"""
Coroutines
So these coroutines are essentially lightweight versions of your more traditional threads. 
By using these we essentially enable ourselves to write asynchronous programs 
that are very similar to threads but they run on top of a single thread. 
We can define coroutines in 2 distinct ways.
"""


async def myfunc21():
    print("Coroutine 2.1")


@asyncio.coroutine
def myfunc22():
    print("Coroutine 2.2")


def main2():
    loop21 = asyncio.get_event_loop()
    loop21.run_until_complete(myfunc21())
#    loop21.close()

    loop22 = asyncio.get_event_loop()
    loop22.run_until_complete(myfunc22())
#    loop22.close()


# prueba: 3 - Futures
"""
Futures
Futures in asyncio are very much similar to the Future objects you would see within 
Python ThreadPoolExecutors or ProcessPoolExecutors and tt follows an almost identical implementation. Future objects are
created with the intention that they will eventually be given a result some time in the future, 
hence the name. This is beneficial as it means that within your Python program you can go off 
and perform other tasks whilst you are waiting for your Future to return a result.

Thankfully working with Futures in asyncio is relatively easy thanks to the ensure_future() 
method which takes in a coroutine and returns the Future version of that coroutine.
"""


# Define a coroutine that takes in a future
# prueba A: 1 - @asyncio.coroutine = async def.
@asyncio.coroutine
def mycoroutine3(future3):
#async def mycoroutine3(future3):

    # simulate some 'work'
    # prueba A: 2 - yield from = await.@asyncio.coroutine
    # await asyncio.sleep(1)
    yield from asyncio.sleep(1)
    # set the result of our future object
    future3.set_result("My Coroutine3-turned-future has completed")
    print("mycoroutine3 he acabado")


async def main3():
    # define a future object
    future3 = asyncio.Future()
    # wait for the completion of our coroutine that we've
    # turned into a future object using the ensure_future() function
    # prueba 3 - 1.- asyncio: asyncio equivale a &
    # prueba 3 - 2.- ensure_feature: es asegurate que acaba pero segura que acaba en bakcground (y si hubiera error seria en el try del envio ?pero el sigue y
    # prueba 3 - 3.- await: debe equivaler a como wait/read asi hasta que no haya hecho lo otro no hace el print.
    await asyncio.ensure_future(mycoroutine3(future3))
    # Print the result of our future
    print(future3.result())

    # prueba 3.- A.-Si quitasemos el await entonces haria el print antes de acabar pero el result estaria vacio no y sale ERRROR Result is not set?
    # asyncio.ensure_future(mycoroutine3(future3))
    # print(future3.result())

    # prueba 3.- B.- Si quitasemos el await entonces haria el print antes de acabar si le digo print("me salto to") entonces no error y sale antes
    # asyncio.ensure_future(mycoroutine3(future3))
    # print(future3)


"""
If you were to run this you should see that our program successfully turns our coroutine
into a future object and prints out the result.
"""


# prueba: 4 - Multiple Coroutines

"""
Multiple Coroutines
Let’s now try to take advantage of asyncio’s ability to run multiple coroutines concurrently.
This will hopefully give you some idea as to how powerful asyncio is and how you can use it to 
effectively create incredibly performant Python programs running on a single-thread.

Let’s start by creating a simple coroutine that takes in an id as its primary parameter. 
This will generate a random integer called process_length and wait for that length of time. 
It will then print out it’s id and how long it awaited for.

Next within our main() method we will generate 10 tasks that and then await these tasks 
completion using the await asyncio.gather() function, passing in our list of tasks. 
Finally we’ll utilize the same event loop from the previous example in order to run our asyncio program.
"""


async def mycoroutine4(id4):
    process_time4 = random.randint(1, 5)
    # prueba 4 - 3.- Este asyncio tambien crea un "thread" en & background aunque espera en la misma linea a que acabae, o sea es
    # prueba 4 - 3.-              como llamar a una funcion o coroutine pero llama a sleep. O sea ahora aqui mand los 10 al &
    await asyncio.sleep(process_time4)
    print("Coroutine4: {}, has successfully completed after {} seconds".format(id4, process_time4))


async def main4():
    tasks4 = []
    for i in range(10):
        # prueba 4 - 1.- asyncio: asyncio equivale a &
        # prueba 4 - 2.- ensure_feature: es asegurate que acaba pero segura que acaba en bakcground. No le pasamos future asi que nos da igual "future.result"
        tasks4.append(asyncio.ensure_future(mycoroutine4(i)))

        # prueba 4 - 3.- await: debe equivaler a como wait/read asi hasta que no haya hecho lo otro no hace el print.
        # prueba 4 - 4.- gather: debe equivaler espera a todos. en el tasks4 el ensure_future le habra puesto un objeto typo Future() y tendra .result o .state.
        # prueba 4 - 4.-        el objeto Future() tiene _exception, y _state=FINISHED PENDING

    # prueba 4 - 1.- Lanza las 10, estan en tasks4[]._state=PENDING
    # prueba 4 - 2.- Despues sube a mycoroutine4 a lanzar .
    await asyncio.gather(*tasks4)


if __name__ == '__main__':
    # prueba: 1 - Getting Started
    main1()

    # prueba: 2 - Coroutines
    main2()

    # prueba: 3 - Futures
    # Spin up a quick and simple event loop
    # and run until completed
    loop3 = asyncio.get_event_loop()
    try:
        loop3.run_until_complete(main3())
    finally:
        # loop3.close()
        pass

    # prueba: 4 - Multiple Coroutines
    loop4 = asyncio.get_event_loop()
    try:
        loop4.run_until_complete(main4())
    finally:
        loop4.close()
