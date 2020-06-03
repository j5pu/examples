import asyncio

'''
Simpler Event Loop Management
It’s not hard to get the current event loop by using asyncio.get_event_loop(),
but you’ll have to make separate calls to determine its state of execution.
Most folks that are new to asyncio are not aware of the distinction, nor do they realize that different modules
can make their own loops, instead of interacting with the one loop in which you’re usually operating.

The addition of asyncio.get_running_loop() will help determine the active event loop,
and catch a RuntimeError if there’s no loop running. While I expect this to see less overall usage than the other changes,
it will definitely help many modules that are dependent on running things in their own loop. It simplifies interoperability between different modules that use asyncio.

Also in the same category, the Task, Server and Future classes now have get_loop() functions
to determine which loop they are running on. This completes the loop management picture by helping us
find which tasks are scheduled to run or, even better, which loops our futures are waiting on. Again, not something that I would expect your every day async code to manage, but there’s several of us that make frameworks or modules that will find the functionality valuable.

'''