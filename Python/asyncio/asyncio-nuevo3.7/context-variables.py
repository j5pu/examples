import asyncio
import contextvars

'''
Context Variables
Version 3.7 now allows the use of context variables within async tasks.
If this is a new concept to you, it might be easier to picture it as global variables whose values are local to the currently running coroutines.

Consider a client-server system where the server is managing a connection to a specific client address.
To operate on the client you might need to pass the address around between coroutines.
But with context variables, any client communication tasks could reference the information with the same name,
but the value would differ depending on which client its talking to (each client is in a different context).

The example below (taken from the documentation) illustrates this scenario fairly well.
An asyncio server executes handle_request() when a new client connects. This sets the client_addr_var context variable,
which we then access in render_goodbye() without having to pass it as a parameter.
'''

client_addr_var = contextvars.ContextVar('client_addr')

def render_goodbye(render_addr):
    # The address of the currently handled client can be accessed
    # without passing it explicitly to this function.
    print('render_addr:', render_addr)
    client_addr = client_addr_var.get()
    print('client_addr:', client_addr)
    client_addr_var.set('tonto')
    new_client_addr = ('127.0.0.1', 99999)
    # Pero no se pueden modificar
    print('client_addr_var.set(new_client_addr):', client_addr_var.set(new_client_addr))

    return f'Good bye, client @ {client_addr}\n'.encode()

async def handle_request(reader, writer):
    addr = writer.transport.get_extra_info('socket').getpeername()
    print('addr:', addr)

    client_addr_var.set(addr)
    print('client_addr_var.get(addr):', client_addr_var.get(addr))
    # In any code that we call is now possible to get
    # client's address by calling 'client_addr_var.get()'.

    while True:
        line = await reader.readline()
        print(line)
        if not line.strip():
            break
        writer.write(line)
    # meto:addr
    writer.write(render_goodbye(addr))
    writer.close()

async def main():
    srv = await asyncio.start_server(
        handle_request, '127.0.0.1', 8081)

    async with srv:
        await srv.serve_forever()

asyncio.run(main())

# To test it you can use telnet:
#     telnet 127.0.0.1 8081
'''
Python has similar constructs for doing this very thing across threads. However, those were not sufficient in async-world
because each thread could run multiple coroutine contexts. Having asyncio support for context variables directly solves that issue.

To further expand on the concept, the coroutine scheduling functions loop.call_soon(), loop.call_soon_threadsafe(), 
loop.call_later(), loop.call_at(), and Future.add_done_callback() can now handle an optional 
keyword-only context parameter so that tasks can manage their context automatically.

For more details check out PEP567 and the contextvars module.

A quick warning before moving on: Just because you can do this doesn’t mean you should do it. 
Overuse will make your code appear magical and therefore hard to read. 
Since our ultimate goal is to write readable code, please think about it carefully before you decide to use it.
'''