from collections import namedtuple
from dataclasses import dataclass
from pprint import pprint
import typing

# https://realpython.com/python-data-classes/
#el namedtuple es inmutable el otro no, valores por defecto en nametuple jodidos etc.
Customer = namedtuple('Customer', 'name age experience accidents')

customers_data = [
    ['John Carl', 32, 13, 0],
    ['Mary Carl', 25, 27, 159],
    ['Mary Melody', 28, 13, 32],
    ['Susie Perl', 33, 17, 12],
    ['Andy Wharton', 66, 24, 0],
    ['Jorge Mar', 44, 18, 24],
    ['Mary Jorge', 37, 24, 36]
]
print(f'Customer._fields: {Customer._fields}')

customers = [Customer(*customer_data) for customer_data in customers_data]

customers = [customer._asdict() for customer in customers]

print(f'type(customers): {type(customers)}')
pprint(customers)

print('\n')
for customer in customers:
    print(f"customer['name']: {customer['name']}")

print('\n')
customer = Customer('Ana', 34, 5, 2)
print(f'customer._fields: {customer._fields}')
print(f'customer._field_defaults: {customer._field_defaults}')


print('-- namedtuple with defaults -------------------------------------')
fields = ('first', 'second', 'third')
Node = namedtuple('Node', fields, defaults=(None,) * len(fields))
print(Node())

print('\n')
defaults = (str(), {}, 1)
Node = namedtuple('Node', fields, defaults=defaults)
print(Node())

print('\n')

print('-- namedtuple with __doc__ -------------------------------------')
Node.__doc__ = ': Node description'
Node.first.__doc__ = 'first field of Node'
Node.first.__doc__ = 'second field of Node'
Node.first.__doc__ = 'third field of Node'

print('-- namedtuple with type hints and defaults -------------------------------------')
Component = namedtuple('Component', ['part_number', 'weight', 'description'])

# equivale a:
class Component(typing.NamedTuple):
    """Represents an component."""
    # Fields with a default value must come after any fields without a default.
    part_number: int
    weight: float = 3.4
    description: typing.Optional[str] = None

component = Component(2)
print(f'typing.NamedTuple component: {component}')

print('\n')

print('-- dataclass mejor que typing.NamedTuple with type hints and defaults -------------------------------------')
@dataclass(order=True, unsafe_hash=False, frozen=False)
class Component():
    """Represents an component."""
    # Fields with a default value must come after any fields without a default.
    part_number: int
    weight: float = 3.4
    description: typing.Optional[str] = None

component = Component(2)

print(f'dataclass component: {component}')

print('\n')

print('--- Since a named tuple is a regular Python class, it is easy to add or change functionality with a subclass pero para eso el @dataclass')
class Point(namedtuple('Point', ['x', 'y'])):
    __slots__ = ()
    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def __str__(self):
        return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

for p in Point(3, 4), Point(14, 5/7):
    print(p)

print('\n')


