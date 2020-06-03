print("""------------------------------------------------------------------------------------------------------------
""")
print("""What is the difference between @staticmethod and @classmethod in Python?

With a module function it is easier to import just the function you need and prevent unnecessary "." syntax
Class methods have more use since they can be used in combination with polymorphism to create factory pattern functions.
this is because class methods receive the class as an implicit parameter

""")
print("""Maybe a bit of example code will help:

class A(object):
    def foo(self,x):
        print("executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        print("executing class_foo(%s,%s)"%(cls,x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)"%x)
""")


class A(object):
    c = 10
    def __init__(self):
        self.y = 3
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        self.x = x
        self.z = 4
        print('A.foo(' + format(A.foo) + ',' + format(x) + ')')

        print('foo.self(' + format(self) + ',' + format(x) + ')')
        print('foo() self.x = ' + format(self.x))
        self.static = self.class_foo(8)
        print('foo() self.class_foo = ' + format(self.static))
        self.static = self.static_foo(4)

        print('foo() self.static_foo = ' + format(self.static))
        return('foo(' + format(self.x) + ') executed')

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        cls.x = x
        print('A.class_foo(' + format(A.class_foo) + ',' + format(x) + ')')

        print('class_foo.cls(' + format(cls) + ',' + format(x) + ')')
        print('class_foo() cls.x = ' + format(cls.x))
        print('class_foo() cls.y = ' + format(cls.y))
        print('class_foo() cls.z = ' + format(cls.z))

        return('class_foo(' + format(cls.x) + ') executed')

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)
        print('A.static_foo(' + format(A.static_foo) + ',' + format(x) + ')')
        return ('static_foo(' + format(x) + ') executed')

print("""Notice the difference in the call signatures
of foo, class_foo and static_foo:

a = A()
""")
a = A()
print('a:', a)
print('a.c:', a.c)
# print('a():', a())

print('a.foo:', a.foo)
print('a.foo(1):', a.foo(1))
# print('a.foo.f:', a.foo.f)
# print('a.foo.f:', a.foo(1).f)
# print('a.foo.f:', a.f)

print('A:', A)
print('A.c:', A.c)
print('A():', A())
print('A():', A())
b = A()
print('b:', b)
c = A()
print('c:', c)

print('A().c:', A().c)
print('A.foo:', A.foo)
# print('A.foo():', A.foo(1))
# print('A.foo.f:', A.foo(1).f)
print('a.class_foo(1):', a.class_foo(1))
print('a.class_foo:', a.class_foo)

print('A.class_foo(1):', A.class_foo(1))
# print('A.class_foo(1):', A.class_foo(1).f)

print("""Below is the usual way an object instance calls a method.
The object instance, a, is implicitly passed as the first argument.
""")
print("""a.foo(1)
""")
a.foo(1)

print("""Con classmethod the class of the object instance is implicitly passed as the first argument instead of self.
""")
print("""------------------------------------------------------------------------------------------------------------
""")
print("""a.class_foo(1)
""")
a.class_foo(1)
print("""You can also call class_foo using the class.
In fact, if you define something to be a classmethod,
it is probably because you intend to call it from the class rather than from a class instance. 
A.foo(1) would have raised a TypeError, but A.class_foo(1) works just fine:

A.class_foo(1)
""")
A.class_foo(1)
print("""One use people have found for class methods is to create inheritable alternative constructors.

""")
print("""Con staticmethods, neither self (the object instance)
nor  cls (the class) is implicitly passed as the first argument.
They behave like plain functions except that you can call them from an instance or the class:""")
print("""------------------------------------------------------------------------------------------------------------
""")
print("""a.static_foo(1)

A.static_foo('hi')
""")
a.static_foo(1)

A.static_foo('hi')
print("""Staticmethods are used to group functions which have some logical connection with a class to the class.
""")
print("""------------------------------------------------------------------------------------------------------------
""")
print("""foo is just a function, but when you call a.foo you don't just get the function,
you get a "partially applied" version of the function with the object instance a bound
as the first argument to the function.
foo expects 2 arguments, while a.foo only expects 1 argument.

""")
print("""a is bound to foo. That is what is meant by the term "bound" below:

""")
print("""print(a.foo)
""")
print(a.foo)

print("""With a.class_foo, a is not bound to class_foo, 
rather the class A is bound to class_foo.

""")
print("""print(a.class_foo)
""")
print(a.class_foo)

print("""Here, with a staticmethod, even though it is a method, 
a.static_foo just returns a good 'ole function with no arguments bound. 
static_foo expects 1 argument, and a.static_foo expects 1 argument too.
""")
print("""print(a.static_foo)
""")
print(a.static_foo)
print("""And of course the same thing happens when you call static_foo with the class A instead.

""")
print("""print(A.static_foo)
""")
print(A.static_foo)
print("""------------------------------------------------------------------------------------------------------------
""")
