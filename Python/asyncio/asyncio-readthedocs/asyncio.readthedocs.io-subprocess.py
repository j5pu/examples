import asyncio

# prueba 1 - Run a subprocess and read its output¶

async def run_command(*args):
    # Create subprocess
    process = await asyncio.create_subprocess_exec(
        *args,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE)
    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()
    # Return stdout
    return stdout.decode().strip()


loop = asyncio.get_event_loop()
# Gather uname and date commands
commands = asyncio.gather(run_command('uname'), run_command('date'))
# Run the commands
uname, date = loop.run_until_complete(commands)
# Print a report
print('uname: {}, date: {}'.format(uname, date))
#loop.close()

# prueba 1 - Communicate with a subprocess using standard streams¶

async def echo(msg):
    # Run an echo subprocess
    process = await asyncio.create_subprocess_exec(
        'cat',
        # stdin must a pipe to be accessible as process.stdin
        stdin=asyncio.subprocess.PIPE,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE)
    # Write message
    print('Writing {!r} ...'.format(msg))
    process.stdin.write(msg.encode() + b'\n')
    # Read reply
    data = await process.stdout.readline()
    reply = data.decode().strip()
    print('Received {!r}'.format(reply))
    # Stop the subprocess
    process.terminate()
    code = await process.wait()
    print('Terminated with code {}'.format(code))


loop = asyncio.get_event_loop()
loop.run_until_complete(echo('hello!'))
loop.close()