#!/usr/bin/env python
# encoding: utf-8

import inspect
import sys

print('--------------------------------------------------------------------------------tracer')
import configparser
import logging.config
import os
import sqlalchemy
import traceback
import hunter
hunter.trace(hunter.Q(module='tbot', action=hunter.VarsPrinter('conf')))

#hunter.trace(module='tbot', action=hunter.CodePrinter)

hunter.trace(hunter.Q(module='tbot', function='prueba_hunter', kind='call', action=hunter.VarsPrinter('ala'))
             |
             # OR
             # show code that contains "conf_ini.conf.ini" on the current line
             # and it's not in Python's stdlib
             # and it contains "conf_ini" on the current line
             hunter.Q(module='tbot', action=lambda event: event.locals.get("conf_ini") == "conf.ini", stdlib=False,
                      source__contains="conf_ini"))
# region vars
__package__ = 'tbot'
__name__ = __package__
__module__ = __name__
__qualname__ = __name__

conf_ini = 'conf.ini'
log_ini = 'log.ini'
db_db = 'tbot.db'
DEFAULT_sem_name = 'DEFAULT'

FILE = 0
LINE = FILE_STACK = 1
FUNC = LINE_STACK = 2
CODE = FUNC_STACK = 3
CODE_STACK = 4
# endregion

# region env
sqlite_dialect = os.getenv('sqlite_dialect', 'NULL')
engine_sqlite_url = '{}{}'.format(sqlite_dialect, db_db)
mysql_dialect = os.getenv('mysql_dialect', 'NULL')
mysql_host = os.getenv('mysql_host', 'NULL')
mysql_alt = int(os.getenv('mysql_alt', 'NULL'))
mysql_password = os.getenv('mysql_password', 'NULL')
tor_password = os.getenv('tor_password', 'NULL')
tor_ctrl_alt_1 = int(os.getenv('tor_ctrl_alt_1', 'NULL'))
REGEX_HREF_LINK_1C_2C = os.getenv('REGEX_HREF_LINK_1C_2C', 'NULL')
MEGAGROUPS_WGET_FILE = os.getenv('MEGAGROUPS_WGET_FILE', 'NULL')
CRAWL_SH = os.getenv('WGET_SH', 'NULL')
MEGAGROUPS_PATTERN_1 = os.getenv('MEGAGROUPS_PATTERN_1', 'NULL')
MEGAGROUPS_PATTERN_2 = os.getenv('MEGAGROUPS_PATTERN_2', 'NULL')
MEGAGROUPS_PATTERN_3 = os.getenv('MEGAGROUPS_PATTERN_3', 'NULL')
MEGAGROUPS_PATTERN_4 = os.getenv('MEGAGROUPS_PATTERN_4', 'NULL')
MEGAGROUPS_PATTERN_5 = os.getenv('MEGAGROUPS_PATTERN_5', 'NULL')
MEGAGROUPS_PATTERN_6 = os.getenv('MEGAGROUPS_PATTERN_6', 'NULL')
MEGAGROUPS_PATTERN_7 = os.getenv('MEGAGROUPS_PATTERN_7', 'NULL')
MEGAGROUPS_PATTERN_8 = os.getenv('MEGAGROUPS_PATTERN_8', 'NULL')
MEGAGROUPS_PATTERN_EXCLUDE = [os.getenv('MEGAGROUPS_PATTERN_EXCLUDE', 'NULL')]

MEGAGROUPS_PATTERNS = [MEGAGROUPS_PATTERN_1, MEGAGROUPS_PATTERN_2, MEGAGROUPS_PATTERN_3, MEGAGROUPS_PATTERN_4,
                       MEGAGROUPS_PATTERN_5, MEGAGROUPS_PATTERN_6, MEGAGROUPS_PATTERN_7, MEGAGROUPS_PATTERN_8]
# endregion

# region conf.ini
conf = configparser.RawConfigParser()
conf.optionxform = str
conf.read(conf_ini)
# endregion

