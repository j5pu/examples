import asyncio
import concurrent.futures
import configparser
import enum
import inspect
import io
import logging
import logging.config
import logging.handlers
import os
import pycurl
import random
import sys
import threading
import time
import aiohttp
import aiotask_context
import colorlog
import sqlalchemy
import sqlalchemy.exc
import sqlalchemy.exc
import sqlalchemy.orm
import sqlalchemy_utils
import verboselogs
from aioify import aioify
import contextlib

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy_mixins import AllFeaturesMixin
from stem import Signal
from stem.control import Controller
import socket
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.proxy import Proxy, ProxyType
# region Env - Vars
http_proxy = os.getenv('http_proxy', 'NULL')
privoxy_host_port = os.getenv('privoxy_host_port', 'NULL')
tor_control_alt = int(os.getenv('tor_control_alt', 'NULL'))
tor_password = os.getenv('tor_password', 'NULL')

# endregion Env - Vars
#
#
# # region Functions
# def vars_to_dict(search_dict, variables):
#     """Convierte palabras de un string o lista en diccionario con variables y valores buscando en un dict"""
#     if isinstance(variables, str):
#         return {key: value for key, value in search_dict.items() for var in variables.split() if key == var}
#     elif isinstance(variables, list):
#         return {key: value for key, value in search_dict.items() for var in variables if key == var}
#     elif isinstance(variables, dict):
#         return {key: value for key, value in search_dict.items() for var in variables.keys() if key == var}
#
#
# def reverse_dict(d):
#     keys_list = list(map(lambda k: k, d))
#     reverse_key_list = keys_list[::-1]
#     reverse_d = dict()
#     i = 0
#     while i < len(reverse_key_list):
#         key = reverse_key_list[int(i)]
#         reverse_d[key] = d[key]
#         i += 1
#     if len(reverse_d) > 0:
#         return reverse_d
#
#
# def is_file(file):
#     try:
#         file = open(file, "r")
#     except FileNotFoundError:
#         raise
#     else:
#         file.close()
#
#
# def is_async_caller():
#     caller = inspect.currentframe().f_back.f_back
#     func_name = inspect.getframeinfo(caller)[2]
#
#     f = caller.f_locals.get(func_name, caller.f_globals.get(func_name))
#
#     if any([inspect.iscoroutinefunction(f), inspect.isgeneratorfunction(f), inspect.iscoroutine(f),
#             inspect.isawaitable(f), inspect.isasyncgenfunction(f), inspect.isasyncgen(f)]):
#         return True
#     else:
#         return False
#
#
# def ip():
#     l = log()
#
#     l.m(msg='Rotating IP')
#
#     old_ip = Net.ip()
#
#     with Controller.from_port(port=tor_control_alt) as controller:
#         controller.authenticate(tor_password)
#         controller.signal(Signal.NEWNYM)
#
#     new_ip = Net.ip()
#
#     if new_ip is old_ip:
#         l.e(msg='IP Not Changed: {}'.format(new_ip))
#     elif 'Error from' in new_ip:
#         l.e(msg='IP Changed: {}'.format(new_ip))
#     else:
#         l.i(msg='IP Changed: {}'.format(new_ip))
#
#
# async def aioip():
#     l = log()
#
#     l.m(msg='Rotating IP')
#
#     async with Net.aioget('http://ipecho.net/plain', retry=False, client=Net.clients[0]) as response:
#         old_ip = (await response.read()).decode()
#         print(old_ip)
#         try:
#             socket.inet_aton(old_ip)
#             l.m(msg='IP: {}'.format(old_ip))
#         except socket.error:
#             old_ip = None
#             l.e(msg='IP: Error - old_ip: from {}'.format(__init__.config.ip_url))
#
#     with Controller.from_port(port=tor_control_alt) as controller:
#         controller.authenticate(tor_password)
#         controller.signal(Signal.NEWNYM)
#
#     async with Net.aioget('http://ipecho.net/plain', retry=False, client=Net.clients[0]) as response:
#         new_ip = (await response.read()).decode()
#         print(new_ip)
#
#         try:
#             socket.inet_aton(new_ip)
#             l.m(msg='IP: {}'.format(new_ip))
#         except socket.error:
#             new_ip = None
#             l.e(msg='IP: Error - new_ip: from {}'.format(__init__.config.ip_url))
#
#     if old_ip and new_ip and old_ip != new_ip:
#         l.i(msg='IP Changed: {}'.format(new_ip))
#     elif old_ip == new_ip:
#         l.e(msg='IP Not Changed: {}'.format(new_ip))
#     elif not old_ip and new_ip:
#         l.i(msg='IP Probably Changed: new_ip == {}'.format(new_ip))
#     elif old_ip and not new_ip:
#         l.i(msg='IP Probably Changed: old_ip == {}'.format(old_ip))
#
#
# async def executor(func, pool='default'):
#     l = log()
#     loop = get()
#
#     if not func:
#         raise ValueError
#
#     if pool == 'thread':
#         with concurrent.futures.ThreadPoolExecutor() as thread_pool:
#             l.d(msg='Custom executor: thread_pool == {} - func  == {}'.format(thread_pool, func))
#             return await loop.run_in_executor(thread_pool, func)
#     elif pool == 'process':
#         with concurrent.futures.ProcessPoolExecutor() as process_pool:
#             l.d(msg='Custom executor: process_pool  == {} - func  == {}'.format(process_pool, func))
#             return await loop.run_in_executor(process_pool, func)
#     elif pool == 'default':
#         # 3. Run in the default loop's executor (blocking_io):
#         l.d(msg='Default executor:  loop == {} - func  == {}'.format(loop, func))
#         return await loop.run_in_executor(None, func)
#     else:
#         raise ValueError
#
#
# async def aiocmd(command):
#     """
#     rc, out, err = await utils.aiocmd('ls')
#
#     print(rc)
#     print(out)
#     print(err)
#
#     :param command:
#     :return:
#     """
#     proc = await asyncio.create_subprocess_shell(command, stdout=asyncio.subprocess.PIPE,
#                                                  stderr=asyncio.subprocess.PIPE)
#     stdout, stderr = await proc.communicate()
#     stdout = stdout.decode()
#     stderr = stderr.decode()
#     return proc.returncode, stdout, stderr
#
#
# async def gather(*tasks):
#     """
#         results = await utils.gather(*[curl.sem(utils.aiocurl_eurl, turl) for turl in urls])
#
#     Ejemplo:
#         curl = utils.Curl()
#         urls = ['https://t.me/thebitcoinnews', 'https://t.me/coinstaker', 'https://t.me/coinstaker']
#
#         results = await utils.gather(*[curl.sem(utils.aiocurl_eurl, turl) for turl in urls])
#         print('results: ', results)
#
#         for result in results:
#             print('result: ', result)
#
#         print('*results[0][0:1]: ', *results[0][0:1])
#
#         set_results = {result[0] for result in results}
#         list_results = [result[0] for result in results]
#
#         print('--------------set_results: ', set_results)
#         print('--------------list_results: ', list_results)
#
#
#         # results:  [('https://t.me/thebitcoinnews', <pycurl.Curl object at 0x7fe54c001a48>, 2, None),
#         ('https://t.me/coinstaker', <pycurl.Curl object at 0x7fe550001838>, 2, None), (
#         'https://t.me/coinstaker', <pycurl.Curl object at 0x7fe544002098>, 2, None)]
#         # result:  ('https://t.me/thebitcoinnews', <pycurl.Curl object at 0x7fe54c001a48>, 2, None)
#         # result:  ('https://t.me/coinstaker', <pycurl.Curl object at 0x7fe550001838>, 2, None)
#         # result:  ('https://t.me/coinstaker', <pycurl.Curl object at 0x7fe544002098>, 2, None)
#         # *results[0][0:1]:  https://t.me/thebitcoinnews
#         # --------------set_results:  {'https://t.me/coinstaker', 'https://t.me/thebitcoinnews'}
#         # --------------list_results:  ['https://t.me/thebitcoinnews', 'https://t.me/coinstaker',
#         'https://t.me/coinstaker']
#
#
#         Cada funcion devuelve una tupla y yo empaqueto todas las tuplas en lista
#         ('https://t.me/coinstaker', <pycurl.Curl object at 0x7fa57c001c68>, 2, None),
#         ('https://t.me/coinstaker', <pycurl.Curl object at 0x7fa580001868>, 2, None)
#     :param tasks:
#     :return: list of tuples
#     """
#     l = log()
#
#     l.i(msg='Start Tasks: {}'.format(tasks))
#
#     for task in tasks:
#         l.m(msg='Start Task: {}'.format(task))
#
#     tasks = await asyncio.gather(*tasks)
#
#     results = []
#     for task in tasks:
#         task.cancel()
#         results.append(task.result())
#         l.m(msg='End Task: {}'.format(task))
#
#     l.s(msg='End Tasks: results == {}'.format(results))
#     return results
# # endregion Functions
#
#
# # region Path
# def os_dir(file):
#     return os.path.dirname(file)
#
#
# def os_pack(file):
#     return os.path.split(os.path.dirname(file))[1]
#
#
# def os_mod(file):
#     return os.path.splitext(os.path.basename(file))[0]
#
#
# def os_pack_prefix(file):
#     return '{}/{}'.format(os_dir(file), os_pack(file))
#
#
# def os_dir_pack_mod(file):
#     return os_dir(file), os_pack(file), os_mod(file)
#
#
# package = os_pack(__file__)
# package_prefix = os_pack_prefix(__file__)
# # endregion Path
#
#
# # region Context
# def add_context(variables: str = None, msg: str = 'Context', ctx: bool = True, context_dict: dict = None) -> str:
#     """
#     Añade información de contexto a un mensaje de log o excepción
#
#     :type variables: str
#     :type msg: str
#     :type ctx: bool
#     :type context_dict: dict
#
#     :param variables: 'var1 var2 var3
#     :param msg: 'Error'
#     :param ctx: (True, excepciones, False, log para que no meta las locales si no pongo mensaje) incluye context
#     information: False para no
#     incluir nada solo msg,
#     se ignora si hay variables.
#     :param context_dict: Log calls with: inspect.currentframe().f_back.f_locals
#     :return: msg str
#
#     try:
#         a = 2/0
#     except:
#         add_context()
#         raise
#     """
#     if not context_dict:
#         context_dict = inspect.currentframe().f_back.f_locals
#
#     try:
#         context_dict = {**context_dict, **{var: value for var, value in asyncio.current_task().items()}}
#     except RuntimeError:
#         pass
#     except AttributeError:
#         pass
#
#     if variables:
#         msg = '{}: {}'.format(msg, ", ".join(
#             "{}={}".format(*item) for item in vars_to_dict(context_dict, variables).items()))
#     elif ctx:
#         msg = '{}: {}'.format(msg, ", ".join("{}={}".format(*item) for item in context_dict.items()))
#
#     exception = sys.exc_info()[1]
#     if exception:
#         exception.args = ('{} [{}]'.format(exception.args[0], msg) if exception.args else msg,) + exception.args[1:]
#
#     return msg
#
#
# def put(variables):
#     """
#     utils.put('a b c d e f g')
#
#     Pone las variables en el contexto con el valor que tengan en local
#
#     Ejemplo:
#         a = 1
#         b = [1, 2, 3 , 4]
#         c = (2, 3, 4)
#         d = {'a': 1}
#         e = config
#         f = Url
#         g = init1
#         utils.put('a b c d e f g')
#     """
#     for var in vars_to_dict(inspect.currentframe().f_back.f_locals, variables).items():
#         aiotask_context.set(*var)
#     for var in vars_to_dict(inspect.currentframe().f_back.f_globals, variables).items():
#         aiotask_context.set(*var)
#     if isinstance(variables, dict):
#         """
#         Meto el dict expandido y el dict entero
#         """
#         setv(**variables)
#
#
# def get():
#     """
#     http_proxy, privoxy_host_port, loop, log = utils.get()
#
#     print(http_proxy)
#     print(privoxy_host_port)
#     print(loop)
#     print(log)
#
#     Copia las variables del contexto
#
#     Ejemplo:
#         http_proxy = utils.get()
#         print(http_proxy)
#         print(b)
#         print(c)
#         print(d)
#         print(e)
#         print(f)
#         print(g)
#     """
#     values = tuple(aiotask_context.get(var) for var in caller_code()[0].replace(' ', '').split('=', 1)[0].rsplit(','))
#     if len(values) is 1:
#         return values[0]
#     else:
#         return values
#
#
# def setv(**kwvariables):
#     """
#     utils.setv(a=2, b=2)
#
#     Modifica las variables en el contexto con el valor que les paso
#     """
#     for var in kwvariables.items():
#         aiotask_context.set(*var)
# # endregion Context
#
#
# # region Inspect
# FRAME = 0
# FILE = 1
# LINE = 2
# NAME = 3
# CODE = 4
# INDEX = 5
# SELF = 0
# CALL = 1
# BACK = 2
#
#
# def caller_function():
#     return inspect.stack()[BACK][NAME]
#
#
# def caller_file():
#     return os.path.abspath(inspect.stack()[BACK][FILE])
#
#
# def caller_code():
#     return inspect.stack()[BACK][CODE]
#
#
# def function_args(frame):
#     fr = frame.f_back
#     args, _, _, values = inspect.getargvalues(fr)
#     return reverse_dict(values)
# # endregion Inspect

