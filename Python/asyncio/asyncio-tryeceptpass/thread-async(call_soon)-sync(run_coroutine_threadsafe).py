from configuracion import *


...

def is_async_caller():
    """Figure out who's calling."""

    # Get the calling frame
    caller = inspect.currentframe().f_back.f_back

    # Pull the function name from FrameInfo
    func_name = inspect.getframeinfo(caller)[2]

    # Get the function object
    f = caller.f_locals.get(
        func_name,
        caller.f_globals.get(func_name)
    )

    # If there's any indication that the function object is a
    # coroutine, return True. inspect.iscoroutinefunction() should
    # be all we need, the rest are here to illustrate.

    if any([inspect.iscoroutinefunction(f),
            inspect.isgeneratorfunction(f),
            inspect.iscoroutine(f), inspect.isawaitable(f),
            inspect.isasyncgenfunction(f) , inspect.isasyncgen(f)]):
        return True
    else:
        return False

def fetch(url):
    """GET the URL, do it asynchronously if the caller is async"""
    # Figure out which function is calling us
    if is_async_caller():
        print("Calling ASYNC method")

        # Run the async version of this method and
        # print the result with a callback
        asyncio.run_coroutine_threadsafe(
            _async_fetch(url),
            new_loop
        ).add_done_callback(lambda f: print(f.result()))

    else:
        print("Calling BLOCKING method")

        # Run the synchronous version and print the result
        print(_sync_fetch(url))

def _sync_fetch(url):
    """Blocking GET"""

    return requests.get(url).content

async def _async_fetch(url):
    """Async GET"""

    resp = await aiohttp.request('GET', url)
    return await resp.text()

def call_sync_fetch():
    """Blocking fetch call"""

    fetch("http://www.github.com")

async def call_async_fetch():
    """Asynchronous fetch call (no different from sync call
       except this function is defined async)"""

    fetch("http://www.github.com")

# Perform a blocking GET
call_sync_fetch()

# Perform an async GET
loop = asyncio.get_event_loop()
loop.run_until_complete(call_async_fetch())