# region log.ini
log_conf = configparser.RawConfigParser()
log_conf.optionxform = str
log_conf.read(log_ini)
logging_update_levels = {logger_name: log_conf['logging_levels'][conf['log_common']['level']]
                         if logger_name in conf['log_common']['to']
                         else log_conf['logging_levels'][conf['log_default'][logger_name]]
                         for logger_name in conf['log_default']}
for logger_name, logger_level in logging_update_levels.items():
    log_conf.set(logger_name, 'level', logger_level)
with open(log_ini, "w+") as configfile:
    log_conf.write(configfile)
for pack in conf['log_other']:
    if pack is 'stem':
        logging.getLogger(pack).disabled()
    else:
        logging.getLogger(pack).setLevel(log_conf.getint('logging_values', conf['log_other'][pack]))
log_colors = dict(conf['log_colors'])
logging.config.fileConfig(log_ini, disable_existing_loggers=False)
logger = logging.getLogger(__name__)
# endregion

# region db
engine_url = '{0}{1}:{2}@{3}:{4}/{1}'.format(mysql_dialect, __package__, mysql_password, mysql_host, mysql_alt)
if conf['db']['db'] == 'sqlite':
    engine_url = '{}{}'.format(sqlite_dialect, db_db)
engine = sqlalchemy.create_engine(engine_url, echo=conf.getboolean('db', 'echo'))
# endregion
http_connection_debug_level = conf.getint('HTTPConnection', 'debuglevel')
ip_url = conf['default']['ip_url']

DEFAULT_sem_value = conf.getint('sem_value', DEFAULT_sem_name)
DEFAULT_sem_low = conf.getint('sem_low', DEFAULT_sem_name)
DEFAULT_sem_factor = conf.getfloat('sem_factor', DEFAULT_sem_name)
fmt = {
            'DEBUG': '[%(log_color)s%(bold)s%(levelname)-8s%(reset)s] - [%(log_color)s%(bold)s%(name)-60s%(reset)s][%(log_color)s%(bold)s%(lineno)-4d%(reset)s] - [%(log_color)s%(bold)s%(message)s%(reset)s] - [%(log_color)s%(bold)s%(locales)s%(reset)s]  - [%(log_color)s%(bold)s%(caller)s%(reset)s] - [%(log_color)s%(bold)s%(backer)s%(reset)s]',
            'INFO': '[%(log_color)s%(bold)s%(levelname)-8s%(reset)s] - [%(log_color)s%(bold)s%(name)-60s%(reset)s][%(log_color)s%(bold)s%(lineno)-4d%(reset)s] - [%(log_color)s%(bold)s%(message)s%(reset)s]',
            'WARNING': '[%(log_color)s%(bold)s%(levelname)-8s%(reset)s] - [%(log_color)s%(bold)s%(name)-60s%(reset)s][%(log_color)s%(bold)s%(lineno)-4d%(reset)s] - [%(log_color)s%(bold)s%(message)s%(reset)s]',
            'ERROR': '[%(log_color)s%(bold)s%(levelname)-8s%(reset)s] - [%(log_color)s%(bold)s%(name)-60s%(reset)s][%(log_color)s%(bold)s%(lineno)-4d%(reset)s] - [%(log_color)s%(bold)s%(message)s%(reset)s]',
            'CRITICAL': '[%(log_color)s%(bold)s%(levelname)-8s%(reset)s] - [%(log_color)s%(bold)s%(name)-60s%(reset)s][%(log_color)s%(bold)s%(lineno)-4d%(reset)s] - [%(log_color)s%(bold)s%(message)s%(reset)s] - [%(log_color)s%(bold)s%(exc_info)s%(reset)s] - [%(log_color)s%(bold)s%(exc_text)s%(reset)s]'}
d = {'locales': str(locals()).replace("\\",""), 'caller': None, 'backer': None, 'trace': None , 'exc': traceback.format_exc()}
logger.info('hola')
nieto = logger.getChild('nieto')
nieto.debug('nieto', stack_info=True, extra=d)
nieto.info('nieto')
nieto.warning('nieto')
nieto.error('nieto')
nieto.critical('nieto', exc_info=True, extra=d)
ala = 2
def prueba_hunter():
    ala = 2
prueba_hunter()
__all__ = [n for n in globals() if n[:1] != '_']
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