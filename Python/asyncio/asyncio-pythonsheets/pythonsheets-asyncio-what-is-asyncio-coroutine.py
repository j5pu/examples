# https://www.pythonsheets.com
import asyncio
import random

# prueba: 1 - What is @asyncio.coroutine?¶
"""

"""
import asyncio
import inspect
from functools import wraps

Future = asyncio.futures.Future
def coroutine(func):
    """Simple prototype of coroutine"""
    @wraps(func)
    def coro(*a, **k):
        res = func(*a, **k)
        if isinstance(res, Future) or inspect.isgenerator(res):
            res = yield from res
        return res
    return coro

@coroutine
def foo():
    yield from asyncio.sleep(1)
    print("Hello Foo")

@asyncio.coroutine
def bar():
    print("Hello Bar")

loop = asyncio.get_event_loop()
tasks = [loop.create_task(foo()),
         loop.create_task(bar())]
loop.run_until_complete(
     asyncio.wait(tasks))
loop.close()
"""

"""

# prueba: 2 - What is a Task?¶
"""

"""
# goal: supervise coroutine run state
# ref: asyncio/tasks.py

import asyncio
Future = asyncio.futures.Future

class Task(Future):
    """Simple prototype of Task"""

    def __init__(self, gen, *,loop):
        super().__init__(loop=loop)
        self._gen = gen
        self._loop.call_soon(self._step)

    def _step(self, val=None, exc=None):
        try:
            if exc:
                f = self._gen.throw(exc)
            else:
                f = self._gen.send(val)
        except StopIteration as e:
            self.set_result(e.value)
        except Exception as e:
            self.set_exception(e)
        else:
            f.add_done_callback(
                 self._wakeup)

    def _wakeup(self, fut):
        try:
            res = fut.result()
        except Exception as e:
            self._step(None, e)
        else:
            self._step(res, None)

@asyncio.coroutine
def foo():
    yield from asyncio.sleep(3)
    print("Hello Foo")

@asyncio.coroutine
def bar():
    yield from asyncio.sleep(1)
    print("Hello Bar")

loop = asyncio.get_event_loop()
tasks = [Task(foo(), loop=loop),
         loop.create_task(bar())]
loop.run_until_complete(
        asyncio.wait(tasks))
loop.close()
"""

"""

# prueba: 3 - What event loop doing? (Without polling)¶
"""

"""
import asyncio

async def wait(fs, loop=None):
    fs = {asyncio.ensure_future(_) for _ in set(fs)}
    if loop is None:
        loop = asyncio.get_event_loop()

    waiter = loop.create_future()
    counter = len(fs)

    def _on_complete(f):
        nonlocal counter
        counter -= 1
        if counter <= 0 and not waiter.done():
             waiter.set_result(None)

    for f in fs:
        f.add_done_callback(_on_complete)

    # wait all tasks done
    await waiter

    done, pending = set(), set()
    for f in fs:
        f.remove_done_callback(_on_complete)
        if f.done():
            done.add(f)
        else:
            pending.add(f)
    return done, pending

async def slow_task(n):
    await asyncio.sleep(n)
    print('sleep "{}" sec'.format(n))

loop = asyncio.get_event_loop()

try:
    print("---> wait")
    loop.run_until_complete(
            wait([slow_task(_) for _ in range(1,3)]))
    print("---> asyncio.wait")
    loop.run_until_complete(
            asyncio.wait([slow_task(_) for _ in range(1,3)]))
finally:
    loop.close()
"""

"""

# prueba: 4 - Future like object¶

"""

"""
import sys
PY_35 = sys.version_info >= (3, 5)
loop = asyncio.get_event_loop()
async def slow_task(n):
    await asyncio.sleep(n)
class SlowObj:
    def __init__(self, n):
        print("__init__")
        self._n = n
    if PY_35:
        def __await__(self):
            print("__await__")
            yield from slow_task(self._n).__await__()
            yield from asyncio.sleep(self._n)
            print("ok")
            return self

async def main():
    obj = await SlowObj(1)

loop.run_until_complete(main())


# prueba: 2 - Transport and Protocol¶
import asyncio

class EchoProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        msg = data.decode()
        self.transport.write(data)

loop = asyncio.get_event_loop()
coro = loop.create_server(EchoProtocol, 'localhost', 5566)
server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except:
    loop.run_until_complete(server.wait_closed())
finally:
    loop.close()