#
# # region Ini
# ini_file = '{}.ini'.format(package_prefix)
#
#
# def config_ini(conf=None):
#     is_file(ini_file)
#
#     if not conf:
#         conf = configparser.RawConfigParser()
#         conf.optionxform = str
#         conf.read(ini_file)
#         return conf
#     else:
#         with open(ini_file, "w+") as configfile:
#             conf.write(configfile)
#             configfile.close()
#             return
#
#
# ini = config_ini()
# # endregion Ini
#
#
# # region Log
# log_file = '{}.log'.format(package_prefix)
#
# logging_levels = {'set': 'NOTSET', 'm': 'SPAM', 'd': 'DEBUG', 'v': 'VERBOSE', 'i': 'INFO', 'n': 'NOTICE',
#                   'w': 'WARNING', 's': 'SUCCESS', 'e': 'ERROR', 'c': 'CRITICAL'}
#
# logging_values = {'set': logging.NOTSET, 'm': verboselogs.SPAM, 'd': logging.DEBUG, 'v': verboselogs.VERBOSE,
#                   'i': logging.INFO, 'n': verboselogs.NOTICE, 'w': logging.WARNING, 's': verboselogs.SUCCESS,
#                   'e': logging.ERROR, 'c': logging.CRITICAL}
#
#
# class MyFormatter(colorlog.ColoredFormatter):
#     log_colors = {logging_levels['m']: 'yellow', logging_levels['d']: 'blue', logging_levels['v']: 'white',
#                   logging_levels['i']: 'green', logging_levels['n']: 'cyan', logging_levels['w']: 'purple',
#                   logging_levels['s']: 'fg_bold_green,bg_yellow', logging_levels['e']: 'red',
#                   logging_levels['c']: 'fg_bold_red,bg_black'}
#
#     def __init__(self, fmt=None, datefmt=None, style='%', reset=True, secondary_log_colors=None):
#         super(MyFormatter, self).__init__(fmt, datefmt, style, self.log_colors, reset, secondary_log_colors)
#
#
# class Log(verboselogs.VerboseLogger):
#     def __init__(self, *args, **kwargs):
#         super(Log, self).__init__(*args, **kwargs)
#
#     def child(self, name=None, level=None):
#         caller = inspect.stack()[CALL][NAME]
#
#         if not name:
#             name = caller
#         l = self.getChild(name)
#
#         args = function_args(inspect.currentframe())
#         try:
#             line = inspect.stack()[BACK][LINE]
#         except IndexError:
#             line = inspect.stack()[CALL][LINE]
#
#         msg = '{}: Calling: {}()'.format(line, caller)
#         if args:
#             msg = "{}: Calling: {}( {} )".format(line, caller, args)
#
#         if self.isEnabledFor(verboselogs.SPAM):
#             self._log(verboselogs.SPAM, msg, None)
#
#         if level and level in logging_levels.keys():
#             l.setLevel(logging_levels[level])
#
#         msg = 'Entering: {}()'.format(caller)
#         if args:
#             msg = "Entering: {}( {} )".format(caller, args)
#         if l.isEnabledFor(verboselogs.SPAM):
#             l._log(verboselogs.SPAM, msg, None)
#
#         if level and level not in logging_levels.keys() and l.isEnabledFor(logging.WARNING):
#             effective = l.getEffectiveLevel()
#             for level, value in logging_levels.items():
#                 if value == effective:
#                     effective = level
#             l._log(logging.WARNING,
#                    "Not valid Logging level='{}' for child(). Effective level == '{}'".format(level, effective), None)
#
#         for pack in ini['other']:
#             logging.getLogger(pack).setLevel(logging_values[ini['other'][pack]])
#
#         return l
#
#     def m(self, variables=None, msg='Context', ctx=False):
#         if self.isEnabledFor(verboselogs.SPAM):
#             msg = add_context(variables, msg, ctx, context_dict=inspect.currentframe().f_back.f_locals)
#             self._log(verboselogs.SPAM, msg, None)
#
#     def d(self, variables=None, msg='Context', ctx=False):
#         if self.isEnabledFor(logging.DEBUG):
#             msg = add_context(variables, msg, ctx, context_dict=inspect.currentframe().f_back.f_locals)
#             self._log(logging.DEBUG, msg, None)
#
#     def v(self, variables=None, msg='Context', ctx=False):
#         if self.isEnabledFor(verboselogs.VERBOSE):
#             msg = add_context(variables, msg, ctx, context_dict=inspect.currentframe().f_back.f_locals)
#             self._log(verboselogs.VERBOSE, msg, None)
#
#     def i(self, variables=None, msg='Context', ctx=False):
#         if self.isEnabledFor(logging.INFO):
#             msg = add_context(variables, msg, ctx, context_dict=inspect.currentframe().f_back.f_locals)
#             self._log(logging.INFO, msg, None)
#
#     def n(self, variables=None, msg='Context', ctx=False):
#         if self.isEnabledFor(verboselogs.NOTICE):
#             msg = add_context(variables, msg, ctx, context_dict=inspect.currentframe().f_back.f_locals)
#             self._log(verboselogs.NOTICE, msg, None)
#
#     def w(self, variables=None, msg='Context', ctx=False):
#         if self.isEnabledFor(logging.WARNING):
#             msg = add_context(variables, msg, ctx, context_dict=inspect.currentframe().f_back.f_locals)
#             self._log(logging.WARNING, msg, None)
#
#     def s(self, variables=None, msg='Context', ctx=False):
#         if self.isEnabledFor(verboselogs.SUCCESS):
#             msg = add_context(variables, msg, ctx, context_dict=inspect.currentframe().f_back.f_locals)
#             self._log(verboselogs.SUCCESS, msg, None)
#
#     def e(self, variables=None, msg='Context', ctx=False):
#         if self.isEnabledFor(logging.ERROR):
#             msg = add_context(variables, msg, ctx, context_dict=inspect.currentframe().f_back.f_locals)
#             self._log(logging.ERROR, msg, None)
#
#     def c(self, variables=None, msg='Context', ctx=False):
#         if self.isEnabledFor(logging.CRITICAL):
#             msg = add_context(variables, msg, ctx, context_dict=inspect.currentframe().f_back.f_locals)
#             self._log(logging.CRITICAL, msg, None)
#
#     def x(self, variables=None, msg='Context', ctx=True, exc_info=True):
#         if self.isEnabledFor(logging_levels['e']):
#             msg = add_context(variables, msg, ctx, context_dict=inspect.currentframe().f_back.f_locals)
#             self._log(logging_levels['e'], msg, None, exc_info=exc_info)
#
#
# def config_log():
#     levels = {name: logging_levels[ini['common']['level']] if name in ini['common']['to'] else logging_levels[
#         ini['default'][name]] for name in ini['default']}
#     for name, level in levels.items():
#         ini.set(name, 'level', level)
#     config_ini(ini)
#
#     logging.config.fileConfig(ini_file, defaults={'file': log_file}, disable_existing_loggers=False)
#     logging.setLoggerClass(Log)
#
#     return logging.getLogger(package)
#
#
# log = config_log().child
# # endregion Log

