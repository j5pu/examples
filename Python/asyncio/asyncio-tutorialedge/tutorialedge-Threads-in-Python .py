# https://tutorialedge.net/python/concurrency/threads-in-python/
import threading
# prueba: 1 - threads
"""
Creating a Simple Thread
Before we go into creating a thread in Python, we should take a look at 
the Python Thread class constructor and see what we need to pass in:

# Python Thread class Constructor
def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
It takes in five distinct parameters:

group: a special parameter which is reserved for future extension
target: the callable object to be invoked by the run method(), if None then nothing will be started…
name: Our threads name
args: argument tuple for target invocation. defaults to ()
kwargs: dictionary keyword argument to invoke the base class constructor
The key one to notice is the target parameter. In order to start a simple thread 
we need to be able to pass it something to run. Let’s create a simple function which we’ll then use to create our first thread like so:
"""

# The simple function that will simply print hello world and
# the thread that is executing this
def myTask():
    print("Hello World: {}".format(threading.current_thread()))

# We create our first thread and pass in our myTask function
# as its target
myFirstThread = threading.Thread(target=myTask)
# We start out thread
myFirstThread.start()

"""

"""


# prueba: 2 -
"""

"""


"""

"""


# prueba: 3 -
"""

"""


"""

"""


# prueba: 4 -

"""

"""


"""

"""


if __name__ == '__main__':
    # prueba: 1 -


    # prueba: 2 -


    # prueba: 3 -


    # prueba: 4 -

    exit(0)