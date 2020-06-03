n = 1
########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Example of Inheritance in Python
  """)
print(""" A polygon is a closed figure with 3 or more sides. Say, we have a class called Polygon defined as follows.

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])  

 A triangle is a polygon with 3 sides. So, we can created a class called Triangle which inherits from Polygon. This makes all the attributes available in class Polygon readily available in Triangle. We don't need to define them again (code re-usability). Triangle is defined as follows.

   class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

        However, class Triangle has a new method findArea() to find and print the area of the triangle. Here is a sample run.


>>> t = Triangle()
>>> t.inputSides()
Enter side 1 : 3
Enter side 2 : 5
Enter side 3 : 4

>>> t.dispSides()
Side 1 is 3.0
Side 2 is 5.0
Side 3 is 4.0

>>> t.findArea()
The area of the triangle is 6.00
        """)


class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side " + format(i + 1) + " : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


t = Triangle()
# t.inputSides()
t.sides[0] = 3.0
t.sides[1] = 5.0
t.sides[2] = 4.0

t.dispSides()
t.findArea()
########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@Method Overriding in Python

  In the above example, notice that __init__() method was defined in both classes, Triangle as well Polygon. When this happens, 
  the method in the derived class overrides that in the base class. This is to say, __init__() in Triangle gets preference over the same in Polygon.

Generally when overriding a base method, we tend to extend the definition rather than simply replace it. 
The same is being done by calling the method in base class from the one in derived class (calling Polygon.__init__() from __init__() in Triangle).

A better option would be to use the built-in function super(). 
So, super().__init__(3) is equivalent to Polygon.__init__(self,3) and is preferred. You can learn more about the super() function in Python.

 """)
print("""    super().__init__(3)
             equivaalente and better than
    Polygon.__init__(self,3)     """)

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Two built-in functions isinstance() and issubclass() are used to check inheritances. 
Function isinstance() returns True if the object is an instance of the class or other classes derived from it. 
Each and every class in Python inherits from the base class object.
  """)
print("isinstance(t,Triangle)")
print(isinstance(t, Triangle))
print("isinstance(t,Polygon)")
print(isinstance(t, Polygon))
print("isinstance(t,int)")
print(isinstance(t, int))
print("isinstance(t,object)")
print(isinstance(t, object))
########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@   """)
print("""   """)
print("issubclass(Polygon,Triangle)")
print(issubclass(Polygon, Triangle))
print("issubclass(Triangle,Polygon)")
print(issubclass(Triangle, Polygon))
print("issubclass(bool,int)")
print(issubclass(bool, int))
########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Method Resolution Order in Python

Every class in Python is derived from the class object. It is the most base type in Python.

So technically, all other class, either built-in or user-defines, are derived classes and all objects are instances of object class.  """)
print(""" # Output: True
print(issubclass(list,object))

# Output: True
print(isinstance(5.5,object))

# Output: True
print(isinstance("Hello",object))  """)

# Output: True
print(issubclass(list, object))

# Output: True
print(isinstance(5.5, object))

# Output: True
print(isinstance("Hello", object))
########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Method Resolution Order (MRO)
  So, in the above example of MultiDerived class the search order is [MultiDerived, Base1, Base2, object].
  This order is also called linearization of MultiDerived class and the set of rules used to find this order is called Method Resolution Order (MRO).

MRO must prevent local precedence ordering and also provide monotonicity.
It ensures that a class always appears before its parents and in case of multiple parents, the order is same as tuple of base classes.

MRO of a class can be viewed as the __mro__ attribute or mro() method. The former returns a tuple while latter returns a list.""")
print("""class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass
print(MultiDerived.__mro__)
print(MultiDerived.mro()) """)


class Base1:
    pass


class Base2:
    pass


class MultiDerived(Base1, Base2):
    pass


print(MultiDerived.__mro__)
print(MultiDerived.mro())
########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@Here is a little more complex multiple inheritance example and its visualization along with the MRO   """)
print("""class X: pass
class Y: pass
class Z: pass

class A(X,Y): pass
class B(Y,Z): pass

class M(B,A,Z): pass

# Output:
# [<class '__main__.M'>, <class '__main__.B'>,
# <class '__main__.A'>, <class '__main__.X'>,
# <class '__main__.Y'>, <class '__main__.Z'>,
# <class 'object'>]

print(M.mro())   """)


class X: pass


class Y: pass


class Z: pass


class A(X, Y): pass


class B(Y, Z): pass


class M(B, A, Z): pass


# Output:
# [<class '__main__.M'>, <class '__main__.B'>,
# <class '__main__.A'>, <class '__main__.X'>,
# <class '__main__.Y'>, <class '__main__.Z'>,
# <class 'object'>]

print(M.mro())