# region DB
# db_file = '{}.db'.format(package_prefix)
#
#
# def config_db():
#     if ini['db']['db'] == 'sqlite':
#         is_file(db_file)
#         sqlite_dialect = os.getenv('sqlite_dialect', 'NULL')
#         engine_url = '{}{}'.format(sqlite_dialect, db_file)
#     elif ini['db']['db'] == 'mysql':
#         mysql_dialect = os.getenv('mysql_dialect', 'NULL')
#         mysql_host = os.getenv('mysql_host', 'NULL')
#         mysql_alt = int(os.getenv('mysql_alt', 'NULL'))
#         mysql_password = os.getenv('mysql_password', 'NULL')
#         engine_url = '{0}{1}:{2}@{3}:{4}/{1}'.format(mysql_dialect, package, mysql_password, mysql_host, mysql_alt)
#     else:
#         raise ValueError
#
#     return sqlalchemy.create_engine(engine_url, echo=ini.getboolean('db', 'echo'))
#
#
# engine = config_db()
#
#
# @as_declarative()
# class Base(AllFeaturesMixin):
#     @declared_attr
#     def __tablename__(self):
#         return self.__name__.lower()
#
#     _session_factory = sqlalchemy.orm.sessionmaker(engine, autocommit=ini.getboolean('db', 'autocommit'),
#                                                    autoflush=ini.getboolean('db', 'autoflush'))
#     _session = sqlalchemy.orm.scoped_session(_session_factory)
#     _exclude = ['_rows', '_session_factory', '_session', '_exclude']
#
#     __mapper_args__ = {'exclude_properties': _exclude}
#
#     __abstract__ = True
#
#     @staticmethod
#     def query_count(query):
#         count_q = query.statement.with_only_columns([sqlalchemy.func.count()]).order_by(None)
#         count = query.session.execute(count_q).scalar()
#         return count
#
#     @classmethod
#     def aioquery(cls):
#         """
#         await Url.query()
#
#         :return:
#         """
#         return aioify(getattr(cls, inspect.stack()[SELF][NAME].replace('aio', '')))()
#
#     @classmethod
#     def aioall(cls):
#         """
#         res = await Url.aioall() -> cls.query.all()
#
#         :return:
#         """
#         return aioify(getattr(cls, inspect.stack()[SELF][NAME].replace('aio', '')))()
#
#     @classmethod
#     def aiofirst(cls):
#         """
#         res = await Url.aiofirst() -> cls.query.first()
#
#         :return:
#         """
#         return aioify(getattr(cls, inspect.stack()[SELF][NAME].replace('aio', '')))()
#
#     @classmethod
#     def column_pk(cls):
#         """
#         :param cls = Class(Base)
#
#         Devuelve lista con el nombre de la columna que contiene la private_key(pk) de la tabla si hay 1
#
#         :return: pk column name of child_class table
#         """
#         pk = [column for column in cls().columns if getattr(cls, column).primary_key]
#         return pk
#
#     @classmethod
#     def column_fk(cls):
#         """
#          :param cls = Class(Base)
#
#          Devuelve lista con el nombre de la columna que contiene la foreign_key(fk) de la tabla del child si hay 1
#
#          :return: fk column name of child_class table
#          """
#         fk = [column for column in cls().columns if getattr(cls, column).foreign_keys]
#         return fk
#
#     @classmethod
#     def column_relation(cls):
#         """
#         :param cls = Class(Base)
#
#         Devuelve el nombre de la columna que referencia la relación al child(column_relation)
#         si hay 1 child(column_relation)
#
#         :return: column_relation
#         """
#         assert len(cls.relations) == 1, "len(cls.relations)=={} should be 1".format(cls.relations)
#         return cls.relations[0]
#
#     @classmethod
#     def child_class(cls, parent_column_relation):
#         """
#         :param cls = Class(Base)
#
#         :param parent_column_relation = cls.column_relation()
#
#         Devuelve la clase de la tabla del child
#
#         :return: child_class
#         """
#         return sqlalchemy_utils.get_type(getattr(cls, parent_column_relation))
#
#     @classmethod
#     def child_column_pk(cls):
#         """
#         :param cls = Class(Base)
#
#         Devuelve lista con el nombre de la columna que contiene la private_key(pk) de la tabla del child si hay 1
#
#         :return: pk column name of child_class table
#         """
#         child_pk = [child_column for child_column in cls().columns if getattr(cls, child_column).primary_key]
#         assert len(child_pk) == 1, "len(child_pk)=={} should be 1".format(len(child_pk))
#         return child_pk
#
#     @classmethod
#     def child_column_fk(cls):
#         """
#          :param cls = Class(Base)
#
#          Devuelve lista con el nombre de la columna que contiene la foreign_key(fk) de la tabla del child si hay 1
#
#          :return: fk column name of child_class table
#          """
#         child_fk = [child_column for child_column in cls().columns if getattr(cls, child_column).foreign_keys]
#         assert len(child_fk) == 1, "len(child_fk)=={} should be 1".format(len(child_fk))
#         return child_fk
#
#     @classmethod
#     def update(cls, **columns_kwargs):
#         """
#         Phone.update(number='+34718898818', hash=78)
#
#         number = {'number': '+34777789', 'id': 34}
#         Phone.update(**number)
#
#         1 row - (nombre_columna=valor)
#
#         :param columns_kwargs: Columnas de la nueva fila
#         :return:new model instance
#         """
#         cls.create(**columns_kwargs)
#         cls._session.remove()
#
#     @classmethod
#     def aioupdate(cls, **columns_kwargs):
#         """
#         await Phone.aioupdate(number='+34718898818', hash=78)
#
#         number = {'number': '+34777789', 'id': 34}
#         await Phone.aioupdate(**number)
#
#         1 row - (nombre_columna=valor)
#
#         1 row - (nombre_columna=valor)
#
#         :param columns_kwargs: Columnas de la nueva fila
#         :return:new model instance
#         """
#         return aioify(getattr(cls, inspect.stack()[SELF][NAME].replace('aio', '')))(**columns_kwargs)
#
#     @classmethod
#     def add_kw(cls, rows_kwargs):
#         """
#         Url.add_kw(rows_kwargs)
#
#         row = {'number': 137412, 'id': 34}
#         Phone.add_kw(row)
#
#         row_1 = {'number': 137412, 'id': 34}
#         row_2 = {'number': 217121}
#         rows = row_1, row_2
#         print(rows)
#         Phone.add_kw(rows)
#
#         row_3 = {'number': 11237412, 'id': 342}
#         row_4 = {'number': 21337121}
#         print([row_3, row_4])
#         Phone.add_kw([row_3, row_4])
#
#         row_5 = {'number': 1123741277, 'id': 34200}
#         row_6 = {'number': 2133712771}
#         print((row_5, row_6))
#         Phone.add_kw((row_5, row_6))
#
#         --------------- No con dict ---------------------
#         row_7 = {'number': 1123741277, 'id': 34200}
#         row_8 = {'number': 2133712771}
#         print({row_7, row_8})
#         Phone.add_kw({row_7, row_8})
#         --------------- No con dict ---------------------
#
#         n rows - (nombre_columna=valor) - Puedo saltarme columnas
#
#         :param rows_kwargs: {'number': 2}, {'number': 3}
#         :param cls = Class(Base)
#
#         Uso:
#             Class.add_kw(rows_kwargs)
#
#         Ejemplos:
#             Config.add_kw(rows_kwargs)
#             Url.add_kw(rows_kwargs)
#             Phone.add_kw(rows_kwargs)
#
#         :return:
#         """
#         if isinstance(rows_kwargs, dict):
#             cls.update(**rows_kwargs)
#         else:
#             for row_kwargs in rows_kwargs:
#                 cls.update(**row_kwargs)
#
#     @classmethod
#     def aioadd_kw(cls, rows_kwargs):
#         """
#         await Url.aioadd_kw(rows_kwargs)
#
#         row = {'number': 137412, 'id': 34}
#         await Phone.aioadd_kw(row)
#
#         row_1 = {'number': 137412, 'id': 34}
#         row_2 = {'number': 217121}
#         rows = row_1, row_2
#         print(rows)
#         await Phone.aioadd_kw(rows)
#
#         row_3 = {'number': 11237412, 'id': 342}
#         row_4 = {'number': 21337121}
#         print([row_3, row_4])
#         await Phone.aioadd_kw([row_3, row_4])
#
#         row_5 = {'number': 1123741277, 'id': 34200}
#         row_6 = {'number': 2133712771}
#         print((row_5, row_6))
#         await Phone.aioadd_kw((row_5, row_6))
#
#         --------------- No con dict ---------------------
#         row_7 = {'number': 1123741277, 'id': 34200}
#         row_8 = {'number': 2133712771}
#         print({row_7, row_8})
#         Phone.add_kw({row_7, row_8})
#         --------------- No con dict ---------------------
#
#         n rows - (nombre_columna=valor) - Puedo saltarme columnas
#
#         :param rows_kwargs: {'number': 2}, {'number': 3}
#         :param cls = Class(Base)
#
#         Uso:
#             await Class.aioadd_kw(rows)
#
#         Ejemplos:
#             await Config.aioadd_kw(rows)
#             await Url.aioadd_kw(rows)
#             await Phone.aioadd_kw(rows)
#
#         :return:
#         """
#         return aioify(getattr(cls, inspect.stack()[SELF][NAME].replace('aio', '')))(rows_kwargs)
#
#     @classmethod
#     def add(cls, rows):
#         """
#         Phone.add([('msd_1', 1, 1)])
#
#         row = 'msd_2', 2, 2
#         Phone.add([row])
#
#         Phone.add({('mkj_1', 11, 11)})
#
#         row = 'mkj_2', 22, 22
#         Phone.add({row})
#
#         row_1 = 'a', 2, 3
#         row_2 = 'b', 2, 8
#         rows = [row_1, row_2]
#         Phone.add(rows)
#
#         row_1 = 'g', 2, 3
#         row_2 = 'j', 2, 8
#         rows = row_1, row_2
#         Phone.add(rows)
#
#         row_8 = 'p', 2, 3
#         row_9 = 'q', 2, 8
#         Phone.add([row_8, row_9])
#
#         row_8 = 'ss', 2, 3
#         row_9 = 'qss', 2, 8
#         Phone.add((row_8, row_9))
#
#         _rows = ('+12056864923', 2, 'txt'), ('+14805267610', 2, 'txt')
#         _rows = ['+12056864923', 2, 'txt'], ['+14805267610', 2, 'txt']
#
#         --------------- ERROR -----------------------
#         row = 'm', 2, 3
#         Phone.add((row))
#         Phone.add(row)
#
#         row = ['i', 2, 3]
#         Phone.add(row)
#
#         row = ('x', 2, 3)
#         Phone.add(row)
#
#         row = {'z', 2, 3}
#         Phone.add(row)
#
#         _rows = {'+12056864923', 2, 'txt'}, {'+14805267610', 2, 'txt'}
#         --------------- ERROR ----------------------
#
#         n rows - (valor_1, valor_2) - No puedo saltarme columnas
#
#         await Url.add(**kwargs) # Igual que: 'update' para self
#
#         :param rows:
#         :return:
#         """
#         # table_columns = columnas - id_column - fk_column
#         table_columns = cls.columns
#
#         try:
#             table_columns.remove('key')
#         except ValueError:
#             pass
#
#         if cls.column_fk():
#             table_columns.remove(cls.column_fk()[0])
#
#         for row_columns in rows:
#             assert len(table_columns) == len(row_columns), "len(table_columns)=={} != len(row_columns)=={} in " \
#                                                            "row_columns=={}".format(len(table_columns),
#                                                                                     len(row_columns), row_columns)
#             row_kwargs = {table_columns[i]: row_columns[i] for i in (range(len(row_columns)))}
#             cls.add_kw(row_kwargs)
#
#     @classmethod
#     def aioadd(cls, rows):
#         """
#         await Phone.aioadd([('msd_1', 1, 1)])
#
#         row = 'msd_2', 2, 2
#         await Phone.aioadd([row])
#
#         await Phone.aioadd({('mkj_1', 11, 11)})
#
#         row = 'mkj_2', 22, 22
#         await Phone.aioadd({row})
#
#         row_1 = 'a', 2, 3
#         row_2 = 'b', 2, 8
#         rows = [row_1, row_2]
#         await Phone.aioadd(rows)
#
#         row_1 = 'g', 2, 3
#         row_2 = 'j', 2, 8
#         rows = row_1, row_2
#         await Phone.aioadd(rows)
#
#         row_8 = 'p', 2, 3
#         row_9 = 'q', 2, 8
#         await Phone.aioadd([row_8, row_9])
#
#         row_8 = 'ss', 2, 3
#         row_9 = 'qss', 2, 8
#         await Phone.aioadd((row_8, row_9))
#
#         n rows - (valor_1, valor_2) - No puedo saltarme columnas
#
#         :return:
#         :param rows: tuple
#         :return:
#         """
#         return aioify(getattr(cls, inspect.stack()[SELF][NAME].replace('aio', '')))(rows)
#
#     @classmethod
#     def _get(cls, pk):
#         """
#         res = Phone.get('pk'))
#
#         res = Url.get(pk) -> cls.query.get(pk)
#
#         :param pk:
#         :return: object row
#         """
#         return cls.find(pk)
#
#     @classmethod
#     def get(cls, pk):
#         """
#         res = Phone.get('pk'))
#
#         res = Url.get(pk) -> cls.query.get(pk)
#
#         :param pk:
#         :return: object row
#         """
#         res = cls._get(pk)
#         cls._session.remove()
#         return res
#
#     @classmethod
#     def aioget(cls, pk):
#         """
#         res = await Phone.aioget('pk'))
#
#         res = await Url.aioget(pk) -> cls.query.get(pk)
#
#         :param pk:
#         :return: object row
#         """
#         return aioify(getattr(cls, inspect.stack()[SELF][NAME].replace('aio', '')))(pk)
#
#     @classmethod
#     def delete(cls, *pks):
#         """
#         Phone.delete('j', 'p') -> for pk in pks: cls.query.get(pk).delete()
#
#         :param pks:
#         :return:
#         """
#         for pk in pks:
#             res = cls._get(pk)
#             res._session.delete(res)
#             res._session.flush()
#             cls._session.remove()
#
#     @classmethod
#     def aiodelete(cls, *pks):
#         """
#         await Phone.aiodelete('j', 'p') -> for pk in pks: cls.query.get(pk).delete()
#
#         :param pks:
#         :return:
#         """
#         return aioify(getattr(cls, inspect.stack()[SELF][NAME].replace('aio', '')))(*pks)
#
#     @classmethod
#     def count(cls, column=None, value=None):
#         """
#         Url.count()
#         print(Phone.count(column='id', value=None))
#
#         :param cls = Class(Base)
#         :param column:
#         :param value:
#         Uso:
#             Class.count()
#
#         Ejemplos:
#             Url.count()
#             print(Url.count())
#
#         :return: rows of cls
#         """
#         if column and value:
#             count = cls.query_count(cls.session().query(cls).filter(getattr(cls, column) == value))
#         else:
#             count = cls.query_count(cls.session().query(cls))
#         cls._session.remove()
#         return count
#
#     @classmethod
#     def aiocount(cls, column=None, value=None):
#         """
#         await Url.aiocount()
#         print(await Phone.aiocount(column='id', value=None))
#
#         :return:
#         """
#         return aioify(getattr(cls, inspect.stack()[SELF][NAME].replace('aio', '')))(column, value)
#
#     @classmethod
#     def child_update(cls, parent_key, **child_columns_kwargs):
#         """
#         Url.child_update(https://www.trackico.io, url="https://t.me/prueba")
#
#         :param cls = Class(Base)
#         :param parent_key: pk al que añadir los hijos
#         :param child_columns_kwargs:
#
#         1 row: columnas con kwargs
#
#         Uso:
#             Class.child_update(parent_key, child_columns_kwargs)
#
#         Ejemplos:
#             parent = 'https://www.trackico.io'
#             child = {'url': 'https:t.me/icorating'}
#             Url.child_update(parent, **child)
#             Url.child_update(parent, url='mierda')
#
#         :return:
#         """
#         parent_column_relation = cls.column_relation()
#         child_cls = cls.child_class(parent_column_relation)
#
#         parent_obj = cls.find_or_fail(parent_key)
#         parent_obj_column_relation = getattr(parent_obj, parent_column_relation)
#         parent_obj_column_relation.append(child_cls(**child_columns_kwargs))
#
#         cls.session.add(parent_obj)
#         cls.session.flush()
#         cls._session.remove()
#
#     @classmethod
#     def aiochild_update(cls, parent_key, **child_columns_kwargs):
#         """
#         await Url.aiochild_update(https://www.trackico.io, url="https://t.me/prueba")
#
#         :param cls = Class(Base)
#         :param parent_key: pk al que añadir los hijos
#         :param child_columns_kwargs:
#
#         1 row: columnas con kwargs
#
#         Uso:
#             await Url.aiochild_update(parent_key, child_columns_kwargs)
#
#         Ejemplos:
#             parent = 'https://www.trackico.io'
#             child = {'url': 'https:t.me/icorating'}
#             await Url.aiochild_update(parent, **child)
#             await Url.aiochild_update(parent, url='mierda')
#
#         :return:
#         """
#         return aioify(getattr(cls, inspect.stack()[SELF][NAME].replace('aio', '')))(parent_key, **child_columns_kwargs)
#
#     @classmethod
#     def child_add_kw(cls, parent_key, child_rows_kwargs):
#         """
#         child_1 = {'url': 'https:t.me/icorating_1'}
#         child_2 = {'url': 'https:t.me/icorating_2'}
#         Url.child_add_kw(https://www.trackico.io, [child_1, child_2])
#
#         :param cls = Class(Base)
#         :param parent_key: pk al que añadir los hijos
#         :param child_rows_kwargs: Valores en kwargs para las rows a añadir
#
#         Uso:
#             Class.child_add_kw(parent_key, [child__1, child__2])
#
#         Ejemplos:
#             parent = 'https://www.trackico.io'
#             child_1 = {'url': 'https:t.me/icorating_1'}
#             child_2 = {'url': 'https:t.me/icorating_2'}
#             childs = child_1, child_2
#             Url.child_add_kw(parent, [child_1, child_2])
#             Url.child_add_kw(parent, childs)
#
#         :return:
#         """
#         if isinstance(child_rows_kwargs, dict):
#             cls.child_update(parent_key, **child_rows_kwargs)
#         else:
#             for child_row_kwargs in child_rows_kwargs:
#                 cls.child_update(parent_key, **child_row_kwargs)
#
#     @classmethod
#     def aiochild_add_kw(cls, parent_key, child_rows_kwargs):
#         """
#         child_1 = {'url': 'https:t.me/icorating_1'}
#         child_2 = {'url': 'https:t.me/icorating_2'}
#         await Url.aiochild_add_kw(https://www.trackico.io, [child_1, child_2])
#
#         :param cls = Class(Base)
#         :param parent_key: pk al que añadir los hijos
#         :param child_rows_kwargs: Valores en kwargs para las rows a añadir
#
#         Uso:
#             Class.child_add_kw(parent_key, [child__1, child__2])
#
#         Ejemplos:
#             parent = 'https://www.trackico.io'
#             child_1 = {'url': 'https:t.me/icorating_3'}
#             child_2 = {'url': 'https:t.me/icorating_4'}
#             childs = child_1, child_2
#             await Url.aiochild_add_kw(parent, [child_1, child_2])
#             await Url.aiochild_add_kw(parent, childs)
#
#         :return:
#         """
#         return aioify(getattr(cls, inspect.stack()[SELF][NAME].replace('aio', '')))(parent_key, child_rows_kwargs)
#
#     @classmethod
#     def child_add(cls, parent_key, child_rows):
#         """
#         Url.child_add(https://www.trackico.io, [('https:t.me/icorating_8',)])
#
#         child_1 = 'https:t.me/icorating_1'
#         child_2 = 'https:t.me/icorating_2'
#         Url.child_add(https://www.trackico.io, [child_1, child_2])
#
#
#         1.- Obtiene las columnas del child que no son ni pk, ni fk
#         2.- Comprueba que el número de columnas a rellenar del punto 1 es igual al número de child_values pasado en
#             llamada
#         3.- Añade a la tabla Child del Parent, con child_column obtenido de 1 = valor de child_values
#
#         :param cls = Class(Base)
#         :param parent_key: pk al que añadir los hijos
#         :param child_rows: Valores para Todas las columnas y todas las filas, del child(relationship) que no son
#         primary_key ni foreign_keys
#
#         Uso:
#             Class.child_add(parent_key, [child__1, child__2])
#
#         Ejemplos:
#             await Url.aiochild_add('https://www.trackico.io', [('https:t.me/icorating_A',)])
#
#             child_1 = ['https:t.me/icorating_1']
#             child_2 = ['https:t.me/icorating_2']
#             Url.child_add('https://www.trackico.io', [child_1, child_2])
#
#             child_1 = 'https:t.me/icorating_1',
#             child_2 = 'https:t.me/icorating_2',
#             Url.child_add('https://www.trackico.io', [child_1, child_2])
#
#             parent = 'https://www.trackico.io'
#
#             childs = child_1, child_2
#             Url.child_add(parent, childs)
#
#         :return:
#         """
#         parent_column_relation = cls.column_relation()
#         child_cls = cls.child_class(parent_column_relation)
#
#         child_columns = [child_column for child_column in child_cls().columns if
#                          child_column not in child_cls.child_column_pk() and
#                          child_column not in child_cls.child_column_fk()]
#
#         for child_row_columns in child_rows:
#             assert len(child_columns) == len(
#                 child_row_columns), "len(child_columns)=={} != len(child_values)=={}".format(len(child_columns),
#                                                                                              len(child_row_columns))
#             child_kwargs = {child_columns[i]: child_row_columns[i] for i in (range(len(child_columns)))}
#             cls.child_add_kw(parent_key, child_kwargs)
#
#     @classmethod
#     def aiochild_add(cls, parent_key, child_rows):
#         """
#         await Url.aiochild_add(https://www.trackico.io, [('https:t.me/icorating_8',)])
#
#         child_1 = 'https:t.me/icorating_1'
#         child_2 = 'https:t.me/icorating_2'
#         await Url.aiochild_add(https://www.trackico.io, [child_1, child_2])
#
#
#         1.- Obtiene las columnas del child que no son ni pk, ni fk
#         2.- Comprueba que el número de columnas a rellenar del punto 1 es igual al número de child_values pasado en
#             llamada
#         3.- Añade a la tabla Child del Parent, con child_column obtenido de 1 = valor de child_values
#
#         :param cls = Class(Base)
#         :param parent_key: pk al que añadir los hijos
#         :param child_rows: Valores para Todas las columnas y todas las filas, del child(relationship) que no son
#         primary_key ni foreign_keys
#
#         Uso:
#             await Class.aiochild_add(parent_key, [child__1, child__2])
#
#         Ejemplos:
#             Url.child_add('https://www.trackico.io', [('https:t.me/icorating_A',)])
#
#             child_1 = ['https:t.me/icorating_1']
#             child_2 = ['https:t.me/icorating_2']
#             await Url.aiochild_add('https://www.trackico.io', [child_1, child_2])
#
#             child_1 = 'https:t.me/icorating_1',
#             child_2 = 'https:t.me/icorating_2',
#             await Url.aiochild_add('https://www.trackico.io', [child_1, child_2])
#
#             parent = 'https://www.trackico.io'
#
#             childs = child_1, child_2
#             await Url.aiochild_add(parent, childs)
#
#         :return:
#         """
#         return aioify(getattr(cls, inspect.stack()[SELF][NAME].replace('aio', '')))(parent_key, child_rows)
#
#     @classmethod
#     def _child_get(cls, parent_key):
#         parent_column_relation = cls.column_relation()
#         child_cls = cls.child_class(parent_column_relation)
#         child_fk = child_cls.child_column_fk()
#         return child_cls.session().query(child_cls).filter(getattr(child_cls, child_fk[0]) == parent_key)
#
#     @classmethod
#     def child_get(cls, parent_key):
#         """
#         Url.child_get(parent)
#
#         :param cls = Class(Base)
#         :param parent_key: pk al que obtener los hijos
#
#         Uso:
#             Class.child_get(parent_key)
#
#         Ejemplos:
#             parent = 'https://www.trackico.io'
#             Url.child_get(parent)
#             print(Url.child_get(parent))
#
#         :return: lista con los child asociados al parent pk
#         """
#         child_rows = cls._child_get(parent_key).all()
#         cls._session.remove()
#         return child_rows
#
#     @classmethod
#     def aiochild_get(cls, parent_key):
#         """
#         await Url.aiochild_get(parent)
#
#         parent = 'https://www.trackico.io'
#         print(await Url.aiochild_get(parent))
#
#         :param parent_key:
#         :return:
#         """
#         return aioify(getattr(cls, inspect.stack()[SELF][NAME].replace('aio', '')))(parent_key)
#
#     @classmethod
#     def child_delete(cls, parent_key):
#         """
#         Url.child_delete(parent)
#
#         :param cls = Class(Base)
#         :param parent_key: pk al que borrar los hijos
#
#         Uso:
#             Class.child_del(parent_key)
#
#         Ejemplos:
#             parent = 'https://www.trackico.io'
#             Url.child_delete(parent)
#
#         :return:
#         """
#         cls._child_get(parent_key).delete(synchronize_session=False)
#         cls._session.remove()
#
#     @classmethod
#     def aiochild_delete(cls, parent_key):
#         """
#         await Url.aiochild_delete(parent)
#
#         :param parent_key:
#         :return:
#         """
#         return aioify(getattr(cls, inspect.stack()[SELF][NAME].replace('aio', '')))(parent_key)
#
#     @classmethod
#     def child_count(cls, parent_key, column=None, value=None):
#         """
#         Url.child_count(parent)
#
#         Url.child_count(parent, column='url', value='https:t.me/icorating_2')
#
#         :param cls = Class(Base)
#         :param parent_key: pk al que contar sus hijos
#         :param column: nombre de la columna adicional del hijo a preguntar
#         :param value: valor de la columna adicional del hijo a preguntar
#
#         Uso:
#             Class.child_count(parent_key)
#
#         Ejemplos:
#             parent = 'https://www.trackico.io'
#             Url.child_count(parent)
#             print(Url.child_count(parent, column='url', value='https:t.me/icorating_2'))
#         :return: rows de los hijos asociados al parent pk
#         """
#         parent_column_relation = cls.column_relation()
#         child_cls = cls.child_class(parent_column_relation)
#         if column and value:
#             count = cls.query_count(cls._child_get(parent_key).filter(getattr(child_cls, column) == value))
#         else:
#             count = cls.query_count(cls._child_get(parent_key))
#         cls._session.remove()
#
#         return count
#
#     @classmethod
#     def aiochild_count(cls, parent_key, column=None, value=None):
#         """
#         await Url.aiochild_count(parent)
#         await Url.aiochild_count(parent, column='url', value='https:t.me/icorating_2')
#
#         print(await Url.aiochild_count(parent, column='url', value='https:t.me/icorating_2'))
#
#         :param parent_key: pk al que contar sus hijos
#         :param column: nombre de la columna adicional del hijo a preguntar
#         :param value: valor de la columna adicional del hijo a preguntar
#
#         :return:
#         """
#         return aioify(getattr(cls, inspect.stack()[SELF][NAME].replace('aio', '')))(parent_key, column, value)
#
#     @classmethod
#     def init(cls):
#         """
#         Url.init()
#
#         n rows - (nombre_columna=valor) - Puedo saltarme columnas
#
#         if tabla vacia añade filas de _rows y si no hay _rows añade por defecto.
#             if _rows
#                 if _rows is *columns_args
#                     cls.add(*columns_args)
#                 else:
#                      cls.add_kw(*columns_kwargs)
#             else
#                 cls.update()  # Por defecto
#
#         :param cls = Class(Base)
#
#         Uso:
#             Class.init()
#
#         Ejemplos:
#             Config.init()
#             Url.init()
#             Phone.init()
#
#         :return:
#         """
#         if not cls.query.first():
#             try:
#                 rows = cls._rows  # for row in cls._rows:  #     cls.update(**row)
#             except AttributeError:
#                 pass
#             else:
#                 if isinstance(rows, list):
#                     cls.add_kw(rows)
#                 elif isinstance(rows, tuple):
#                     cls.add(rows)
#             finally:
#                 cls._session.remove()
#
#     @classmethod
#     def aioinit(cls):
#         """
#         await Url.aioinit()
#
#         :return:
#         """
#         return aioify(getattr(cls, inspect.stack()[SELF][NAME].replace('aio', '')))()
#
#
# import __init__
# endregion DB


