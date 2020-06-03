import enum
import argparse
class Sem(enum.Enum):
    DEFAULT = 0
    AIOHTTP = 1
    AIOCURL = 2
    DOMAIN = 3

    def __str__(self):
        return self.name

    @staticmethod
    def from_string(call_string_value):
        try:
            return Sem[call_string_value]
        except KeyError:
            raise ValueError()

Sem_values = [n for n in dir(Sem) if n[:1] != '_']

print(Sem_values)
print('--')
parser = argparse.ArgumentParser()
parser.add_argument('-semaphore', type=Sem.from_string, choices=list(Sem))
print(parser.parse_args(["-semaphore", "AIOHTTP"]))

class EnumType(object):
    """Factory for creating enum object types
    """
    def __init__(self, enum_class):
        self.enums = enum_class

    def __call__(self, call_string_value):
        name = self.enums.__name__
        try:
            return self.enums[call_string_value.upper()]
        except KeyError:
            msg = ', '.join([t.name.lower() for t in self.enums])
            msg = '{}: use one of {}'.format(name, msg)
            raise argparse.ArgumentTypeError(msg)

    def __repr__(self):
        astr = ', '.join([t.name.lower() for t in self.enums])
        return '{}({})'.format(self.enums.__name__, astr)


parser = argparse.ArgumentParser()
parser.add_argument("-semaphore", type=EnumType(Sem), default=Sem.DEFAULT, help='type info: {}'.format(type))

print('--1-')
parser.print_help()
print('--2-')

print(parser.parse_args([]))
print('--3-')

print(parser.parse_args(["-semaphore","AIOHTTP"]))
print('--4-')

print(parser.parse_args(["-semaphore","AIOCURL"]))
import asyncio
class Sem(enum.Enum):
    DEFAULT = asyncio.Semaphore(300)
    AIOHTTP = asyncio.Semaphore(140)
    AIOCURL = asyncio.Semaphore(200)
    DOMAIN = asyncio.Semaphore(8)


def semaforo(sem: Sem.__members__ = Sem.DEFAULT):
    print(list(Sem))
    return sem
print(list(Sem))
print(semaforo())
print(semaforo(sem=Sem.AIOCURL))
print('--5-')



Sema1 = {'DEFAULT': asyncio.Semaphore(300),
        'AIOHTTP': asyncio.Semaphore(200),
        'AIOCURL': asyncio.Semaphore(140),
        'DOMAIN': asyncio.Semaphore(8)}

def sema1(sem: Sema1 = Sema1['DEFAULT'])-> Sema1:
    return sem
print(sema1())
