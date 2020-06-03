n = 1
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ What is operator overloading in Python?

Python operators work for built-in classes. But same operator behaves differently with different types. 
For example, the + operator will, perform arithmetic addition on two numbers, merge two lists and concatenate two strings.

This feature in Python, that allows same operator to have different meaning according to the context is called operator overloading.

So what happens when we use them with objects of a user-defined class? Let us consider the following class, which tries to simulate a point in 2-D coordinate system.

Using special functions, we can make our class compatible with built-in functions.

if we define __str__() method in our class, we can control how it gets printed.


""")
print("""class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

p1 = Point(2,3)
print(p1)
print(format(p1))
print(p1.__str__())
""")


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

p1 = Point(2,3)
print(p1)
print(format(p1))
print(p1.__str__())

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Overloading the + Operator in Python
To overload the + sign, we will need to implement __add__() function in the class. With great power comes great responsibility.
We can do whatever we like, inside this function. But it is sensible to return a Point object of the coordinate sum.

  """)
print(""" class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(2,3)
print(p1)
print(format(p1))
print(p1.__str__())
p2 = Point(-1,2)
print(p1 + p2)
print(p1.__add__(p2))
print(Point.__add__(p1,p2))  """)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(2,3)
print(p1)
print(format(p1))
print(p1.__str__())
p2 = Point(-1,2)
print(p1 + p2)
print(p1.__add__(p2))
print(Point.__add__(p1,p2))

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Overloading Comparison Operators in Python

Python does not limit operator overloading to arithmetic operators only. We can overload comparison operators as well.

Suppose, we wanted to implement the less than symbol < symbol in our Point class.

Let us compare the magnitude of these points from the origin and return the result for this purpose. It can be implemented as follows.

  """)
print("""   """)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag

print(Point(1,1) < Point(-2,-3))
#p1 = Point(1,1)
#p1 = Point(-2,-3)
#print(p1.__lt__(p2))
#print(Point.__lt__(p1,p2))

print(Point(1,1) < Point(0.5,-0.2))
print(Point(1,1) < Point(1,1))
