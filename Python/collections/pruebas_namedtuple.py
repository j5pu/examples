import collections
import sqlite3
from pprint import pprint

"""The standard tuple uses numerical indexes to access its members.
In contrast, remembering which index should be used for each value can lead to errors, especially
if the tuple has a lot of fields and is constructed far from where it is used. A namedtuple assigns names,
as well as the numerical index, to each member.
namedtuple instances are just as memory efficient as regular tuples because they do not have per-instance dictionaries.

Each kind of namedtuple is represented by its own class, which is created by using the namedtuple() factory function. 
The arguments are the name of the new class and a string containing the names of the elements.
"""
Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('\nRepresentation:', bob)

jane = Person(name='Jane', age=29)
print('\nField by name:', jane.name)

print('\nFields by index:')
for p in [bob, jane]:
    print('{} is {} years old'.format(*p))

"""It is possible to access the fields of the namedtuple by name using dotted notation (obj.attr) as well as by using
the positional indexes of standard tuples."""
Person = collections.namedtuple('Person', 'name age')

pat = Person(name='Pat', age=12)
print('\nRepresentation:', pat)

pat.age = 21

"""Trying to change a value through its named attribute results in an AttributeError.
Field names are invalid if they are repeated or conflict with Python keywords."""

"""In situations where a namedtuple is created based on values outside the control of the program
(such as to represent the rows returned by a database query, where the schema is not known in advance), the rename 
option should be set to True so the invalid fields are renamed."""

with_class = collections.namedtuple(
    'Person', 'name class age',
    rename=True)
print(with_class._fields)

two_ages = collections.namedtuple(
    'Person', 'name age age',
    rename=True)
print(two_ages._fields)

"""Special Attributes

namedtuple provides several useful attributes and methods for working with subclasses and instances. All of these 
built-in properties have names prefixed with an underscore (_), which by convention in most Python programs indicates 
a private attribute. For namedtuple, however, the prefix is intended to protect the name from collision with 
user-provided attribute names.

The names of the fields passed to namedtuple to define the new class are saved in the _fields attribute."""
Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('Representation:', bob)
print('Fields:', bob._fields)

"""namedtuple instances can be converted to OrderedDict instances using _asdict()"""
Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('Representation:', bob)
print('As Dictionary:', bob._asdict())

"""The _replace() method builds a new instance, replacing the values of some fields in the process."""
Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('\nBefore:', bob)
bob2 = bob._replace(name='Robert')
print('After:', bob2)
print('Same?:', bob is bob2)

"""Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. 
They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of 
position index."""

""" Instances of the subclass also have a helpful docstring (with typename and field_names) and a helpful __repr__() 
method which lists the tuple contents in a name=value format."""

"""The field_names are a single string with each fieldname separated by whitespace and/or commas, 
for example 'x y' or 'x, y'. Alternatively, field_names can be a sequence of strings such as ['x', 'y']."""

# Basic example
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)     # instantiate with positional or keyword arguments
print(p[0] + p[1])      # indexable like the plain tuple (11, 22)
x, y = p                # unpack like a regular tuple
var = (x, y)
print(var)
print(p.x + p.y)        # fields also accessible by name

print(p)               # readable __repr__ with a name=value style

"""Named tuples are especially useful for assigning field names to result tuples returned 
by the csv or sqlite3 modules:"""
EmployeeRecord = collections.namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
import csv
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
    print(emp.name, emp.title)

conn = sqlite3.connect('/companydata')
cursor = conn.cursor()
cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print(emp.name, emp.title)


"""In addition to the methods inherited from tuples, named tuples support three additional methods and two attributes. 
To prevent conflicts with field names, the method and attribute names start with an underscore."""
t = [11, 22]
Point._make(t)
pprint(Point)

"""somenamedtuple._make(iterable)¶
Class method that makes a new instance from an existing sequence or iterable."""
t = [11, 22]
Point._make(t)
Point(x=11, y=22)
pprint(Point)

""" somenamedtuple._asdict()
Return a new OrderedDict which maps field names to their corresponding values:"""
p = Point(x=11, y=22)
p._asdict()
pprint(collections.OrderedDict([('x', 11), ('y', 22)]))

""" somenamedtuple._replace(**kwargs)
Return a new instance of the named tuple replacing specified fields with new values:"""
p = Point(x=11, y=22)
p._replace(x=33)

# for partnum, record in inventory.items():
#     inventory[partnum] = record._replace(price=newprices[partnum], timestamp=time.now())

""" somenamedtuple._source
A string with the pure Python source code used to create the named tuple class. The source makes the named 
tuple self-documenting. It can be printed, executed using exec(), or saved to a file and imported.
"""

""" somenamedtuple._fields
Tuple of strings listing the field names. Useful for introspection and for creating new named tuple types 
from existing named tuples."""
print(p._fields)           # view the field names
a = ('x', 'y')
print(a)

Color = collections.namedtuple('Color', 'red green blue')
Pixel = collections.namedtuple('Pixel', Point._fields + Color._fields)
pprint(Pixel(11, 22, 128, 255, 0))
print(Pixel(x=11, y=22, red=128, green=255, blue=0))
"""

To retrieve a field whose name is stored in a string, use the getattr() function:"""
pprint(getattr(p, 'x'))

"""To convert a dictionary to a named tuple, use the double-star-operator (as described in Unpacking Argument Lists):"""
d = {'x': 11, 'y': 22}
Point(**d)
Point(x=11, y=22)
print(Point)


"""Since a named tuple is a regular Python class, it is easy to add or change functionality with a subclass. 
Here is how to add a calculated field and a fixed-width print format:"""


class Point(collections.namedtuple('Point', 'x y')):
    __slots__ = ()

    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)


for p in Point(3, 4), Point(14, 5/7):
    print(p)

"""The subclass shown above sets __slots__ to an empty tuple. This helps keep memory requirements low 
by preventing the creation of instance dictionaries.
Subclassing is not useful for adding new, stored fields. Instead, simply create a new named tuple type from the _fields 
attribute:"""
Point3D = collections.namedtuple('Point3D', Point._fields + ('z',))

"""Docstrings can be customized by making direct assignments to the __doc__ fields:"""
Book = collections.namedtuple('Book', ['id', 'title', 'authors'])
Book.__doc__ += ': Hardcover book in active collection'
Book.id.__doc__ = '13-digit ISBN'
Book.title.__doc__ = 'Title of first printing'
Book.authors.__doc__ = 'List of authors sorted by last name'

"""Property docstrings became writeable
"""
Account = collections.namedtuple('Account', 'owner balance transaction_count')
default_account = Account('<owner name>', 0.0, 0)
johns_account = default_account._replace(owner='John')
janes_account = default_account._replace(owner='Jane')
