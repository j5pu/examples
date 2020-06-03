from lib.log import logger
from utils import ini_try
import os
import sh

import time
import random
from stem import Signal, SocketError, SocketClosed, ProtocolError
from stem.control import Controller, EventType

TOR_CONTROL_PORT = int(os.getenv('TOR_CONTROL_PORT', 'NULL'))
TOR_PASSWORD = os.getenv('TOR_CONTROL_PORT', 'NULL')

log = logger()
ini = ini_try()

ip_change_streams = int(ini['tor']['ip_change_streams'])
ip_change_min = int(ini['tor']['ip_change_min'])
ip_change_max = int(ini['tor']['ip_change_max'])

sudo = sh.sudo.bake("-S")


def random_ip_change():
    global counter
    # new_ip = os.popen('curl ipecho.net/plain')

    change = random.randint(ip_change_min, ip_change_max)
    if counter >= change:
        with Controller.from_port(port=TOR_CONTROL_PORT) as controller:
            controller.authenticate(TOR_PASSWORD)
            controller.signal(Signal.NEWNYM)
            counter = 0
            # new_ip = os.popen('curl -sS --output /dev/null  ipecho.net/plain')
            # log.info('IP changed: {}'.format(new_ip.read()))
    counter += 1
    # print('{}-{}-{}'.format(counter, change, new_ip.read()))


def tor_ip_change():
    with Controller.from_port(port=TOR_CONTROL_PORT) as controller:
        controller.authenticate(TOR_PASSWORD)
        controller.signal(Signal.NEWNYM)


def bw_response(event):
    print('sent: {}, received: {}'.format(event.written, event.read))


def stream_response(event):
    print('sent: {}, received: {}'.format(event.written, event.read))


def connect():
    l = log.child()

    try:
        controller = Controller.from_port(port=TOR_CONTROL_PORT)
        controller.authenticate(TOR_PASSWORD)
        print('a')
    except SocketClosed:
        print('b')
        pass
    except SocketError:
        print('c')

        l.e('SocketError: tor Connection refused - Trying to restart tor')
        try:
            sudo('service', 'tor', 'restart')
        except sh.ErrorReturnCode:
            log.error('tor could not be restarted')
    except ConnectionRefusedError:
        print('d')
        print('SocketError: tor Connection refused - Trying to restart tor')

        # log.error('SocketError: tor Connection refused - Trying to restart tor')
        try:
            sudo('service', 'tor', 'restart')
        except sh.ErrorReturnCode:
            print('tor could not be restarted')
            l.e('tor could not be restarted')
    else:
        return controller, controller.get_pid()


def add_event(controller, event=EventType.STREAM):
    l = log.child()

    if event == EventType.BW:
        response = 'bw_response'
    else:
        response = 'stream_response'

    try:
        controller.add_event_listener(response, event)
    except ProtocolError:
        print('tor could not be restarted')
        l.e('tor could not be restarted')


def tor_loop():
    l = log.child()

    controller, pid = connect()
    add_event(controller)
    while True:
        if controller.get_pid() != pid:
            controller, pid = connect()
            add_event(controller)
        ip = sudo('curl', 'ipecho.net/plain')
        l.debug('IP: ' + ip)
        time.sleep(4)


if __name__ == '__main__':
    tor_loop()
    # print(sh.curl('ipecho.net/plain'))
    # with Controller.from_port(port=9051) as controller:
    #     controller.authenticate('1aragon1')
    #     controller.add_event_listener(print_bw, EventType.BW)
    #
    #     bytes_read = controller.get_info("traffic/read")
    #     bytes_written = controller.get_info("traffic/written")
    #     print("My Tor relay has read %s bytes and written %s." % (bytes_read, bytes_written))
    #     time.sleep(2)

    # tor_ip_change()