class Enum(enum.Enum):
    @classmethod
    def names(cls):
        return [name for name in cls.__members__.keys()]

    @classmethod
    def keys(cls):
        return [getattr(cls, name) for name in cls.names()]

    @classmethod
    def members(cls):
        return [member for name, member in cls.__members__.items()]

    @classmethod
    def items(cls):
        return {name: member for name, member in cls.__members__.items()}

    @classmethod
    def get(cls, name):
        return getattr(cls, name)


class Sem:
    names = ['default', 'aiohttp', 'browser', 'crawl', 'curl']
    maxs = {name: getattr(__init__.config, 'sem_{}'.format(name)) for name in names}
    sems = {name: asyncio.Semaphore(max) for name, max in maxs.items()}
    lows = {name: getattr(__init__.config, 'sem_{}_sleep'.format(name)) for name in names}
    highs = {name: int(low * __init__.config.time_factor) for name, low in lows.items()}

    def __init__(self, name: str = names[0]):
        self.name = name
        self.max = self.maxs[self.name]
        self.sem = self.sems[self.name]
        self.low = self.lows[self.name]
        self.high = self.highs[self.name]
        self.tasks = set()

    async def run(self, func, *args, **kwargs):
        l = log()

        await self.sem.acquire()
        l.d(msg='Semaphore: {}({}) - {}({})'.
            format(self.name, self.max, 'acquire', self.sem._value))

        sleep = random.randint(self.low, self.high)
        l.m(msg='Start task - Sleep started({}): {}( {}, {} )'.format(sleep, func.__qualname__, args, kwargs))
        await asyncio.sleep(sleep)
        l.m(msg='Start task - Sleep end({}): {}( {}, {} )'.format(sleep, func.__qualname__, args, kwargs))

        task = asyncio.create_task(func(*args, **kwargs))
        self.tasks.add(task)
        l.i(msg='Start task: {}( {}, {} )'.format(func.__qualname__, args, kwargs))

        await task
        self.tasks.remove(task)
        l.s(msg='End task: {} = {}( {}, {} )'.format(task.result(), func.__qualname__, args, kwargs))

        self.sem.release()
        l.d(msg='Semaphore: {}({}) - {}({})'.
            format(self.name, self.max, 'release', self.sem._value))
        return task


