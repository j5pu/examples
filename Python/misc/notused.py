def log_exc(logger):
    from functools import wraps

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # logger = getattr(__import__('module', fromlist=['logger']), 'logger')
            values = func_args(*args, **kwargs)
            log = logger.Child()
            kwargs["log"] = log
            log.debug('Entering: {}({}):'.format(f.__qualname__, values))
            return f(*args, **kwargs)
        return wrapper
    return decorator


class ExecCmd:
    def __init__(self, cmd, command):
        self.cmd = cmd
        self.command = command

    async def __aenter__(self):
        import asyncio

        proc = await asyncio.create_subprocess_shell(self.command,
                                                     stdout=asyncio.subprocess.PIPE,
                                                     stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await proc.communicate()
        self.stdout = stdout.decode()
        self.stderr = stderr.decode()
        # proc.returncode despues de que haya terminado el comando de ejecutar
        self.returncode = proc.returncode
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass


def func_args(*args, **kwargs):
    values = ''
    add = ''
    for value in args:
        values += '{}{!r}'.format(add, value)
        add = ', '
    for key, value in kwargs.items():
        values += '{}{!r}={!r}'.format(add, key, value)
        add = ', '
    return values


def func_name_args(f):
    from functools import wraps
    from inspect import signature

    @wraps(f)
    def wrapper(*args, **kwargs):
        args = signature(f).bind(*args, **kwargs).arguments
        func_args_str = ', '.join('{} = {!r}'.format(*item) for item in f.items())
        print('Function {} -  Parameters ({}):'.format(f.__qualname__, func_args_str))
        return f(*args, **kwargs)
    return wrapper


async def commands():
    command = {'ip': 'curl ipecho.net/plain',
               'tor': 'service tor status',
               'privoxy': 'service privoxy status',
               'tor_port': 'sudo lsof -i :tor',
               'tor_control_port': 'sudo lsof -i :tor-control',
               'privoxy_port': 'sudo lsof -i :privoxy',
               }
    ip = ''
    for cmd in command.keys():
        async with ExecCmd(cmd, command[cmd]) as ret_cmd:
            assert ret_cmd.returncode == 0, \
                "Error executing: {0}\nAssertionError: Error code: {1}\nAssertionError: Error message: {2}". \
                format(ret_cmd.command, ret_cmd.returncode, ret_cmd.stderr)
            if 'ip' in ret_cmd.cmd:
                ip = ret_cmd.stdout

    return ip


class Frame:
    def __init__(self, frame):
        from anytree import Node
        from inspect import stack

        from utils import module, BACK, FILE
        self.exclude_vars = ('__globals__', '__name__', '__qualname__', '__annotations__', '__call__',
                             '__get__', '__init__', '__spec__', '__main__', '__doc__', '__package__',
                             '__loader__', '__file__', '__builtins__', '__len__', '__closure__', '__code__',
                             '__dict__', '__globals__', '__defaults__', '__self__', '__func__',
                             '__kwdefaults__', '__qualname__', '__objclass__', '__add__', '__class__', '__contains__',
                             '__delattr__', '__dir__', '__all__', '__eq__', '__format__', '__ge__',
                             '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
                             '__init_subclass__', '__iter__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__',
                             '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
                             '__setattr__', '__sizeof__', '__subclasshook__', '_Feature', '__instancecheck__',
                             '__prepare__', '__subclasscheck__', '__subclasses__', '__abstractmethods__', '__bases__',
                             '__base__', '__basicsize__', '__dictoffset__', '__flags__', '__itemsize__', '__mro__',
                             '__text_signature__', '__weakrefoffset__', '__next__', '__loader__',
                             '__weakref__', '__isabstractmethod__', '__func__', '__ixor__', '__ior__', '__iand__',
                             '__contains__', '__reversed__', '__module__',
                             '__import__', '__build_class__', '__cached__')
        self.exclude_cls = ('module', 'type', 'function', 'builtin_function_or_method', 'method', 'FunctionType',
                            'LambdaType', 'CodeType', 'MappingProxyType', 'built-in method', 'method-wrapper',
                            'OSError', 'Warning', '__thisclass__', 'super', 'IOError',
                            '__function', '__asyncgenerator', '__generator', '__method', '__coroutine',
                            'classmethod')
        self.include_cls = ('dict', 'list', 'set', 'str', 'int', 'tuple', 'bool', 'float', 'long', 'float', 'complex',
                            'set', 'frozenset', 'bytes', 'bytearray', 'enumerate', '__namedtuple', 'filter', 'map',
                            'memoryview', 'property', 'zip')
        self.frame = frame
        name = self.frame.f_back.f_code.co_name
        if name == '<module>':
            name = module(stack()[BACK][FILE])
        self.root = Node('{}:{}'.format(name, self.frame.f_back.f_lineno))
        self.globals = Node('globals', parent=self.root)
        self.locals = Node('locals', parent=self.root)
        self.tree()

    def tree(self):
        import types
        import abc
        from anytree import Node, RenderTree
        from inspect import isgeneratorfunction, isawaitable, isabstract, iscoroutinefunction, isasyncgenfunction



        def isnot(k, v, private=True):
            if not private and k[0] == '_':
                return None
            if isinstance(k, type) or isinstance(k, types.MethodType) or isinstance(k,
                                                                                    types.MemberDescriptorType) or isinstance(
                k, types.GetSetDescriptorType) or isinstance(k, types.FunctionType) or isinstance(k,
                                                                                                  types.AsyncGeneratorType) or isinstance(
                k, types.CoroutineType) or isinstance(k, types.GeneratorType) or isinstance(k,
                                                                                            types.TracebackType) or isinstance(
                k, types.TracebackType) or isinstance(k, types.FrameType) or isinstance(k, types.CodeType) or callable(
                k) or isinstance(k, abc.ABCMeta) or isinstance(k, types.BuiltinFunctionType) or isgeneratorfunction(
                k) or iscoroutinefunction(k) or isasyncgenfunction(k) or isawaitable(k) or isabstract(k):
                return None
            if k in self.exclude_vars:
                return None
            if v.__class__.__name__ == 'type':
                return None
            if v.__class__.__name__ in self.exclude_cls:
                return None
            if v.__class__.__name__ not in self.include_cls:
                return True
            return False
        def obj(d, p):
            for k in d.__dict__.keys():

                v = getattr(d, k)
                print('{}: {}'.format(k, v))

                o = isnot(k, v)
                if o is None:
                    continue
                print('k:', v)
                yield k, v, p
                if o:
                    for ok, ov, op in obj(k, k):
                        yield ok, ov, op

        def scan(d, p):
            for k, v in d.items():
                o = isnot(k, v)
                if o is None:
                    continue
                yield k, v, p
                if o:
                    for ok, ov, op in obj(k, k):
                        yield ok, ov, op

        for key, value, parent in scan(self.frame.f_back.f_globals, 'globals'):
            setattr(self, key, Node(key, parent=getattr(self, parent), kwargs=value))
        for key, value, parent in scan(self.frame.f_back.f_locals, 'locals'):
            setattr(self, key, Node(key, parent=getattr(self, parent), kwargs=value))

        print(RenderTree(self.root).by_attr())


@silence
async def change_ip():
    from lib.log import Log
    from stem import Signal
    from stem.control import Controller

    log = Log().child()
    with Controller.from_port(port=9051) as controller:
        # controller.authenticate(password='1Zaragoza$.')
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
    log.debug('Signal.NEWNYM to Tor controller port:9051')


async def tor():
    from lib.log import Log

    log = Log().child()

    old_ip = await commands()
    await change_ip()
    new_ip = await commands()
    assert old_ip != new_ip,\
        "Error changing IP\nAssertionError: New IP: {0}\nAssertionError: Old IP: {1}".format(new_ip, old_ip)
    log.info('Tor IP changed to: {' + format(new_ip).rstrip() + '} from {'
             + format(old_ip).rstrip() + '}')


# region tabview
# def tabview_locals(private=False, modules=False, functions=False, max_width=128):
    # tabview = gtabview.view
    # data = []
    # for k, v in currentframe().f_back.f_locals.items():
    #     if v.__class__.__name__ == '_Feature':
    #         continue
    #     if not private and k[0] == '_':
    #         continue
    #     if not modules and type(v) == type(sys):
    #         continue
    #     if not functions and type(v) == types.FunctionType:
    #         continue
    #     value = v
    #     if isinstance(value, pd.DataFrame):
    #         value = list(value.columns)
    #     value = repr(str(value))[1:-1]
    #     if len(value) > max_width:
    #         value = value[:max_width - 1] + '…'
    #     data.append([k, v.__class__.__name__, value])
    # data = pd.DataFrame(data, columns=['NAME', 'TYPE', 'VALUE'])
    # data.set_index(data['NAME'], inplace=True)
    # data.drop('NAME', axis=1, inplace=True)
    # tabview(data, title='bound local variables')
# endregion

def silence(f):
    import logging

    def wrapper(*args, **kwargs):
        log = logging.getLogger('stem')
        log.disabled = True
        ret = f(*args, **kwargs)
        log.enabled = True
        return ret
    return wrapper


