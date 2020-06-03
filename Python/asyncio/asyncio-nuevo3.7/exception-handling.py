'''
Generator Exception Handling
PEP 479 is now fully implemented in 3.7, this fixes the situation in which a
generator that raises StopIteration may mask a real problem somewhere in the call stack.
From now on, directly or indirectly
raising StopIteration in coroutines and generators will transform into RuntimeError exceptions instead.
I suggest looking at the PEP for more information.
'''