class Response:
    def __init__(self, client, response, obj, code):
        """

        :param client:
            client = pycurl.Curl()
            client = aiohttp.ClientSession(headers=self.headers, trust_env=True)
            client = webdriver.Firefox(desired_capabilities=self.capabilities)
        :param response:
                net.perform()

            response = io.BytesIO()
            response = client.get(url)
            response =
         source
            source = io.BytesIO().getvalue().decode()
            source = response.read().decode('utf-8', 'replace')
            source = client.page_source
        :param obj:
            obj =
            obj =
            obj =
        :param code:
            status =
            status = response.status
            status =
        headers
            headers =
            headers = response.headers.get()
            headers =
        """
        self.client = client
        self.response = response
        self.source = obj
        self.code = code


class Browser:
    def __init__(self):
        self.proxy = Proxy()
        self.proxy.proxy_type = ProxyType.MANUAL
        self.proxy.http_proxy = os.getenv('privoxy_host_port', 'NULL')
        self.capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.proxy.add_to_capabilities(self.capabilities)
        self.browser_load_sleep = 3
        self.browser = None
        self.browser = webdriver.Firefox(desired_capabilities=self.capabilities)
        self.browser.implicitly_wait(30)


class Net:
    clients = ['aiohttp', 'browser', 'curl']
    retry_enabled = __init__.config.retry_enabled
    retry_delay = __init__.config.retry_delay
    retry_times = __init__.config.retry_times
    retry_codes = [400, 403, 404, 408, 500, 502, 503, 504]
    retry_count = 0

    @staticmethod
    def _retry(func, url):
        for count in range(Net.retry_times):
            response, net, code = func(url)
            if code is 200:
                return response
            time.sleep(Net.retry_delay)

    @staticmethod
    @contextlib.asynccontextmanager
    async def _aioretry(func, url):
        for count in range(Net.retry_times):
            # response = Response(*func(url))
            response = func(url)
            if response.code is 200:
                try:
                    yield response
                finally:
                    response.close()
            await asyncio.sleep(Net.retry_delay)

    @staticmethod
    def _curl(url):
        response = io.BytesIO()
        net = pycurl.Curl()
        net.setopt(net.URL, url)
        net.setopt(net.FOLLOWLOCATION, 1)
        net.setopt(net.WRITEFUNCTION, response.write)
        net.setopt(net.PROXY, http_proxy)
        net.perform()

        return response.getvalue().decode(), net, net.getinfo(net.HTTP_CODE)

    @staticmethod
    def curl(url, retry=retry_enabled):
        if retry is True:
            return Net._retry(Net._curl, url)
        else:
            return Net._curl(url)

    @staticmethod
    async def aiocurl(url, retry=retry_enabled):
        return aioify(getattr(Net, inspect.stack()[SELF][NAME].replace('aio', '')))(url, retry)

    @staticmethod
    @contextlib.asynccontextmanager
    async def _aiohttp(url):
        headers = {"Referer": "https://www.google.com/search?",
                   "Accept": "text/html,application/xhtml+xml, application/xml;q=0.9,*/*;q=0.8",
                   "Accept_Language": "en", "DNT": "0", "Content-Language": "en-US",
                   "Content-Type": "text/html; charset=utf-8",
                   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) "
                   "AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10"}

        async with aiohttp.ClientSession(headers=headers, trust_env=True) as client:
            try:
                async with client.get(url) as response:
                    try:
                        yield response
                    finally:
                        response.close()
            finally:
                await client.close()

    @staticmethod
    @contextlib.asynccontextmanager
    async def aiohttp(url, retry=retry_enabled):
        if retry:
            async with Net._aioretry(Net._aiohttp, url) as response:
                try:
                    yield response
                finally:
                    response.close()
        else:
            async with Net._aiohttp(url) as response:
                try:
                    yield response
                finally:
                    response.close()

    @staticmethod
    def get(url, retry=retry_enabled, client=clients[0]):
        if client is Net.clients[0]:
            raise AttributeError('client == {} - must use == Net.aioget'.format(client))
        elif client is Net.clients[1]:
            pass
        elif client is Net.clients[2]:
            return Net.curl(url, retry)
        else:
            raise AttributeError('client == {} - clients == {}'.format(client, Net.clients))

    @staticmethod
    @contextlib.asynccontextmanager
    async def aioget(url, retry=retry_enabled, client=clients[0]):
        if client is Net.clients[0]:
            async with Net.aiohttp(url, retry) as response:
                try:
                    yield response
                finally:
                    response.close()
        elif client is Net.clients[1]:
            pass
        elif client is Net.clients[2]:
            # return Net.curl(url, retry)
            pass
        else:
            raise AttributeError('client == {} - clients == {}'.format(client, Net.clients))

    @staticmethod
    def ip():
        l = log()
        response, net, code = Net.get(__init__.config.ip_url, retry=False, client=Net.clients[2])
        try:
            socket.inet_aton(response)
            l.m(msg='IP: {}'.format(response))
            return response
        except socket.error:
            l.e(msg='IP: Error from {}'.format(__init__.config.ip_url))
            return None

    @staticmethod
    async def aioip():
        return aioify(getattr(Net, inspect.stack()[SELF][NAME].replace('aio', '')))()

    @staticmethod
    def eurl(url, retry=retry_enabled):
        l = log()
        response, net, code = Net.get(url, retry, client=Net.clients[2])

        effective_url = net.getinfo(net.EFFECTIVE_URL)
        if effective_url is None:
            effective_url = url
        l.m(msg='effective_url: {}'.format(effective_url))
        return effective_url

    @staticmethod
    async def aioeurl(url, retry=retry_enabled):
        return aioify(getattr(Net, inspect.stack()[SELF][NAME].replace('aio', '')))(url, retry)


