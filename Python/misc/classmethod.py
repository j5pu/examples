from aioify import aioify as aio
from pprint import pprint

# @aio
# async def main():
#     print('hola')
#
# main()
class Date:

    def __init__(self, day=0, month=0, year=0):
        print('__init__')
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @classmethod
    def from_int(cls, day=0, month=0, year=0):
        cls.day = day
        cls.month = month
        cls.year = year
        date1 = cls(day, month, year)
        return date1

    @classmethod
    def from_int_sin_instance(cls, day=0, month=0, year=0):
        cls.day = day
        cls.month = month
        cls.year = year
        return cls

    @classmethod
    def init(cls):
        # Puedo mirar las columnas que tiene y que lo haga solo el copiar y crear el objeto
        date1 = cls(cls.__dict__['day'], cls.__dict__['month'], cls.__dict__['year'])
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

print('- Class - Objec')
date2 = Date.from_int_sin_instance(11, 9, 2012)
date2.month = 4
date2.year = 10
date2.day = 1
pprint(date2.__mro__)
pprint(date2)
pprint(date2.__dict__)

print('- Object de Class.init()')
date3 = date2.init()
pprint(date2.__mro__)
pprint(date3)
pprint(date3.__dict__)

print('- Object de Class()')
date4 = Date.from_int(11, 9, 2012)
pprint(date2.__mro__)
pprint(date4)
print(date4.__dict__)

is_date = Date.is_date_valid('11-09-2012')