# If the goal is "when an exception was raised, do something different", how about:
#
# exception_raised = False
# try:
#     value = my_function(*args)
# except:
#     exception_raised = True
#     raise
# finally:
#     with some_context_manager:
#         do_something()
#         if not exception_raised:
#             do_something_else(value)
# Now, if you're going to have multiple exceptions that you actually do something with, I'd recommend:
#
# completed_successfully = False
# try:
#     value = my_function(*args)
# else:
#     completed_successfully = True
# finally:
#     with some_context_manager:
#         do_something()
#         if completed_sucessfully:
#             do_something_else(value)