class Crawl(Sem):
    def __init__(self, row):
        super().__init__(name=Sem.names[3])
        self.url = row.url
        self.click = row.click
        self.times_max = row.times_max
        self.times_real = row.times_real

        self.semaphore = asyncio.Semaphore(8)

        self.todo = set()
        self.busy = set()
        self.done = {}
        self.extracted = {}
        self.tasks = set()
        self.megagroups = None
        self.error = 0

        self.patterns = ['http://t.me/', 'https://t.me/', 'http://www.t.me/', 'https://www.t.me/',
                         'http://telegram.me/', 'https://telegram.me/', 'http://www.telegram.me/',
                         'https://www.telegram.me/']


class Thread:
    factory = {'mix': aiotask_context.chainmap_context_factory, 'not': aiotask_context.copying_task_factory,
               'all': aiotask_context.task_factory}

    def __init__(self, func, *args, **kwargs):
        print('__init__')

        self.loop = asyncio.new_event_loop()
        self.thread = threading.Thread(target=self.run, args=())
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.thread.name = self.func.__qualname__
        self.thread.daemon = True
        self.event = threading.Event()
        self.thread.start()
        # self.thread = threading.Thread(target=target, args=args, kwargs=kwargs)

    def run(self):
        asyncio.set_event_loop(self.loop)
        self.loop.set_task_factory(self.factory['all'])
        try:
            self.loop.run_until_complete(self.set())
        finally:
            print('finally')

            self.event.set()
            self.loop.stop()
            self.loop.close()

    async def set(self):
        put(' '.join(str(global_var) for global_var in globals() if global_var[:1] != '_'))
        put(' '.join(str(local_var) for local_var in locals() if local_var[:1] != '_'))
        aiotask_context.set('event_{}'.format(self.func.__qualname__), self.event)
        await self.func(*self.args, **self.kwargs)


