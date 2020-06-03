n = 1
########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Python Decorators
 A decorator takes in a function, adds some functionality and returns it. In this article, you will learn how you can create a decorator and why you should use it.

 Python has an interesting feature called decorators to add functionality to an existing code.

This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time. """)
print("""   """)

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ We must be comfortable with the fact that, everything in Python (Yes! Even classes), are objects. Names that we define are simply identifiers bound to these objects. 
Functions are no exceptions, they are objects too (with attributes). Various different names can be bound to the same function object.

  """)
print(""" def first(msg):
    print(msg)    

first("Hello")

second = first
second("Hello")  """)


def first(msg):
    print(msg)


first("Hello")

second = first
second("Hello")
########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Functions can be passed as arguments to another function.

If you have used functions like map, filter and reduce in Python, then you already know about this.

Such function that take other functions as arguments are also called higher order functions. Here is an example of such a function.  """)
print("""   """)


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


print(operate(inc, 3))
print(operate(dec, 3))
########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Furthermore, a function can return another function.

  """)
print(""" def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()

#Outputs "Hello"
new()  """)


def is_called():
    def is_returned():
        print("Hello")

    return is_returned


new = is_called()

# Outputs "Hello"
new()

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Getting back to Decorators
Functions and methods are called callable as they can be called.

In fact, any object which implements the special method __call__() is termed callable. So, in the most basic sense, a decorator is a callable that returns a callable.

Basically, a decorator takes in a function, adds some functionality and returns it.  """)
print("""def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")
ordinary()
# let's decorate this ordinary function
pretty = make_pretty(ordinary)
pretty()
In the example shown above, make_pretty() is a decorator. In the assignment step.

pretty = make_pretty(ordinary)
The function ordinary() got decorated and the returned function was given the name pretty.

We can see that the decorator function added some new functionality to the original function. This is similar to packing a gift. The decorator acts as a wrapper. The nature of the object that got decorated (actual gift inside) does not alter. But now, it looks pretty (since it got decorated).

Generally, we decorate a function and reassign it as,

ordinary = make_pretty(ordinary).
""")


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


def ordinary():
    print("I am ordinary")


ordinary()
print("\n# let's decorate this ordinary function")
pretty = make_pretty(ordinary)
pretty()

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@This is a common construct and for this reason, Python has a syntax to simplify this.

We can use the @ symbol along with the name of the decorator function and place it above the definition of the function to be decorated. For example,   """)
print("""def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()   """)


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


ordinary()

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ is equivalent to  """)
print("""def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

print("\n# let's decorate this ordinary function")

ordinary = make_pretty(ordinary)
ordinary()   """)


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


def ordinary():
    print("I am ordinary")


print("\n# let's decorate this ordinary function")

ordinary = make_pretty(ordinary)
ordinary()

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@Decorating Functions with Parameters
The above decorator was simple and it only worked with functions that did not have any parameters. What if we had functions that took in parameters like below?   """)
print("""def divide(a, b):
    return a/b
This function has two parameters, a and b. We know, it will give error if we pass in b as 0.

print(divide(2,5))
print(divide(2,0))
Traceback (most recent call last):
...
ZeroDivisionError: division by zero

""")


def divide(a, b):
    return a / b


print(divide(2, 5))
# print(divide(2,0))


########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Now let's make a decorator to check for this case that will cause the error.

  """)
print(""" def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b

This new implementation will return None if the error condition arises.
print(divide(2,5))
print(divide(2,0))

""")


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    return a / b


print(divide(2, 5))
print(divide(2, 0))

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@A keen observer will notice that parameters of the nested inner() function inside the decorator is same as the parameters of functions it decorates. Taking this into account, now we can make general decorators that work with any number of parameter.

In Python, this magic is done as function(*args, **kwargs). In this way, args will be the tuple of positional arguments and kwargs will be the dictionary of keyword arguments. An example of such decorator will be.
   """)
print("""def works_for_all(func):
    def inner(*args, **kwargs):
        print("\nI can decorate any function")
        print("I am going to divide", *args, "and", **kwargs)
        print("I am going to divide", args, "and", kwargs)

        return func(*args, **kwargs)
    return inner

@works_for_all
def divide(a,b):
    return a/b

@works_for_all
def imprime(a,b,c):
    print(a, b, c)

print(divide(2,5))

imprime(2,5,0)   """)


def works_for_all(func):
    def inner(*args, **kwargs):
        print(func)
        print(divide)
        print(func.__name__)
        print("\nI can decorate any function")
        if func.__name__ == 'divide':
            print("I am going to divide", *args, "and", **kwargs)
            print("I am going to divide", args, "and", kwargs)
        if func.__name__ == 'imprime':
            print("I am going to imprimir", *args, "and", **kwargs)
            print("I am going to imprimir", args, "and", kwargs)
        if func is divide:
            print("I am going to divide", *args, "and", **kwargs)
            print("I am going to divide", args, "and", kwargs)
        if func is imprime:
            print("I am going to imprimir", *args, "and", **kwargs)
            print("I am going to imprimir", args, "and", kwargs)
        return func(*args, **kwargs)

    return inner


@works_for_all
def divide(a, b):
    return a / b


@works_for_all
def imprime(a, b, c):
    print(a, b, c)


print(divide(2, 5))

imprime(2, 5, 0)

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Chaining Decorators in Python
Multiple decorators can be chained in Python.

This is to say, a function can be decorated multiple times with different (or same) decorators. We simply place the decorators above the desired function.  """)
print("""def star(func):
    def inner(*args, **kwargs):
        print("start(inner 1): args=", args, "and kwargs=", kwargs)
        print("*" * 30)
        func(*args, **kwargs)
        print("start(inner 2): args=", args, "and kwargs=", kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("percent(inner 1): args=", args, "and kwargs=", kwargs)
        print("%" * 30)
        func(*args, **kwargs)
        print("percent(inner 2): args=", args, "and kwargs=", kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print("Mensaje:",msg)
printer("Hello")   """)


def star(func):
    def inner(*args, **kwargs):
        print(func)
        print(printer)
        print(inner)
        print(star)
        print(func.__name__)
        print("start(inner 1): args=", args, "and kwargs=", kwargs)
        print("*" * 30)
        func(*args, **kwargs)
        print("start(inner 2): args=", args, "and kwargs=", kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print(func)
        print(printer)
        print(inner)
        print(percent)
        print("percent(inner 1): args=", args, "and kwargs=", kwargs)
        print("%" * 30)
        func(*args, **kwargs)
        print("percent(inner 2): args=", args, "and kwargs=", kwargs)
        print("%" * 30)

    return inner


@star
@percent
def printer(msg):
    print(printer)
    print(star)
    print(percent)
    print("Mensaje:", msg)


printer("Hello")
