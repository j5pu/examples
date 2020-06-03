#!/usr/bin/env python
# encoding: utf-8

import inspect
import sys

print('--------------------------------------------------------------------------------tracer')

def tracer(frame, event, arg):
    if event != 'call':
        return
    code = frame.f_code
    locals = frame.f_locals
    line_no = frame.f_lineno
    func = code.co_name
    filename = code.co_filename
    CODE = 3
    line_co = ((inspect.getframeinfo(frame))[CODE])[0].strip(' ').rstrip('\n')
    variables = {var: vars(locals.get(var))  if hasattr(locals.get(var), '__dict__')
                 else locals.get(var) for var in locals if var[:1] != '_' or not var is 'sys'}
    line_variables = None

    params = ''
    pargs, args, kwargs, f_locals = inspect.getargvalues(frame)
    try:
        params = {**{parg: f_locals[parg] for parg in pargs}, **{args: f_locals[args]}, **{**f_locals[kwargs]}}
    except KeyError:
        pass

    caller_frame = frame.f_back
    caller_code = caller_frame.f_code
    caller_locals = caller_frame.f_locals
    caller_line_no = caller_frame.f_lineno
    caller_func = caller_code.co_name
    caller_filename = caller_code.co_filename
    caller_line_co = ((inspect.getframeinfo(caller_frame))[CODE])[0].strip(' ').rstrip('\n')
    caller_variables = {var: vars(value)  if hasattr(value, '__dict__')
                            else value for var, value in caller_locals.items() if caller_func != '<module>'}
    if func == 'write':
        return
    if event is 'call':
        print('{}:{}: {}: {}:{} -> {}:{}: {}({})'.format(caller_filename, caller_line_no, caller_line_co, caller_func, caller_variables, filename, line_no, func, params))
        tracer(frame, 'line', arg)
    if event is 'return':
        print('{}:{}: return {}'.format(func, line_no, arg))
    if event is 'line':
        print('{}:{}: {}: {}'.format(func, line_no, line_co, line_variables))
        tracer(frame, 'return', arg)
    if event is 'exception':
        exc_type, exc_value, exc_traceback = arg
        print('{}:{}: {}: {}:{} Tracing exception: %s "%s" on line %s of %s and traceback %s'.format(func, line_no, exc_type.__name__, exc_value, exc_traceback))
    return

def c(arg):
    try:
        raise RuntimeError('generating exception in c()')
    except RuntimeError:
        pass
def b(arg):
    val = arg * 5
    c(val)
    return val

def a(arg):
    val = b(arg)
    return val * 2

sys.settrace(tracer)
zeta = 2
a(1)

print('--------------------------------------------------------------------------------trace_lines')

def trace_lines(frame, event, arg):
    if event != 'line':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    print('  %s line %s file %s arg %s' % (func_name, line_no, filename, arg))

print('--------------------------------------------------------------------------------trace_calls1')

def trace_calls1(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    print('Call to %s on line %s of %s with arg %s' % (func_name, line_no, filename, arg))
    if func_name in TRACE_INTO:
        # Trace into this function
        return trace_lines
    return


def C(input):
    #print('input =', input)
    #print('Leaving C()')
    pass

def B(arg):
    val = arg * 5
    C(val)
    #print('Leaving B()')


def A():
    B(2)
    #print('Leaving A()')



TRACE_INTO = ['A', 'B', 'C']

sys.settrace(tracer)

A()
print('--------------------------------------------------------------------------------trace_calls_and_returns')
def trace_calls_and_returns(frame, event, arg):
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    if event == 'call':
        print('Call to %s on line %s of %s' % (func_name, line_no, filename))
        return trace_calls_and_returns
    elif event == 'return':
        print('%s => %s' % (func_name, arg))
    return

def b1():
    #print('in b1()')
    return 'response_from_b1 '

def a1():
    # print('in a1()')
    val = b1()
    return val * 2

sys.settrace(trace_calls_and_returns)
a1()
print('--------------------------------------------------------------------------------excepciones')


def trace_exceptions(frame, event, arg):
    if event != 'exception':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    exc_type, exc_value, exc_traceback = arg
    print('Tracing exception: %s "%s" on line %s of %s' % (exc_type.__name__, exc_value, line_no, func_name))


def trace_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name in TRACE_INTO:
        return trace_exceptions


def c2():
    raise RuntimeError('generating exception in c()')


def b2():
    c2()
    #print('Leaving b()')


def a2():
    b2()
    #print('Leaving a()')


TRACE_INTO = ['a2', 'b2', 'c2']

sys.settrace(trace_calls)
try:
    a2()
except Exception as e:
    pass
   # print('Exception handler:', e)