async def aiorotate():
    print('aiorotate')

    event = aiotask_context.get('event_{}'.format(inspect.stack()[SELF][NAME]))
    low = __init__.config.rotate_time
    high = int(low * __init__.config.time_factor)
    while not event.is_set():
        print('loop')
        time.sleep(random.randint(low, high))
        await aioip()


def start(func, *args, **kwargs):
    """
    utils.start(init, a, hola=hola)

    Ejemplo:
        async def init(var1, hola='a'):
            print(var1)
            print(hola)
            context.set('a', 1)
        if __name__ == '__main__':
            a = 1
            hola = 'ala'
            utils.start(init, a, hola=hola)
    :param func:
    :param args:
    :param kwargs:
    :return:
    """
    def rotate():
        low = __init__.config.rotate_time
        high = int(low * __init__.config.time_factor)
        while not rotate_stop.is_set():
            time.sleep(random.randint(low, high))
            ip()

    async def aiorun(loop):
        put(' '.join(str(global_var) for global_var in globals() if global_var[:1] != '_'))
        put(' '.join(str(local_var) for local_var in locals() if local_var[:1] != '_'))
        await func(*args, **kwargs)

    l = log()

    rotate_stop = threading.Event()
    if __init__.config.rotate_enabled:
        # r = threading.Thread(target=rotate, args=(rotate_stop,))

        r = threading.Thread(target=rotate)
        r.start()
        l.s(msg='SUCCESSFUL: IP Rotate - Start')

    try:
        if inspect.iscoroutinefunction(func):
            """
            Permite que haya variables que pasan en contexto sin que vayan en llamadas.

            context.task_factory
            context.set("simple", "from child") # Modifica PARENT
            context.get("complex")[1] = "child" # Modifica PARENT

            context.copying_task_factory
            context.set("simple", "from child") # No Modifica PARENT
            context.get("complex")[1] = "child" # No Modifica PARENT

            context.chainmap_task_factory
            context.set("simple", "from child") # No Modifica PARENT
            context.get("complex")[1] = "child" # Modifica PARENT
            """
            lo = asyncio.get_event_loop()

            factory = {'mix': aiotask_context.chainmap_context_factory, 'not': aiotask_context.copying_task_factory,
                       'all': aiotask_context.task_factory}
            lo.set_task_factory(factory['all'])
            lo.run_until_complete(aiorun(lo))
        else:
            func(*args, **kwargs)
    except ValueError as exception:
        if "No event loop found, key a couldn't be set" in repr(exception):
            add_context()
        raise
    finally:
        if __init__.config.rotate_enabled:
            rotate_stop.set()
            l.i(msg='SUCCESSFUL: IP Rotate - Stop')


if __name__ == '__main__':
    rotatethread = Thread(aiorotate)
    time.sleep(40)

    print('Bye')
    # __all__ = [n for n in globals() if n[:1] != '_']