# prueba: 3 - Transport and Protocol with SSL¶
    import asyncio
    import ssl


    def make_header():
        head = b'HTTP/1.1 200 OK\r\n'
        head += b'Content-Type: text/html\r\n'
        head += b'\r\n'
        return head


    def make_body():
        resp = b"<html>"
        resp += b"<h1>Hello SSL</h1>"
        resp += b"</html>"
        return resp


    sslctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    sslctx.load_cert_chain(certfile='./root-ca.crt',
                           keyfile='./root-ca.key')


    class Service(asyncio.Protocol):

        def connection_made(self, tr):
            self.tr = tr
            self.total = 0

        def data_received(self, data):
            if data:
                resp = make_header()
                resp += make_body()
                self.tr.write(resp)
            self.tr.close()


    async def start():
        server = await loop.create_server(Service,
                                          'localhost',
                                          4433,
                                          ssl=sslctx)
        await server.wait_closed()


    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start())
    finally:
        loop.close()


# prueba: 4 - What loop.create_server do?¶
    import asyncio
    import socket

    loop = asyncio.get_event_loop()


    async def create_server(loop, protocol_factory, host,
                            port, *args, **kwargs):
        sock = socket.socket(socket.AF_INET,
                             socket.SOCK_STREAM, 0)
        sock.setsockopt(socket.SOL_SOCKET,
                        socket.SO_REUSEADDR, 1)
        sock.setblocking(False)
        sock.bind((host, port))
        sock.listen(10)
        sockets = [sock]
        server = asyncio.base_events.Server(loop, sockets)
        loop._start_serving(protocol_factory, sock, None, server)

        return server


    class EchoProtocol(asyncio.Protocol):
        def connection_made(self, transport):
            peername = transport.get_extra_info('peername')
            print('Connection from {}'.format(peername))
            self.transport = transport

        def data_received(self, data):
            message = data.decode()
            self.transport.write(data)


    # Equal to: loop.create_server(EchoProtocol,
    #                              'localhost', 5566)
    coro = create_server(loop, EchoProtocol, 'localhost', 5566)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    finally:
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()
    # prueba: 4 -What loop.sock_* do?¶
    import asyncio
    import socket


    def sock_accept(self, sock, fut=None, registed=False):
        fd = sock.fileno()
        if fut is None:
            fut = self.create_future()
        if registed:
            self.remove_reader(fd)
        try:
            conn, addr = sock.accept()
            conn.setblocking(False)
        except (BlockingIOError, InterruptedError):
            self.add_reader(fd, self.sock_accept, sock, fut, True)
        except Exception as e:
            fut.set_exception(e)
        else:
            fut.set_result((conn, addr))
        return fut


    def sock_recv(self, sock, n, fut=None, registed=False):
        fd = sock.fileno()
        if fut is None:
            fut = self.create_future()
        if registed:
            self.remove_reader(fd)
        try:
            data = sock.recv(n)
        except (BlockingIOError, InterruptedError):
            self.add_reader(fd, self.sock_recv, sock, n, fut, True)
        except Exception as e:
            fut.set_exception(e)
        else:
            fut.set_result(data)
        return fut


    def sock_sendall(self, sock, data, fut=None, registed=False):
        fd = sock.fileno()
        if fut is None:
            fut = self.create_future()
        if registed:
            self.remove_writer(fd)
        try:
            n = sock.send(data)
        except (BlockingIOError, InterruptedError):
            n = 0
        except Exception as e:
            fut.set_exception(e)
            return
        if n == len(data):
            fut.set_result(None)
        else:
            if n:
                data = data[n:]
            self.add_writer(fd, sock, data, fut, True)
        return fut


    async def handler(loop, conn):
        while True:
            msg = await loop.sock_recv(conn, 1024)
            if msg:
                await loop.sock_sendall(conn, msg)
            else:
                break
        conn.close()


    async def server(loop):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setblocking(False)
        sock.bind(('localhost', 9527))
        sock.listen(10)

        while True:
            conn, addr = await loop.sock_accept(sock)
            loop.create_task(handler(loop, conn))


    EventLoop = asyncio.SelectorEventLoop
    EventLoop.sock_accept = sock_accept
    EventLoop.sock_recv = sock_recv
    EventLoop.sock_sendall = sock_sendall
    loop = EventLoop()

    try:
        loop.run_until_complete(server(loop))
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
    # prueba: 4 - Simple asyncio connection pool¶
    import asyncio
    import socket
    import uuid


    class Transport:

        def __init__(self, loop, host, port):
            self.used = False

            self._loop = loop
            self._host = host
            self._port = port
            self._sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            self._sock.setblocking(False)
            self._uuid = uuid.uuid1()

        async def connect(self):
            loop, sock = self._loop, self._sock
            host, port = self._host, self._port
            return (await loop.sock_connect(sock, (host, port)))

        async def sendall(self, msg):
            loop, sock = self._loop, self._sock
            return (await loop.sock_sendall(sock, msg))

        async def recv(self, buf_size):
            loop, sock = self._loop, self._sock
            return (await loop.sock_recv(sock, buf_size))

        def close(self):
            if self._sock: self._sock.close()

        @property
        def alive(self):
            ret = True if self._sock else False
            return ret

        @property
        def uuid(self):
            return self._uuid


    class ConnectionPool:

        def __init__(self, loop, host, port, max_conn=3):
            self._host = host
            self._port = port
            self._max_conn = max_conn
            self._loop = loop

            conns = [Transport(loop, host, port) for _ in range(max_conn)]
            self._conns = conns

        def __await__(self):
            for _c in self._conns:
                yield from _c.connect().__await__()
            return self

        def getconn(self, fut=None):
            if fut is None:
                fut = self._loop.create_future()

            for _c in self._conns:
                if _c.alive and not _c.used:
                    _c.used = True
                    fut.set_result(_c)
                    break
            else:
                loop.call_soon(self.getconn, fut)

            return fut

        def release(self, conn):
            if not conn.used:
                return
            for _c in self._conns:
                if _c.uuid != conn.uuid:
                    continue
                _c.used = False
                break

        def close(self):
            for _c in self._conns:
                _c.close()


    async def handler(pool, msg):
        conn = await pool.getconn()
        byte = await conn.sendall(msg)
        mesg = await conn.recv(1024)
        pool.release(conn)
        return 'echo: {}'.format(mesg)


    async def main(loop, host, port):
        try:
            # creat connection pool
            pool = await ConnectionPool(loop, host, port)

            # generate messages
            msgs = ['coro_{}'.format(_).encode('utf-8') for _ in range(5)]

            # create tasks
            fs = [loop.create_task(handler(pool, _m)) for _m in msgs]

            # wait all tasks done
            done, pending = await asyncio.wait(fs)
            for _ in done: print(_.result())
        finally:
            pool.close()


    loop = asyncio.get_event_loop()
    host = '127.0.0.1'
    port = 9527

    try:
        loop.run_until_complete(main(loop, host, port))
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
    # prueba: 4 - Simple asyncio web server¶
    import asyncio
    import socket

    host = 'localhost'
    port = 9527
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setblocking(False)
    s.bind((host, port))
    s.listen(10)

    loop = asyncio.get_event_loop()


    def make_header():
        header = b"HTTP/1.1 200 OK\r\n"
        header += b"Content-Type: text/html\r\n"
        header += b"\r\n"
        return header


    def make_body():
        resp = b'<html>'
        resp += b'<body><h3>Hello World</h3></body>'
        resp += b'</html>'
        return resp


    async def handler(conn):
        req = await loop.sock_recv(conn, 1024)
        if req:
            resp = make_header()
            resp += make_body()
            await loop.sock_sendall(conn, resp)
        conn.close()


    async def server(sock, loop):
        while True:
            conn, addr = await loop.sock_accept(sock)
            loop.create_task(handler(conn))


    try:
        loop.run_until_complete(server(s, loop))
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
        s.close()
    # Then open browser with url: localhost:9527

    # prueba: 4 - Simple HTTPS asyncio web server¶
    import asyncio
    import socket
    import ssl


    def make_header():
        head = b'HTTP/1.1 200 OK\r\n'
        head += b'Content-type: text/html\r\n'
        head += b'\r\n'
        return head


    def make_body():
        resp = b'<html>'
        resp += b'<h1>Hello SSL</h1>'
        resp += b'</html>'
        return resp


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(False)
    sock.bind(('localhost', 4433))
    sock.listen(10)

    sslctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    sslctx.load_cert_chain(certfile='./root-ca.crt',
                           keyfile='./root-ca.key')


    def do_handshake(loop, sock, waiter):
        sock_fd = sock.fileno()
        try:
            sock.do_handshake()
        except ssl.SSLWantReadError:
            loop.remove_reader(sock_fd)
            loop.add_reader(sock_fd, do_handshake,
                            loop, sock, waiter)
            return
        except ssl.SSLWantWriteError:
            loop.remove_writer(sock_fd)
            loop.add_writer(sock_fd, do_handshake,
                            loop, sock, waiter)
            return

        loop.remove_reader(sock_fd)
        loop.remove_writer(sock_fd)
        waiter.set_result(None)


    def handle_read(loop, conn, waiter):
        try:
            req = conn.recv(1024)
        except ssl.SSLWantReadError:
            loop.remove_reader(conn.fileno())
            loop.add_reader(conn.fileno(), handle_read,
                            loop, conn, waiter)
            return
        loop.remove_reader(conn.fileno())
        waiter.set_result(req)


    def handle_write(loop, conn, msg, waiter):
        try:
            resp = make_header()
            resp += make_body()
            ret = conn.send(resp)
        except ssl.SSLWantReadError:
            loop.remove_writer(conn.fileno())
            loop.add_writer(conn.fileno(), handle_write,
                            loop, conn, waiter)
            return
        loop.remove_writer(conn.fileno())
        conn.close()
        waiter.set_result(None)


    async def server(loop):
        while True:
            conn, addr = await loop.sock_accept(sock)
            conn.setblocking(False)
            sslconn = sslctx.wrap_socket(conn,
                                         server_side=True,
                                         do_handshake_on_connect=False)
            # wait SSL handshake
            waiter = loop.create_future()
            do_handshake(loop, sslconn, waiter)
            await waiter

            # wait read request
            waiter = loop.create_future()
            handle_read(loop, sslconn, waiter)
            msg = await waiter

            # wait write response
            waiter = loop.create_future()
            handle_write(loop, sslconn, msg, waiter)
            await waiter


    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(server(loop))
    finally:
        loop.close()

    # prueba: 4 - Simple asyncio WSGI web server¶
    # ref: PEP333

    import asyncio
    import socket
    import io
    import sys

    from flask import Flask, Response

    host = 'localhost'
    port = 9527
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setblocking(False)
    s.bind((host, port))
    s.listen(10)

    loop = asyncio.get_event_loop()


    class WSGIServer(object):

        def __init__(self, sock, app):
            self._sock = sock
            self._app = app
            self._header = []

        def parse_request(self, req):
            """ HTTP Request Format:

            GET /hello.htm HTTP/1.1\r\n
            Accept-Language: en-us\r\n
            ...
            Connection: Keep-Alive\r\n
            """
            # bytes to string
            req_info = req.decode('utf-8')
            first_line = req_info.splitlines()[0]
            method, path, ver = first_line.split()
            return method, path, ver

        def get_environ(self, req, method, path):
            env = {}

            # Required WSGI variables
            env['wsgi.version'] = (1, 0)
            env['wsgi.url_scheme'] = 'http'
            env['wsgi.input'] = req
            env['wsgi.errors'] = sys.stderr
            env['wsgi.multithread'] = False
            env['wsgi.multiprocess'] = False
            env['wsgi.run_once'] = False

            # Required CGI variables
            env['REQUEST_METHOD'] = method  # GET
            env['PATH_INFO'] = path  # /hello
            env['SERVER_NAME'] = host  # localhost
            env['SERVER_PORT'] = str(port)  # 9527
            return env

        def start_response(self, status, resp_header, exc_info=None):
            header = [('Server', 'WSGIServer 0.2')]
            self.headers_set = [status, resp_header + header]

        async def finish_response(self, conn, data, headers):
            status, resp_header = headers

            # make header
            resp = 'HTTP/1.1 {0}\r\n'.format(status)
            for header in resp_header:
                resp += '{0}: {1}\r\n'.format(*header)
            resp += '\r\n'

            # make body
            resp += '{0}'.format(data)
            try:
                await loop.sock_sendall(conn, str.encode(resp))
            finally:
                conn.close()

        async def run_server(self):
            while True:
                conn, addr = await loop.sock_accept(self._sock)
                loop.create_task(self.handle_request(conn))

        async def handle_request(self, conn):
            # get request data
            req = await loop.sock_recv(conn, 1024)
            if req:
                method, path, ver = self.parse_request(req)
                # get environment
                env = self.get_environ(req, method, path)
                # get application execute result
                res = self._app(env, self.start_response)
                res = [_.decode('utf-8') for _ in list(res)]
                res = ''.join(res)
                loop.create_task(
                    self.finish_response(conn, res, self.headers_set))


    app = Flask(__name__)


    @app.route('/hello')
    def hello():
        return Response("Hello WSGI", mimetype="text/plain")


    server = WSGIServer(s, app.wsgi_app)
    try:
        loop.run_until_complete(server.run_server())
    except:
        pass
    finally:
        loop.close()

    # Then open browser with url: localhost:9527/hello
    # prueba: 4 -

    # prueba: 4 -


    exit(0)