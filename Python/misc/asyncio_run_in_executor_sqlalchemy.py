from crawler.megagroups import groups
import concurrent.futures
import asyncio


def blocking_io():
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    with open('/dev/urandom', 'rb') as f:
        return f.read(100)


def cpu_bound():
    # CPU-bound operations will block the event loop:
    # in general it is preferable to run them in a
    # process pool.
    return sum(i * i for i in range(10 ** 7))


async def main():
    loop = asyncio.get_running_loop()

    # Options:
    # Use functools.partial() to pass keyword arguments to func.

    # 1. Run in the default loop's executor:
    result = await loop.run_in_executor(
        None, groups)
    print('default thread pool', result)

    # 2. Run in a custom thread pool (blocking_io):
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, groups)
        print('custom thread pool', result)

    # 3. Run in a custom process pool (cpu_bound):
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, groups)
        print('custom process pool', result)


asyncio.run(main())
