
import inspect
import sys
def sample(a, b):
    x = a + b
    y = x * 2
    print('Sample: ' + str(y))

'''
Assuming that every time a new frame is executed,
you want a callback that prints the code object and
line number its executing, you can define it as:
'''
def trace_calls(frame, event, arg):
    if frame.f_code.co_name == "sample":
        print(frame.f_code)

        print('frame.f_code:', frame.f_code)
        return trace_lines

def trace_lines(frame, event, arg):
    print('frame.f_lineno', frame.f_lineno)
    source = inspect.getsourcelines(frame.f_code)[0]
    print('source:', source)


# Nota: un trace borra al anterior o sea sys.settrace(trace_lines) desactivaria
sys.settrace(trace_calls)


sample(2, 3)


sample(2, 4)

