# https://www.programiz.com/python-programming
from pprint import pprint
class MyClass:
    """This is my second class"""
    a = 10
    def func(self):
        print('Hello')

# create a new MyClass
ob = MyClass()

# Output: <function MyClass.func at 0x000000000335B0D0>
print(MyClass.func)

print(MyClass)

# Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
print(ob.func)

# Calling function func()
# Output: Hello
ob.func()

pass

class Parrot:
    # CLASS ATTRIBUTE
    species = "bird"

    # INSTANCE ATTRIBUTE
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

blu = Parrot("Blu", 10)

print(Parrot.species)
print(Parrot.mro())
print(Parrot.mro)
print(Parrot.__module__)
print(Parrot.__doc__)
print(Parrot.__class__)
print(Parrot.__base__)
print(Parrot.__bases__)
print(Parrot.__qualname__)
print(Parrot.__name__)

print(blu)
print(blu.__class__)
print(blu.__dict__)
print(blu.__dir__())
print(blu.__getattribute__('name'))
print(blu.__repr__())
print(blu.__str__())
print(blu.__doc__)
print(blu.__module__)

pprint(blu)
print(blu.sing("'Happy'"))
print(blu.dance())

class A:
    y = None
    def foo(self, x):
        self.x = x

    @classmethod
    def class_foo(cls, y):
        cls.y = y
        print(cls.__name__)
        print(cls.__qualname__)
        print(cls.__dict__)
        print(cls.y)

    @staticmethod
    def static_foo(cls, z):
        cls.y = z
        print(cls.__name__)
        print(cls.__qualname__)
        print(cls.__dict__)
        print(cls.y)

    @property
    def prop_foo(self):
        return self.x

a = A()
print(a.foo)
print(a.foo(1))
print(a.x)
print(A.y)

a.class_foo(1)
A.class_foo(1)
print(a.class_foo(1))
print(a.y)
print(A.class_foo(1))
print(A.class_foo(2))
print(A.y)
print(A.static_foo(A, 3))
print(A.y)

print(a.prop_foo)

# parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

otro = Bird()
otro.whoisThis()
peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

# encapsulation
## obj.__variable__ = value NO CAMBIA EL VALOR SOLO CON FUNCION EN EL OBJETO
class Computer:

    def __init__(self):
        self.__maxprice = 900
        self.minprice = 500

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
        print("Selling Min Price: {}".format(self.minprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

    def setMinPrice(self, price):
        self.minprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.minprice = 400
c.sell()

# using setter function
c.setMaxPrice(1000)
c.setMinPrice(300)
c.sell()

# Polymorphism is an ability (in OOP) to use common interface for multiple form (data types). METHOD que se usa para todas las CLASS
class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)

# CONSTRUCTORS
class ComplexNumber:
    def __init__(self,r = 0,i = 0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

# Create a new ComplexNumber object
c1 = ComplexNumber(2,3)

# Call getData() function
# Output: 2+3j
c1.getData()

# Create another ComplexNumber object
# and create a new attribute 'attr'
c2 = ComplexNumber(5)
c2.attr = 10

# Output: (5, 0, 10)
print((c2.real, c2.imag, c2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
# c1.attr

# Generator Expression
my_list = [1, 3, 6, 10]
print(my_list)
comp = [x ** 2 for x in my_list]
print(comp)
genera = (x**2 for x in my_list)
print(genera)
for numero in (x**2 for x in my_list):
    print(numero)

my_string = 'programiz'
# my_string[5] = 'a'


a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)

colors = ['red',
          'blue',
          'green']

print(a, colors)

# [Operator Overloading]
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

p1 = Point(2,3)
print(p1)

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
p1 = Point(2,3)
print(p1)

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

p1 = Point(2,3)
print(p1)

p2 = Point(-1,2)
print(p1 + p2)


# [Arithmetic operators]
x=2
y=1
print(x/y) # cociente/quotient (float)
print(x%y) # remainder/resto
print(x//y) # cociente/quotient (int)

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

