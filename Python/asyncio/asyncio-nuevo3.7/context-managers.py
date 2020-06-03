from contextlib import asynccontextmanager
import asyncio

'''
Async Context Managers
Another quality-of-life improvement. We now have the asynccontextmanager()
decorator for producing async context managers without the need for a class that
implements __aenter__() or __aexit__(). This behaves exactly like the contextmanager() decorator that we use today for synchronous code. They also added a new AbstractAsyncContextManager and AsyncExitStack to complement their synchronous cousins.

If you’re not familiar with the concept, asynchronous context managers will 
await at the async with line before entering their code block. 
To illustrate, imagine you want to access a web API asynchronously to obtain a list of resources. 
Before executing the list call, you have to login and use the token in your list call.
'''
@asynccontextmanager()
async def login(username, password):
    # Wait for the login to complete and return the token
    token = await _login_to_web_api(username, password)
    try:
        # Execute the context block
        yield token
    finally:
        # Logout
        await _logout_from_web_api(token)

async def list_resources():
    async with login(username, password) as token:
        # We are now logged in and have a valid token
        return await list_resources(token)