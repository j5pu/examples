import asyncio
'''
Callback updates
When using call_soon() or call_soon_threadsafe(),
we normally get a Handle object as a response that we can use to cancel the call.
Now there’s a Handle.cancelled() method to determine whether the call was already canceled. Meaning, we can better handle interrupts or exceptions that may cancel a task without your knowledge.

Another change is that any cancelled tasks will
no longer log exceptions. A nuisance where sometimes you might exit an application with running coroutines,
and the act of interrupting the calls would log exceptions. These messages could mislead the user into thinking that there was some previously unhandled problem, when really they were caused by the interruption itself.

Along the same lines of managing callbacks, loop.call_later() now returns callback objects
with a new when() method that tells us the absolute timestamp in which we expect to run.
'''
