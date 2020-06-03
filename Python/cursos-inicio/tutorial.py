#!/usr/bin/python
n: int = 1
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""https://www.jetbrains.com/help/pycharm/part-1-debugging-python-code.html""")
print("""DEBUGGIG IR AL SITIO""")
print("""import math


class Solver:

def demo(self, a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        disc = math.sqrt(d)
        root1 = (-b + disc) / (2 * a)
        root2 = (-b - disc) / (2 * a)
        return root1, root2
    elif d == 0:
        return -b / (2 * a)
    else:
        return "This equation has no roots"


if __name__ == '__main__':
    solver = Solver()

while True:
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    result = solver.demo(a, b, c)
    print(result)""")

import math

class Solver:

    def demo(self, a, b, c):
        d = b ** 2 - 4 * a * c
        if d > 0:
            disc = math.sqrt(d)
            root1 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)
            return root1, root2
        elif d == 0:
            return -b / (2 * a)
        else:
            return "This equation has no roots"


# if __name__ == '__main__':
#     solver = Solver()
#     d = 0
#
#     while d == 0:
#         a = int(input("a: "))
#         b = int(input("b: "))
#         c = int(input("c: "))
#         result = solver.demo(a, b, c)
#         print(result)
#         d = 1


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("Hello world!")

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("Hello world!")


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("Hello world!")

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
str = 'programiz'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print ('Hello ''World!')

s = ('Hello '
'World')
print (s)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'l letters found')

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
if 'a' in 'program':
    print ("a in program: True")

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
str = 'cold'

# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

#character count
print('len(str) = ', len(str))

enumera = enumerate(str)
print('enumera(str) = ', enumera)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
# using triple quotes
print('''He said, "What's there?"''')

# escaping single quotes
print('He said, "What\'s there?"')

# escaping double quotes
print("He said, \"What's there?\"")

print("C:\\Python32\\Lib")

print("This is printed\nin two lines")

print("This is \x48\x45\x58 representation")

print("This is \x61 \ngood example")

print(r"This is \x61 \ngood example")

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
# default(implicit) order
print ('format()\n')
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)

# formatting integers
print("Binary representation of {0} is {0:b}".format(12))

# formatting floats
print("Exponent representation: {0:e}".format(1566.345))

# round off
print("One third is: {0:.3f}".format(1/3))

# string alignment
print("|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham'))

x = 12.3456789
print('The value of x is %3.2f' %x)
print('The value of x is %3.4f' %x)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
# bueno: encontrar, juntar, partir, y sustituir
print ('string_methods()\n')
print("PrOgRaMiZ".lower())
print("PrOgRaMiZ".upper())
print("This will split all words into a list".split())
print(' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string']))
print('Happy New Year'.find('ew'))
print('Happy New Year'.replace('Happy','Brilliant'))

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
def double(num):
    """Function to double the value"""
    return 2*num

print(double.__doc__)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print ('Assigning multiple values to multiple variables')
a, b, c = 5, 3.2, "Hello"

print (a)
print (b)
print (c)

print ("If we want to assign the same value to multiple variables at once, we can do this as")
x = y = z = "same"

print (x)
print (y)
print (z)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print ("Numeric Literals")
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5
float_2 = 1.5e2

#Complex Literal
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("String literals")
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("Boolean literals")
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)
y = (0 == False)
print("y is", y)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print ("Special literals - None")
drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
# 376 bueno: lista, tupla, dictionario, y set

print ("Literal Collections: List literals, Tuple literals, Dict literals, and Set literals")
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

numeros = 1, 2, 3
todos = fruits, numbers, alphabets, vowels

print("List:",fruits)
print("Tuple:",numbers)
print("Dict:",alphabets)
print("Set:",vowels)

print("Tuple sin paréntesis:",numeros)
print("Tuple sin paréntesis:",todos)


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("Data type - Numbers: int, float and complex")

a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("Data type - List: is an ordered sequence of items, We can use the slicing operator [ ]")

a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

print ("\nLists are mutable, meaning, value of elements of a list can be altered.\n\
>>> a = [1,2,3]\n\
>>> a[2]=4\n\
>>> a\n\
[1, 2, 4]")
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("Data type - Tuple: is an ordered sequence of items, We can use the slicing operator ( )\nThe only difference is that tuples are immutable")

t = (5,'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
print("Generates error, Tuples are immutable:\n t[0] = 10")

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("Data type - Strings: is sequence of Unicode characters, We can use the slicing operator [ ]\nStrings are immutable")

s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Generates error
# Strings are immutable in Python
print("Generates error, Strings are immutable:\n s[5] = 'd'")

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("Data type - Set: is an unordered collection of unique items, We can use { }\nItems in a set are not ordered")

a = {5,2,3,1,4}

# printing set variable
print("a = ", a)

# data type of variable a
print("type(a)", type(a))

print("Data type - Set: have unique values.")
a = {1,2,2,3,3,3}
print("a = {1,2,2,3,3,3}")
print("They eliminate duplicates: a =",a)

print ("Hence the slicing operator [] does not work.\n\
>>> a = {1, 2, 3}\n\
>>> a[1]\n\
Traceback(most recent call last):\n\
  File \"<string>\", line 01, in runcode\n\
  File \"<interactive input>\", line 1, in < module >\n\
TypeError: 'set' object does not support indexing")

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("Data type - Dictionary: is an unordered collection of key-value pairs., Define { }\nWe must know the key to retrieve the value")
print("\ndictionaries are defined within braces {} with each item being a pair in the form key:value. Key and value can be of any type")

d = {1:'value','key':2}
print("d = {1:'value','key':2}")
print("type(d)", type(d))
print(d[1])
print(d['key'])

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print ("Conversion between data types\nWe can convert between different data types by using different type conversion functions like int(), float(), str() etc.")

print ("float(5)", float(5))
print ("int(10.6)", int(10.6))
print ("int(-10.6)", int(-10.6))
print ("float('2.5')", float('2.5'))

print ("format(25)", format(25))
print ("set([1,2,3])", set([1,2,3]))
print ("tuple({5,6,7})", tuple({5,6,7}))
print ("list('hello')", list('hello'))
print ("dict([[1,2],[3,4]])", dict([[1,2],[3,4]]))
print ("dict([(3,26),(4,44)])", dict([(3,26),(4,44)]))

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print ("Implicit Type Conversion:")

print("\nExample 1: Converting integer to float")
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

print ("\nExplicit Type Conversion: Syntax (required_datatype)(expression)")
print ("\nExample 3: Addition of string and integer using explicit conversion")
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("The actual syntax of the print() function is\nprint(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)")
print("Here, objects is the value(s) to be printed.\n\
\n\
The sep separator is used between the values. It defaults into a space character.\n\
\n\
After all values are printed, end is printed. It defaults into a new line.\n\
\n\
The file is the object where the values are printed and its default value is sys.stdout (screen). Here are an example to illustrate this.")
print(1,2,3,4)
# Output: 1 2 3 4

print(1,2,3,4,sep='*')
# Output: 1*2*3*4

print(1,2,3,4,sep='#',end='&')
# Output: 1#2#3#4&

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print ("Output formatting")

x = 5; y = 10
print("x = 5; y = 10")
print("print('The value of x is {} and y is {}'.format(x,y))")
print('The value of x is {} and y is {}'.format(x,y))

print('I love {0} and {1}'.format('bread','butter'))
# Output: I love bread and butter

print('I love {1} and {0}'.format('bread','butter'))
# Output: I love butter and bread

print ("We can even use keyword arguments to format the string.")
print("print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))")
print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("Input")
print("To allow flexibility we might want to take the input from the user. In Python, we have the input() function to allow this. The syntax for input() is: input([prompt])")
print("num = input('Enter a number: ')")
#num = input('Enter a number: ')
num = 10
print(num)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("Import")
import math
print(math.pi)
from math import pi
print(pi)
import sys
print("sys.path",sys.path)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
# 633 bueno Operators
print("Operators")
print("Example #1: Arithmetic operators in Python")
x = 15
y = 4

# Output: x + y = 19
print('x + y =',x+y)

# Output: x - y = 11
print('x - y =',x-y)

# Output: x * y = 60
print('x * y =',x*y)

# Output: x / y = 3.75
print('x / y =',x/y)

# Output: x // y = 3
print('x // y =',x//y)

# Output: x ** y = 50625
print('x ** y =',x**y)

print("\nComparison operators")
x = 10
y = 12

# Output: x > y is False
print('x > y  is',x>y)

# Output: x < y is True
print('x < y  is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)

print("\nLogical Operators")
x = True
y = False

# Output: x and y is False
print('x and y is',x and y)

# Output: x or y is True
print('x or y is',x or y)

# Output: not x is False
print('not x is',not x)

print("\Example #4: Identity operators")
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)

print("\nMembership operators")
x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("Name (also called identifier) is simply a name given to objects. Everything in Python is an object. Name is a way to access the underlying object.\nFor example, when we do the assignment a = 2, here 2 is an object stored in memory and a is the name we associate it with. We can get the address (in RAM) of some object through the built-in function, id(). Let's check it.")
# Note: You may get different value of id

a = 2
print("a = 2")
# Output: id(2)= 10919424
print('id(2) =', id(2))

# Output: id(a) = 10919424
print('id(a) =', id(a))

# Note: You may get different value of id
print("Here, both refer to the same object. Let's make things a little more interesting.")
a = 2
print("a = 2")

# Output: id(a) = 10919424
print('id(a) =', id(a))

a = a+1
print("a = a+1")
# Output: id(a) = 10919456
print('id(a) =', id(a))

# Output: id(3) = 10919456
print('id(3) =', id(3))

b = 2
print("b = 2")
# Output: id(2)= 10919424
print('id(2) =', id(2))

print("\nThis is efficient as Python doesn't have to create a new duplicate object. This dynamic nature of name binding makes Python powerful; a name could refer to any type of object.")
a = 5
print("a = 5: ",a)
a = 'Hello World!'
print("a = 'Hello World!': ",a)
a = [1,2,3]
print("a = [1,2,3]: ",a)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("namespace is a collection of names: Example of Scope and Namespace")

# 776 bueno variables scope
def outer_function():
    a = 20
    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)

print("\nIn this program, three different variables a are defined in separate namespaces and accessed accordingly. While in the following program,")
a = 10
outer_function()
print('a =', a)


def outer_function():
    global a
    a = 20

    def inner_function():
        global a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)

def outer_function():
    def inner_function():
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)

def outer_function():
    b = 2
    def inner_function():
        print('a =', a)
        print('b =', b)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)
print('b =', b)

def outer_function():
    b = 2
    def inner_function():
        global b
        b = 5
        print('a =', a)
        print('b =', b)

    inner_function()
    print('a =', a)
    print('b =', b)


a = 10
outer_function()
print('a =', a)
print('b =', b)

def outer_function():
    b = 2
    def inner_function():
        print('a =', a)
        print('b =', b)

    print('b =', b)
    inner_function()
    print('a =', a)


a = 10
print('b =', b)
outer_function()
print('a =', a)
print('b =', b)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
# Program checks if the number is positive or negative
# And displays an appropriate message

num = 3

# Try these two variations as well.
# num = -5
# num = 0

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
# In this program,
# we check if the number is positive or
# negative or zero and
# display an appropriate message

num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val

# Output: The sum is 48
print("The sum is", sum)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("# Program to iterate through a list using indexing")
genre = ['pop', 'rock', 'jazz']
# 956 bueno cuenta de 0 hasta el numero que le dices range rango

# iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("for loop with else")
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("while")
# Program to add natural
# numbers upto
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("while loop with else")
# Example to illustrate
# the use of else statement
# with the while loop

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("Example: Python break")
# Use of break statement inside loop

for val in "string":
    if val == "i":
        break
    print(val)

print("The end")
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("Example: Python continue")
# Program to show the use of continue statement inside loops
# 1037 bueno break y continue en for

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("# pass is just a placeholder for # functionality to be added later.")
# pass is just a placeholder for
# functionality to be added later.
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    print(val)
    pass

for val in sequence:
    pass

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("Example #1: Infinite loop using while")
print("""# An example of infinite loop
# press Ctrl + c to exit from the loop

while True:
   num = int(input("Enter an integer: "))
   print("The double of",num,"is",2 * num)""")
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@Loop with condition at the top")
print("""# Program to illustrate a loop with condition at the top

# Try different numbers
n = 10

# Uncomment to get user input
#n = int(input("Enter n: "))

# initialize sum and counter
sum = 0
i = 1

while i <= n:
   sum = sum + i
   i = i+1    # update counter

# print the sum
print("The sum is",sum)""")
# Program to illustrate a loop with condition at the top

# Try different numbers
n = 10

# Uncomment to get user input
#n = int(input("Enter n: "))

# initialize sum and counter
sum = 0
i = 1

while i <= n:
   sum = sum + i
   i = i+1    # update counter

# print the sum
print("The sum is",sum)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@Loop with condition in the middle")
print("""# Program to illustrate a loop with condition in the middle. 
# Take input from the user untill a vowel is entered

vowels = "aeiouAEIOU"

# infinite loop
while True:
   v = input("Enter a vowel: ")
   # condition in the middle
   if v in vowels:
       break
   print("That is not a vowel. Try again!")

print("Thank you!")""")



########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Loop with condition at the bottom ")
print("""# Python program to illustrate a loop with condition at the bottom
# Roll a dice untill user chooses to exit

# import random module
import random

while True:
   input("Press enter to roll the dice")

   # get a number between 1 to 6
   num = random.randint(1,6)
   print("You got",num)
   option = input("Roll again?(y/n) ")

   # condition
   if option == 'n':
       break
   """)



########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Example of return ")
print(""" def absolute_value(num):
    

    if num >= 0:
        return num
    else:
        return -num

# Output: 2
print(absolute_value(2))

# Output: 4
print(absolute_value(-4))  """)
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num

# Output: 2
print(absolute_value(2))

# Output: 4
print(absolute_value(-4))


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Scope and Lifetime of variables  ")
print(""" def my_func():
    x = 10
    print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)  """)

def my_func():
    x = 10
    print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Python Default Arguments ")
print(""" def greet(name, msg = "Good morning!"):
   This function greets to
   the person with the
   provided message.

   If message is not provided,
   it defaults to "Good
   morning!"

   print("Hello",name + ', ' + msg)

greet("Kate")
greet("Bruce","How do you do?")  """)
# 1241 bueno valor por defecto en parametros  en llamadas a funciones si se llama si valor

def greet(name, msg = "Good morning!"):
   """
   This function greets to
   the person with the
   provided message.

   If message is not provided,
   it defaults to "Good
   morning!"
   """

   print("Hello",name + ', ' + msg)

greet("Kate")
greet("Bruce","How do you do?")


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Arbitrary Arguments  ")
print(""" def greet(*names):
   This function greets all
   the person in the names tuple.

   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Monica","Luke","Steve","John")  """)
# 1275 bueno llamar a una funcion muchas veces cambiado el parametro de llamada

def greet(*names):
   """This function greets all
   the person in the names tuple."""

   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Monica","Luke","Steve","John")

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Example of recursive function  ")
print(""" # An example of a recursive function to
# find the factorial of a number

def calc_factorial(x):
    This is a recursive function
    to find the factorial of an integer

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = 4
print("The factorial of", num, "is", calc_factorial(num))	  """)
# An example of a recursive function to
# find the factorial of a number

def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = 4
print("The factorial of", num, "is", calc_factorial(num))
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  anonymous functions are defined using the lambda keyword - COMO UNA SUBRUTINA ANTES DE LLAMAR A LA FUNCION -  Lambda functions can have any number of arguments but only one expression.")
print(""" # Program to show the use of lambda functions

double = lambda x: x * 2
# 1330 bueno lambda funciones de una linea o expresion con muchos parametros como un alias 

# Output: 10
print(double(5))  """)

# Program to show the use of lambda functions

double = lambda x: x * 2

# Output: 10
print(double(5))

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  we generally use it as an argument to a higher-order function (a function that takes in other functions as arguments). Lambda functions are used along with built-in functions like filter(), map() etc. ")
print("""  # Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list) """)

# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print('x%2',x%2,'-me da el resto de dividor por 2')
# Output: [4, 6, 8, 12]
print(new_list)

items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Example use with map() ")
print(""" # Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)  """)


# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Example 1: Create a Global Variable ")
print(""" x = "global"

def foo():
    print("x inside :", x)

foo()
print("x outside:", x)  """)

x = "global"

def foo():
    print("x inside :", x)

foo()
print("x outside:", x)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Example 4: Using Global and Local variables in same code  ")
print(""" x = "global"

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)
    
foo()  """)

x = "global"


def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)


foo()

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Example 5: Global variable and Local variable with same name ")
print("""  x = 5

def foo():
    x = 10
    print("local x:", x)

foo()
print("global x:", x) """)
x = 5

def foo():
    x = 10
    print("local x:", x)

foo()
print("global x:", x)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Example 6: Create a nonlocal variable  ")
print(""" def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()  """)


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Example 1: Accessing global Variable From Inside a Function  ")
print(""" c = 1 # global variable

def add():
    print(c)

add()  """)

c = 1 # global variable

def add():
    print(c)

add()

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Example 2: Modifying Global Variable From Inside the Function  ")
print("""  c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c) """)
c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Example 4 : Share a global Variable Across Python Modules  ")
print("""  Create a config.py file, to store global variables

a = 0
b = "empty"
Create a update.py file, to change global variables

import config

config.a = 10
config.b = "alphabet"
Create a main.py file, to test changes in value

import config
import update

print(config.a)
print(config.b)
When we run the main.py file, the output will be

10
alphabet """)

# import config
# import update
#
# print(config.a)
# print(config.b)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Example 5: Using a Global Variable in Nested Function  ")
print("""  def foo():
    x = 20

    def bar():
        global x
        x = 25
    
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main : ", x) """)

# 1623 bueno variables scope nonlocal global

def foo():
    x = 20

    def bar():
        global x
        x = 25

    def nonlocal_bar():
        nonlocal x
        x = 8

    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)


    print("Before calling nonlocal_bar: ", x)
    print("Calling nonlocal_bar now")
    nonlocal_bar()
    print("After calling nonlocal_bar: ", x)

foo()
print("x in main : ", x)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ List Index  ")
print("""  my_list = ['p','r','o','b','e']
# Output: p
print(my_list[0])

# Output: o
print(my_list[2])

# Output: e
print(my_list[4])

# Error! Only integer can be used for indexing
# my_list[4.0]

# Nested List
n_list = ["Happy", [2,0,1,5]]

# Nested indexing

# Output: a
print(n_list[0][1])    

# Output: 5
print(n_list[1][3]) """)
my_list = ['p','r','o','b','e']
# Output: p
print(my_list[0])

# Output: o
print(my_list[2])

# Output: e
print(my_list[4])

# Error! Only integer can be used for indexing
# my_list[4.0]

# Nested List
n_list = ["Happy", [2,0,1,5]]

# Nested indexing

# Output: a
print(n_list[0][1])

# Output: 5
print(n_list[1][3])
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ How to slice lists in Python?  ")
print(""" my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5])

# elements beginning to 4th
print(my_list[:-5])

# elements 6th to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])  """)

my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5])

# elements beginning to 4th
print(my_list[:-5])

# elements 6th to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ How to change or add elements to a list?  ")
print("""  # mistake values
odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            

# Output: [1, 4, 6, 8]
print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  

# Output: [1, 3, 5, 7]
print(odd)                    """)

# mistake values
odd = [2, 4, 6, 8]

# change the 1st item
odd[0] = 1

# Output: [1, 4, 6, 8]
print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]

# Output: [1, 3, 5, 7]
print(odd)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
# 1784 bueno list.append extend y combine

print("@ We can add one item to a list using append() method or add several items using extend() method.  ")
print(""" odd = [1, 3, 5]

odd.append(7)

# Output: [1, 3, 5, 7]
print(odd)

odd.extend([9, 11, 13])

# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)  """)


odd = [1, 3, 5]

odd.append(7)

# Output: [1, 3, 5, 7]
print(odd)

odd.extend([9, 11, 13])

# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  We can also use + operator to combine two lists. This is also called concatenation. The * operator repeats a list for the given number of times.")
print("""  odd = [1, 3, 5]

# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])

#Output: ["re", "re", "re"]
print(["re"] * 3) """)


odd = [1, 3, 5]

# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])

#Output: ["re", "re", "re"]
print(["re"] * 3)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Furthermore, we can insert one item at a desired location by using the method insert() or insert multiple items by squeezing it into an empty slice of a list.  ")
print(""" odd = [1, 9]
odd.insert(1,3)

# Output: [1, 3, 9] 
print(odd)

odd[2:2] = [5, 7]

# Output: [1, 3, 5, 7, 9]
print(odd)  """)

odd = [1, 9]
odd.insert(1,3)

# Output: [1, 3, 9]
print(odd)

odd[2:2] = [5, 7]

# Output: [1, 3, 5, 7, 9]
print(odd)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ We can delete one or more items from a list using the keyword del. It can even delete the list entirely.  ")
print(""" my_list = ['p','r','o','b','l','e','m']

# delete one item
del my_list[2]

# Output: ['p', 'r', 'b', 'l', 'e', 'm']     
print(my_list)

# delete multiple items
del my_list[1:5]  

# Output: ['p', 'm']
print(my_list)

# delete entire list
del my_list       

# Error: List not defined
print(my_list)  """)
my_list = ['p','r','o','b','l','e','m']

# delete one item
del my_list[2]

# Output: ['p', 'r', 'b', 'l', 'e', 'm']
print(my_list)

# delete multiple items
del my_list[1:5]

# Output: ['p', 'm']
print(my_list)

# delete entire list
del my_list

# Error: List not defined
#print(my_list)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ We can use remove() method to remove the given item or pop() method to remove an item at the given index.

The pop() method removes and returns the last item if index is not provided. This helps us implement lists as stacks (first in, last out data structure).

We can also use the clear() method to empty a list.  """)
print(""" my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'o'
print(my_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'm'
print(my_list.pop())

# Output: ['r', 'b', 'l', 'e']
print(my_list)

my_list.clear()

# Output: []
print(my_list)  """)

my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'o'
print(my_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'm'
print(my_list.pop())

# Output: ['r', 'b', 'l', 'e']
print(my_list)

my_list.clear()

# Output: []
print(my_list)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ List Methods  ")
print(""" my_list = [3, 8, 1, 6, 0, 8, 4]

# Output: 1
print(my_list.index(8))

# Output: 2
print(my_list.count(8))

my_list.sort()

# Output: [0, 1, 3, 4, 6, 8, 8]
print(my_list)

my_list.reverse()

# Output: [8, 8, 6, 4, 3, 1, 0]
print(my_list)  """)

my_list = [3, 8, 1, 6, 0, 8, 4]

# Output: 1
print(my_list.index(8))

# Output: 2
print(my_list.count(8))

my_list.sort()

# Output: [0, 1, 3, 4, 6, 8, 8]
print(my_list)

my_list.reverse()

# Output: [8, 8, 6, 4, 3, 1, 0]
print(my_list)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  List Comprehension: Elegant way to create new List ")
print(""" pow2 = [2 ** x for x in range(10)]

# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)  """)
pow2 = [2 ** x for x in range(10)]

# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)

print(2 ** 0)
print(2 ** 1)
print(2 ** 2)
print(2 ** 3)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ List Membership Test  ")
print("""my_list = ['p','r','o','b','l','e','m']

# Output: True
print('p' in my_list)

# Output: False
print('a' in my_list)

# Output: True
print('c' not in my_list)   """)

my_list = ['p','r','o','b','l','e','m']

# Output: True
print('p' in my_list)

# Output: False
print('a' in my_list)

# Output: True
print('c' not in my_list)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Iterating Through a List ")
print(""" for fruit in ['apple','banana','mango']:
    print("I like",fruit)  """)

for fruit in ['apple','banana','mango']:
    print("I like",fruit)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Creating a Tuple ")
print("""  # empty tuple
# Output: ()
my_tuple = ()
print(my_tuple)

# tuple having integers
# Output: (1, 2, 3)
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
# Output: (1, "Hello", 3.4)
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
# Output: ("mouse", [8, 4, 6], (1, 2, 3))
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# tuple can be created without parentheses
# also called tuple packing
# Output: 3, 4.6, "dog"

my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
# Output:
# 3
# 4.6
# dog
a, b, c = my_tuple
print(a)
print(b)
print(c) """)
# empty tuple
# Output: ()
my_tuple = ()
print(my_tuple)

# tuple having integers
# Output: (1, 2, 3)
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
# Output: (1, "Hello", 3.4)
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
# Output: ("mouse", [8, 4, 6], (1, 2, 3))
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# tuple can be created without parentheses
# also called tuple packing
# Output: 3, 4.6, "dog"

my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
# Output:
# 3
# 4.6
# dog
a, b, c = my_tuple
print(a)
print(b)
print(c)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@  Creating a tuple with one element is a bit tricky.

Having one element within parentheses is not enough. We will need a trailing comma to indicate that it is in fact a tuple.""")
print(""" # only parentheses is not enough
# Output: <class 'str'>
my_tuple = ("hello")
print(type(my_tuple))

# need a comma at the end
# Output: <class 'tuple'>
my_tuple = ("hello",)  
print(type(my_tuple))

# parentheses is optional
# Output: <class 'tuple'>
my_tuple = "hello",
print(type(my_tuple))  """)

# only parentheses is not enough
# Output: <class 'str'>
my_tuple = ("hello")
print(type(my_tuple))
# 2169 bueno tuple con un elemento se añade,

# need a comma at the end
# Output: <class 'tuple'>
my_tuple = ("hello",)
print(type(my_tuple))

# parentheses is optional
# Output: <class 'tuple'>
my_tuple = "hello",
print(type(my_tuple))

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Indexing Tuple ")
print(""" my_tuple = ('p','e','r','m','i','t')

# Output: 'p'
print(my_tuple[0])

# Output: 't'
print(my_tuple[5])

# index must be in range
# If you uncomment line 14,
# you will get an error.
# IndexError: list index out of range

#print(my_tuple[6])

# index must be an integer
# If you uncomment line 21,
# you will get an error.
# TypeError: list indices must be integers, not float

#my_tuple[2.0]

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
# Output: 's'
print(n_tuple[0][3])

# nested index
# Output: 4
print(n_tuple[1][1])  """)
my_tuple = ('p','e','r','m','i','t')

# Output: 'p'
print(my_tuple[0])

# Output: 't'
print(my_tuple[5])

# index must be in range
# If you uncomment line 14,
# you will get an error.
# IndexError: list index out of range

#print(my_tuple[6])

# index must be an integer
# If you uncomment line 21,
# you will get an error.
# TypeError: list indices must be integers, not float

#my_tuple[2.0]

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
# Output: 's'
print(n_tuple[0][3])

# nested index
# Output: 4
print(n_tuple[1][1])



########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Negative Indexing Tuple ")
print("""  my_tuple = ('p','e','r','m','i','t')

# Output: 't'
print(my_tuple[-1])

# Output: 'p'
print(my_tuple[-6]) """)

my_tuple = ('p','e','r','m','i','t')

# Output: 't'
print(my_tuple[-1])

# Output: 'p'
print(my_tuple[-6])

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Slicing Tuple  ")
print(""" my_tuple = ('p','r','o','g','r','a','m','i','z')

# elements 2nd to 4th
# Output: ('r', 'o', 'g')
print(my_tuple[1:4])

# elements beginning to 2nd
# Output: ('p', 'r')
print(my_tuple[:-7])

# elements 8th to end
# Output: ('i', 'z')
print(my_tuple[7:])

# elements beginning to end
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[:])  """)


my_tuple = ('p','r','o','g','r','a','m','i','z')

# elements 2nd to 4th
# Output: ('r', 'o', 'g')
print(my_tuple[1:4])

# elements beginning to 2nd
# Output: ('p', 'r')
print(my_tuple[:-7])

# elements 8th to end
# Output: ('i', 'z')
print(my_tuple[7:])

# elements beginning to end
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[:])
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Changing a Tuple  ")
print(""" my_tuple = (4, 2, 3, [6, 5])

# we cannot change an element
# If you uncomment line 8
# you will get an error:
# TypeError: 'tuple' object does not support item assignment

#my_tuple[1] = 9

# but item of mutable element can be changed
# Output: (4, 2, 3, [9, 5])
my_tuple[3][0] = 9
print(my_tuple)

# tuples can be reassigned
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
my_tuple = ('p','r','o','g','r','a','m','i','z')
print(my_tuple)  """)

my_tuple = (4, 2, 3, [6, 5])

# we cannot change an element
# If you uncomment line 8
# you will get an error:
# TypeError: 'tuple' object does not support item assignment

#my_tuple[1] = 9

# but item of mutable element can be changed
# Output: (4, 2, 3, [9, 5])
my_tuple[3][0] = 9
print(my_tuple)

# tuples can be reassigned
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
my_tuple = ('p','r','o','g','r','a','m','i','z')
print(my_tuple)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@  We can use + operator to combine two tuples. This is also called concatenation.

We can also repeat the elements in a tuple for a given number of times using the * operator.

Both + and * operations result into a new tuple. """)
print("""  # Concatenation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3) """)

# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@  Deleting a Tuple
As discussed above, we cannot change the elements in a tuple. That also means we cannot delete or remove items from a tuple.

But deleting a tuple entirely is possible using the keyword del. """)
print("""  my_tuple = ('p','r','o','g','r','a','m','i','z')

# can't delete items
# if you uncomment line 8,
# you will get an error:
# TypeError: 'tuple' object doesn't support item deletion

#del my_tuple[3]

# can delete entire tuple
# NameError: name 'my_tuple' is not defined
del my_tuple
my_tuple """)

my_tuple = ('p','r','o','g','r','a','m','i','z')

# can't delete items
# if you uncomment line 8,
# you will get an error:
# TypeError: 'tuple' object doesn't support item deletion

#del my_tuple[3]

# can delete entire tuple
# NameError: name 'my_tuple' is not defined
del my_tuple
#my_tuple

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ tuple methods  ")
print(""" my_tuple = ('a','p','p','l','e',)

# Count
# Output: 2
print(my_tuple.count('p'))

# Index
# Output: 3
print(my_tuple.index('l'))  """)

my_tuple = ('a','p','p','l','e',)

# Count
# Output: 2
print(my_tuple.count('p'))

# Index
# Output: 3
print(my_tuple.index('l'))

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Tuple Membership Test ")
print("""  my_tuple = ('a','p','p','l','e',)

# In operation
# Output: True
print('a' in my_tuple)

# Output: False
print('b' in my_tuple)

# Not in operation
# Output: True
print('g' not in my_tuple) """)

my_tuple = ('a','p','p','l','e',)

# In operation
# Output: True
print('a' in my_tuple)

# Output: False
print('b' in my_tuple)

# Not in operation
# Output: True
print('g' not in my_tuple)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Iterating Through a Tuple  ")
print(""" # Output: 
# Hello John
# Hello Kate
for name in ('John','Kate'):
     print("Hello",name)      """)

# Output:
# Hello John
# Hello Kate
for name in ('John','Kate'):
     print("Hello",name)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ How to create a set?  ")
print(""" # set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)  """)
# set do not have duplicates
# Output: {1, 2, 3, 4}
my_set = {1,2,3,4,3,2}
print(my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# If you uncomment line #12,
# this will cause an error.
# TypeError: unhashable type: 'list'

#my_set = {1, 2, [3, 4]}

# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1,2,3,2])
print(my_set)
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)
# set do not have duplicates
# Output: {1, 2, 3, 4}
my_set = {1,2,3,4,3,2}
print(my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# If you uncomment line #12,
# this will cause an error.
# TypeError: unhashable type: 'list'

#my_set = {1, 2, [3, 4]}

# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1,2,3,2])
print(my_set)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
# 2550 bueno set vacio es diferente a = {} es a = set(), add, update, discard, remove, pop , clear, union (|), intersection (&), difference (-), diference (^)

print("""@  Creating an empty set is a bit tricky.

Empty curly braces {} will make an empty dictionary in Python. To make a set without any elements we use the set() function without any argument. """)
print("""  # initialize a with {}
a = {}

# check data type of a
# Output: <class 'dict'>
print(type(a))

# initialize a with set()
a = set()

# check data type of a
# Output: <class 'set'>
print(type(a)) """)
# initialize a with {}
a = {}

# check data type of a
# Output: <class 'dict'>
print(type(a))

# initialize a with set()
a = set()

# check data type of a
# Output: <class 'set'>
print(type(a))
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ How to change a set in Python?  ")
print(""" # initialize my_set
my_set = {1,3}
print(my_set)

# if you uncomment line 9,
# you will get an error
# TypeError: 'set' object does not support indexing

#my_set[0]

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2,3,4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4,5], {1,6,8})
print(my_set)  """)

# initialize my_set
my_set = {1,3}
print(my_set)

# if you uncomment line 9,
# you will get an error
# TypeError: 'set' object does not support indexing

#my_set[0]

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2,3,4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4,5], {1,6,8})
print(my_set)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@  How to remove elements from a set?  A particular item can be removed from set using methods, discard() and remove().

The only difference between the two is that, while using discard() if the item does not exist in the set, it remains unchanged. But remove() will raise an error in such condition.

The following example will illustrate this.""")
print(""" # initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# If you uncomment line 27,
# you will get an error.
# Output: KeyError: 2

#my_set.remove(2)  """)


# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# If you uncomment line 27,
# you will get an error.
# Output: KeyError: 2

#my_set.remove(2)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@  we can remove and return an item using the pop() method.

Set being unordered, there is no way of determining which item will be popped. It is completely arbitrary.

We can also remove all items from a set using clear(). """)
print("""  # initialize my_set
# Output: set of unique elements
my_set = set("HelloWorld")
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())

# pop another element
# Output: random element
my_set.pop()
print(my_set)

# clear my_set
#Output: set()
my_set.clear()
print(my_set) """)


# initialize my_set
# Output: set of unique elements
my_set = set("HelloWorld")
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())

# pop another element
# Output: random element
my_set.pop()
print(my_set)

# clear my_set
#Output: set()
my_set.clear()
print(my_set)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Set Union ")
print(""" # initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)  """)
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Set Intersection ")
print("""  # initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
# Output: {4, 5}
print(A & B) """)

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
# Output: {4, 5}
print(A & B)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@   ")
print("""   """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Set Difference  ")
print(""" # initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
# Output: {1, 2, 3}
print(A - B)  """)

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
# Output: {1, 2, 3}
print(A - B)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Set Symmetric Difference  ")
print("""  # initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B) """)

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Set Membership Test ")
print(""" # initialize my_set
my_set = set("apple")

# check if 'a' is present
# Output: True
print('a' in my_set)

# check if 'p' is present
# Output: False
print('p' not in my_set)  """)

# initialize my_set
my_set = set("apple")

# check if 'a' is present
# Output: True
print('a' in my_set)

# check if 'p' is present
# Output: False
print('p' not in my_set)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Iterating Through a Set ")
print("""  for letter in set("apple"):
 print(letter)""")

for letter in set("apple"):
    print(letter)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
# 2886 bueno Frozenset, como set pero no cambia y diferentes metodos
print("""@  Frozenset
Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. While tuples are immutable lists, frozensets are immutable sets.

Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, frozensets are hashable and can be used as keys to a dictionary.

Frozensets can be created using the function frozenset().

This datatype supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(), symmetric_difference() and union(). Being immutable it does not have method that add or remove elements.

 """)
print(""" # initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
 A.isdisjoint(B)
A.difference(B)
A | B
A.add(3)""")

# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

A.isdisjoint(B)
A.difference(B)
A | B
#A.add(3)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  How to create a dictionary? ")
print("""# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])   """)
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ How to access elements from a dictionary?  ")
print("""my_dict = {'name':'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# my_dict.get('address')
# my_dict['address']   """)

my_dict = {'name':'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# my_dict.get('address')
# my_dict['address']

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
# 2984 bueno dictionary,get, pop, popitem, del

print("@  How to change or add elements in a dictionary? ")
print(""" my_dict = {'name':'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'  

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)  """)

my_dict = {'name':'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ How to delete or remove elements from a dictionary?  ")
print("""  # create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}  

# remove a particular item
# Output: 16
print(squares.pop(4))  

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item
# Output: (1, 1)
print(squares.popitem())

# Output: {2: 4, 3: 9, 5: 25}
print(squares)

# delete a particular item
del squares[5]  

# Output: {2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

# Throws Error
# print(squares) """)

# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}

# remove a particular item
# Output: 16
print(squares.pop(4))

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item
# Output: (1, 1)
print(squares.popitem())

# Output: {2: 4, 3: 9, 5: 25}
print(squares)

# delete a particular item
#del squares[5]

# Output: {2: 4, 3: 9}
#print(squares)

# remove all items
#squares.clear()

# Output: {}
#print(squares)

# delete the dictionary itself
#del squares

# Throws Error
# print(squares)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Dictionary Methods  ")
print("""marks = {}.fromkeys(['Math','English','Science'], 0)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
print(marks)

for item in marks.items():
    print(item)

# Output: ['English', 'Math', 'Science']
list(sorted(marks.keys()))   """)
# 3107 bueno  crear dict automatico
marks = {}.fromkeys(['Math','English','Science'], 0)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
print(marks)

for item in marks.items():
    print(item)

# Output: ['English', 'Math', 'Science']
list(sorted(marks.keys()))

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Dictionary Comprehension ")
print("""  squares = {x: x*x for x in range(6)}

# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares) """)

squares = {x: x*x for x in range(6)}

# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Iterating Through a Dictionary ")
print("""  squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i]) """)
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Dictionary Membership Test ")
print(""" squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: True
print(1 in squares)

# Output: True
print(2 not in squares)

# membership tests for key only not value
# Output: False
print(49 in squares)  """)

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: True
print(1 in squares)

# Output: True
print(2 not in squares)

# membership tests for key only not value
# Output: False
print(49 in squares)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ built-in functions to work with dictionary  ")
print("""  squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: 5
print(len(squares))

# Output: [1, 3, 5, 7, 9]
print(sorted(squares)) """)

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: 5
print(len(squares))

# Output: [1, 3, 5, 7, 9]
print(sorted(squares))

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ What is Nested Dictionary in Python?
In Python, a nested dictionary is a dictionary inside a dictionary. It's a collection of dictionaries into one single dictionary.

nested_dict = { 'dictA': {'key_1': 'value_1'},
                'dictB': {'key_2': 'value_2'}}
Here, the nested_dict is a nested dictionary with the dictionary dictA and dictB. They are two dictionary each having own key and value. 
 
 Create a Nested Dictionary""")
print(""" people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people)  """)

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
# 3227 bueno nested dictionary es como un bbdd/matriz
print("@ Access elements of a Nested Dictionary  ")
print("""  people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex']) """)

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Add element to a Nested Dictionary  ")
print("""  people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

people[3] = {}

people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'

print(people[3]) """)

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

people[3] = {}

people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'

print(people[3])

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@   Example 4: Add another dictionary to the nested dictionary")
print(""" people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}}

people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
print(people[4])  """)

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}}

people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
print(people[4])
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Delete elements from a Nested Dictionary  ")
print(""" people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}

del people[3]['married']
del people[4]['married']

print(people[3])
print(people[4])  """)

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}

del people[3]['married']
del people[4]['married']

print(people[3])
print(people[4])

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Example 6: How to delete dictionary from a nested dictionary?  ")
print("""  people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}

del people[3], people[4]
print(people) """)

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}

del people[3], people[4]
print(people)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Example 7: How to iterate through a Nested dictionary?  ")
print(""" people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)
    
    for key in p_info:
        print(key + ':', p_info[key])  """)

people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

# 3227 y 3360 bueno nested dictionary es como un bbdd/matriz
for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)

    for key in p_info:
        print(key + ':', p_info[key])

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
# 3372 bueno no arrays sino listas, real arrays con numpy

print("""@ However, in Python, there is no native array data structure. So, we use Python lists instead of an array.

Note: If you want to create real arrays in Python, you need to use NumPy's array data structure. For mathematical problems, NumPy Array is more efficient.

  
  Example 1: How to create an array in Python?
""")
print(""" arr = [10, 20, 30, 40, 50]
  """)

arr = [10, 20, 30, 40, 50]


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Example 2: Accessing elements of array using indexing ")
print("""  arr = [10, 20, 30, 40, 50]
print(arr[0])
print(arr[1])
print(arr[2]) """)

arr = [10, 20, 30, 40, 50]
print(arr[0])
print(arr[1])
print(arr[2])

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Example 3: Accessing elements of array using negative indexing ")
print("""  arr = [10, 20, 30, 40, 50]
print(arr[-1])
print(arr[-2]) """)
arr = [10, 20, 30, 40, 50]
print(arr[-1])
print(arr[-2])
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Example 4: Find length of an array using len()  ")
print(""" brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
num_brands = len(brands)
print(num_brands)  """)

brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
num_brands = len(brands)
print(num_brands)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Example 5: Adding an element in an array using append() ")
print("""  add = ['a', 'b', 'c']
add.append('d')
print(add) """)

add = ['a', 'b', 'c']
add.append('d')
print(add)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Example 6: Removing elements of an array using del, remove() and pop() ")
print("""  colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
del color[4]
colors.remove("blue")
colors.pop(3)
print(color) """)

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
del colors[4]
colors.remove("blue")
colors.pop(3)
print(colors)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Example 7: Modifying elements of an array using Indexing  ")
print(""" fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
fruits[1] = "Pineapple"
fruits[-1] = "Guava"
print(fruits)  """)

fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
fruits[1] = "Pineapple"
fruits[-1] = "Guava"
print(fruits)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Example 8: Concatenating two arrays using + operator ")
print(""" concat = [1, 2, 3]
concat += [4,5,6]
print(concat)  """)

concat = [1, 2, 3]
concat += [4,5,6]
print(concat)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Example 8: Repeating elements in array using * operator ")
print(""" repeat = ["a"]
repeat = repeat * 5
print(repeat)  """)
repeat = ["a"]
repeat = repeat * 5
print(repeat)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Example 9: Slicing an array using Indexing  ")
print(""" fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits[1:4])
print(fruits[ : 3])
print(fruits[-4:])
print(fruits[-3:-1])  """)

fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits[1:4])
print(fruits[ : 3])
print(fruits[-4:])
print(fruits[-3:-1])

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
# 3524 bueno 2D array and matrix y crear dynamic
print("@  Example 10: Create a two-dimensional array using lists ")
print("""  multd = [[1,2], [3,4], [5,6], [7,8]]
print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0]) """)


multd = [[1,2], [3,4], [5,6], [7,8]]
print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0])
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Example 1: Create a matrix in python  ")
print("""# a is 2-D matrix with integers
a = [['Roy',80,75,85,90,95],
     ['John',75,80,75,85,100],
     ['Dave',80,80,80,90,95]]

#b is a nested list but not a matrix
b= [['Roy',80,75,85,90,95],
    ['John',75,80,75],
    ['Dave',80,80,80,90,95]]   """)

# a is 2-D matrix with integers
a = [['Roy',80,75,85,90,95],
     ['John',75,80,75,85,100],
     ['Dave',80,80,80,90,95]]

#b is a nested list but not a matrix
b = [['Roy',80,75,85,90,95],
    ['John',75,80,75],
    ['Dave',80,80,80,90,95]]

print(a)
print(b)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@ Example 2: Create a dynamic matrix using for loop in python  ")
print(""" n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m
print(a)  """)
n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m
print(a)


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("@  Example 3: Create a matrix using numpy in pyhton ")
print(""" from numpy import * 

x = range(16)

x = reshape(x,(4,4)) 

print(x)   """)

from numpy import *
#import numpy
x = range(16)

x = reshape(x,(4,4))

print(x)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@Example 4: Accessing elements of the matrix in python by using list index
   """)
print(""" # a is 2-D matrix with integers
a = [['Roy',80,75,85,90,95],
     ['John',75,80,75,85,100],
     ['Dave',80,80,80,90,95]]

print(a[0])

print(a[0][1])

print(a[1][2])  """)
# a is 2-D matrix with integers
a = [['Roy',80,75,85,90,95],
     ['John',75,80,75,85,100],
     ['Dave',80,80,80,90,95]]

print(a[0])

print(a[0][1])

print(a[1][2])

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Example 5: Accessing elements of the matrix in python by using negative list index
  """)
print(""" a = [['Roy',80,75,85,90,95],
     ['John',75,80,75,85,100],
     ['Dave',80,80,80,90,95]]
    
print(a[-1]) 
    
print(a[-1][-2]) 

print(a[-2][-3])  """)

a = [['Roy', 80, 75, 85, 90, 95],
     ['John', 75, 80, 75, 85, 100],
     ['Dave', 80, 80, 80, 90, 95]]

print(a[-1])

print(a[-1][-2])

print(a[-2][-3])
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Why and how to slice matrix in python?
In the students matrix we store marks for different subjects of three students. Suppose we want to access marks of Science for all 3 students, here we will be using slicing to get the sub elements of the matrix. In python slicing is done using colon(:) with a syntax (start:end:increment) but for matrix we have to do it using numpy library.

We use slicing to get specific sets of sub-elements from it, without any long, drawn out for loops.
 
 Example 6: Slicing a matrix in python using colon(:)  and numpy
 """)
print("""from numpy import *

a = array([['Roy',80,75,85,90,95],
           ['John',75,80,75,85,100],
           ['Dave',80,80,80,90,95]])

print(a[:3,[0,1]])   """)

from numpy import *

a = array([['Roy',80,75,85,90,95],
           ['John',75,80,75,85,100],
           ['Dave',80,80,80,90,95]])

print(a[:3,[0,1]])
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Example 7: Change elements of a matrix in python
  """)
print("""  a = [['Roy',80,75,85,90,95],
     ['John',75,80,75,85,100],
     ['Dave',80,80,80,90,95]]

b=a[0]
print(b)

b[1]=75
print(b)

a[2]=['Sam',82,79,88,97,99]
print(a)

a[0][4]=95
print(a) """)
a = [['Roy',80,75,85,90,95],
     ['John',75,80,75,85,100],
     ['Dave',80,80,80,90,95]]

b=a[0]
print(b)

b[1]=75
print(b)

a[2]=['Sam',82,79,88,97,99]
print(a)

a[0][4]=95
print(a)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Example 8: Adding a new row in the matrix in python using append()
  """)
print(""" from numpy import *

a = array([['Roy',80,75,85,90,95],
           ['John',75,80,75,85,100],
           ['Dave',80,80,80,90,95]])

a= append(a,[['Sam',82,79,88,97,99]],0)

    //here 0 is axis that represents the dimensions where 0 stands for row and 1 stands for column

print(a)  """)

from numpy import *

a = array([['Roy',80,75,85,90,95],
           ['John',75,80,75,85,100],
           ['Dave',80,80,80,90,95]])

a= append(a,[['Sam',82,79,88,97,99]],0)

#	//here 0 is axis that represents the dimensions where 0 stands for row and 1 stands for column

print(a)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@Example 9: Add a new column in the matrix for economics marks using insert().
   """)
print("""  from numpy import * 

a = array([['Roy',80,75,85,90,95],
      ['John',75,80,75,85,100],
      ['Dave',80,80,80,90,95]]) 

a= insert(a,[6],[[73],[80],[85]],axis=1) 
//here axis represents the dimensions where 0 stands for row and 1 stands for column 

print(a)  """)
from numpy import *

a = array([['Roy',80,75,85,90,95],
      ['John',75,80,75,85,100],
      ['Dave',80,80,80,90,95]])

a= insert(a,[6],[[73],[80],[85]],axis=1)
#//here axis represents the dimensions where 0 stands for row and 1 stands for column

print(a)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@Example 10: Add a row in the matrix in python using +
   """)
print(""" a=[['Roy',80,75,85,90,95],
    ['John',75,80,75,85,100],
    ['Dave',80,80,80,90,95]]

a= a+ [['Sam',82,79,88,97,99]]

print(a)  """)
a=[['Roy',80,75,85,90,95],
    ['John',75,80,75,85,100],
    ['Dave',80,80,80,90,95]]

a= a+ [['Sam',82,79,88,97,99]]

print(a)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Example 11: Delete a row of a matrix in python using delete from numpy
  """)
print(""" from numpy import *

a = array([['Roy',80,75,85,90,95],
      ['John',75,80,75,85,100],
      ['Dave',80,80,80,90,95]])

a= delete(a,[1],0)

print(a)  """)
from numpy import *

a = array([['Roy',80,75,85,90,95],
      ['John',75,80,75,85,100],
      ['Dave',80,80,80,90,95]])

a= delete(a,[1],0)

print(a)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Example 12: Delete columns of a matrix in python using delete from numpy
  """)
print(""" from numpy import *

a = array([['Roy',80,75,85,90,95],
      ['John',75,80,75,85,100],
      ['Dave',80,80,80,90,95]])

a= delete(a, s_[1::2], 1)

print(a)  """)


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ List Comprehension vs For Loop in Python
 Suppose, we want to separate the letters of the word human and add the letters as items of a list. The first thing that comes in mind would be using for loop.

Example 1: Iterating through a string Using for Loop """)
print(""" h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)  """)
h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ However, Python has an easier way to solve this issue using List Comprehension. List comprehension is an elegant way to define and create lists based on existing lists.

Let’s see how the above program can be written using list comprehensions.

Example 2: Iterating through a string Using List Comprehension  """)
# 3885 bueno Iterating through a string Using List Comprehension
print("""  h_letters = [ letter for letter in 'human' ]
print( h_letters) """)
h_letters = [ letter for letter in 'human' ]
print( h_letters)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ List Comprehensions vs Lambda functions
List comprehensions aren’t the only way to work on lists. Various built-in functions and lambda functions can create and modify lists in less lines of code.

Example 3: Using Lambda functions inside List   """)
print(""" h_letters = list(map(lambda x: x, 'human'))
  """)
h_letters = list(map(lambda x: x, 'human'))
print( h_letters)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Conditionals in List Comprehension
  List comprehensions can utilize conditional statement to modify existing list (or other tuples). We will create list that uses mathematical operators, integers, and range().

Example 4: Using if with List Comprehension""")
print(""" number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)  """)

number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@  Example 5: Nested IF with List Comprehension
 """)
print("""  num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list) """)
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Example 6: if...else With List Comprehension
  """)
print("""  obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj) """)
# 3941 bueno if, else y loops en list comprension obj = ["Even" if i%2==0 else "Odd" for i in range(10)]

obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@Nested Loops in List Comprehension
Suppose, we need to compute transpose of a matrix which requires nested for loop. Let’s see how it is done using normal for loop first.

Example 7: Transpose of Matrix using Nested Loops   """)
print("""
LA LINEA matrix = la he ñadido yo que daba error

matrix = [[1, 2],[3,4],[5,6],[7,8]]
transposed = []

for i in range(2):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
        transposed.append(transposed_row)

print(transposed)   """)
matrix = [[1, 2],[3,4],[5,6],[7,8]]
transposed = []

for i in range(2):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
        transposed.append(transposed_row)

print(transposed)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ The above code usestwo for loops to find transpose of a matrix.

We can also perform nested iteration inside a list comprehension. In this section, we will find transpose of a matrix using nested loop inside list comprehension.

Example 8: Transpose of a Matrix using List Comprehension  """)
print(""" matrix = [[1, 2],[3,4],[5,6],[7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)  """)
matrix = [[1, 2],[3,4],[5,6],[7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ How to open a file?
  >>> f = open("test.txt")    # open file in current directory
>>> f = open("C:/Python33/README.txt")  # specifying full path""")
print(""" 
 
We can specify the mode while opening a file. In mode, we specify whether we want to read 'r', write 'w' or append 'a' to the file. We also specify if we want to open the file in text mode or binary mode.

The default is reading in text mode. In this mode, we get strings when reading from the file.

On the other hand, binary mode returns bytes and this is the mode to be used when dealing with non-text files like image or exe files.

 f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode """)
# 4013 bueno ficheros
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ How to close a file Using Python?
When we are done with operations to the file, we need to properly close the file.

Closing a file will free up the resources that were tied with the file and is done using Python close() method.

Python has a garbage collector to clean up unreferenced objects but, we must not rely on it to close the file.  """)
print("""  f = open("test.txt",encoding = 'utf-8')
# perform file operations
f.close() """)


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@This method is not entirely safe. If an exception occurs when we are performing some operation with the file, the code exits without closing the file.

A safer way is to use a try...finally block.   """)
print("""  try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close() """)


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ This way, we are guaranteed that the file is properly closed even if an exception is raised, causing program flow to stop.

The best way to do this is using the with statement. This ensures that the file is closed when the block inside with is exited.

We don't need to explicitly call the close() method. It is done internally.

with open("test.txt",encoding = 'utf-8') as f:
   # perform file operations  """)
print("""   """)


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ How to write to File Using Python?
 In order to write into a file in Python, we need to open it in write 'w', append 'a' or exclusive creation 'x' mode.

We need to be careful with the 'w' mode as it will overwrite into the file if it already exists. All previous data are erased.

Writing a string or sequence of bytes (for binary files) is done using write() method. This method returns the number of characters written to the file. 

with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")""")
print("""   """)


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ How to read files in Python?
  """)
print(""" To read a file in Python, we must open the file in reading mode.

There are various methods available for this purpose. We can use the read(size) method to read in size number of data. If size parameter is not specified, it reads and returns up to the end of the file.

>>> f = open("test.txt",'r',encoding = 'utf-8')
>>> f.read(4)    # read the first 4 data
'This'

>>> f.read(4)    # read the next 4 data
' is '

>>> f.read()     # read in the rest till end of file
'my first file\nThis file\ncontains three lines\n'

>>> f.read()  # further reading returns empty sting
''
We can see that, the read() method returns newline as '\n'. Once the end of file is reached, we get empty string on further reading.

We can change our current file cursor (position) using the seek() method. Similarly, the tell() method returns our current position (in number of bytes).

>>> f.tell()    # get the current file position
56

>>> f.seek(0)   # bring file cursor to initial position
0

>>> print(f.read())  # read the entire file
This is my first file
This file
contains three lines
We can read a file line-by-line using a for loop. This is both efficient and fast.

>>> for line in f:
...     print(line, end = '')
...
This is my first file
This file
contains three lines
The lines in file itself has a newline character '\n'.

Moreover, the print() end parameter to avoid two newlines when printing.

Alternately, we can use readline() method to read individual lines of a file. This method reads a file till the newline, including the newline character.

>>> f.readline()
'This is my first file\n'

>>> f.readline()
'This file\n'

>>> f.readline()
'contains three lines\n'

>>> f.readline()
''
Lastly, the readlines() method returns a list of remaining lines of the entire file. All these reading method return empty values when end of file (EOF) is reached.

>>> f.readlines()
['This is my first file\n', 'This file\n', 'contains three lines\n']  """)


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ What is Directory in Python?
If there are a large number of files to handle in your Python program, you can arrange your code within different directories to make things more manageable.

A directory or folder is a collection of files and sub directories. Python has the os module, which provides us with many useful methods to work with directories (and files as well).  """)
print("""   """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@Get Current Directory
We can get the present working directory using the getcwd() method.   """)
print("""
import os
os.getcwd()
os.getcwdb()
print(os.getcwd())
print(os.getcwdb())
os.chdir('..')
print(os.getcwd())
os.chdir('programiz-curso')
print(os.getcwd())
print(os.listdir('/'))
os.mkdir('/tmp/test')
print(os.listdir('/tmp/test'))
os.rename('/tmp/test','/tmp/new_one')
print(os.listdir('/tmp/new_one'))
os.rmdir('/tmp/new_one')
#However, note that rmdir() method can only remove empty directories
import shutil
os.mkdir('/tmp/test')
shutil.rmtree('/tmp/test')
 """)
import os
os.getcwd()
os.getcwdb()
print(os.getcwd())
print(os.getcwdb())
os.chdir('..')
print(os.getcwd())
#os.chdir('tutorial')
print(os.getcwd())
print(os.listdir('/'))
os.mkdir('/tmp/test')
print(os.listdir('/tmp/test'))
os.rename('/tmp/test','/tmp/new_one')
print(os.listdir('/tmp/new_one'))
os.rmdir('/tmp/new_one')
#However, note that rmdir() method can only remove empty directories
import shutil
os.mkdir('/tmp/test')
shutil.rmtree('/tmp/test')

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Python Errors and Built-in Exceptions
 
 Errors can also occur at runtime and these are called exceptions. They occur, for example, when a file we try to open does not exist (FileNotFoundError), dividing a number by zero (ZeroDivisionError), module we try to import is not found (ImportError) etc.

Whenever these type of runtime error occur, Python creates an exception object. If not handled properly, it prints a traceback to that error along with some details about why that error occurred. """)
print("""Illegal operations can raise exceptions. There are plenty of built-in exceptions in Python that are raised when corresponding errors occur. We can view all the built-in exceptions using the local() built-in functions as follows.
locals()['__builtins__'] """)
print(locals()['__builtins__'])

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ What are exceptions in Python?
Python has many built-in exceptions which forces your program to output an error when something in it goes wrong.

When these exceptions occur, it causes the current process to stop and passes it to the calling process until it is handled. 
If not handled, our program will crash.

For example, if function A calls function B which in turn calls function C and an exception occurs in function C. 
If it is not handled in C, the exception passes to B and then to A.

If never handled, an error message is spit out and our program come to a sudden, unexpected halt.  """)
print("""   """)


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Catching Exceptions in Python
In Python, exceptions can be handled using a try statement.

A critical operation which can raise exception is placed inside the try clause and the code that handles exception is written in except clause.

It is up to us, what operations we perform once we have caught the exception. Here is a simple example.  """)
print(""" # import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)  """)
# 4267 errores y exceptions

# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)

for entrada in randomList:
    try:
        print("The entrada is", entrada)
        reciproco = 1/int(entrada)
        print("The reciprocal of", entrada, "is", reciproco)
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Catching Specific Exceptions in Python
In the above example, we did not mention any exception in the except clause.

This is not a good programming practice as it will catch all exceptions and handle every case in the same way. 
We can specify which exceptions an except clause will catch.

A try clause can have any number of except clause to handle them differently but only one 
will be executed in case an exception occurs.

We can use a tuple of values to specify multiple exceptions in an except clause. Here is an example pseudo code.  """)
print("""  try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass """)

try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Raising Exceptions
In Python programming, exceptions are raised when corresponding errors occur at run time, but we can forcefully raise 
it using the keyword raise.

We can also optionally pass in value to the exception to clarify why that exception was raised.  """)
print("""  >>> raise KeyboardInterrupt
Traceback (most recent call last):
...
KeyboardInterrupt

>>> raise MemoryError("This is an argument")
Traceback (most recent call last):
...
MemoryError: This is an argument

>>> try:
...     a = int(input("Enter a positive integer: "))
...     if a <= 0:
...         raise ValueError("That is not a positive number!")
... except ValueError as ve:
...     print(ve)
...    
Enter a positive integer: -2
That is not a positive number! """)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ try...finally
The try statement in Python can have an optional finally clause. This clause is executed no matter what, 
and is generally used to release external resources.

For example, we may be connected to a remote data center through the network or working with a file 
or working with a Graphical User Interface (GUI).

In all these circumstances, we must clean up the resource once used, whether it was successful or not. 
These actions (closing a file, GUI or disconnecting from network) are performed in the finally clause to guarantee execution.

Here is an example of file operations to illustrate this.  """)
print("""  try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close() """)
# 4382 try, raise, finally, except (estan en builtins.pyi):  errores y exceptions sys.exc_info()[0]

try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
except:
    print("except: Error con fichero")
finally:
    if ValueError == '0':
        f.close()
        raise ValueError("finally: raise: Ya cerre el fichero")
    else:
        print("finally: Error con fichero")

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Python Custom Exceptions

 However, sometimes you may need to create custom exceptions that serves your purpose.

In Python, users can define such exceptions by creating a new class. This exception class has to be derived, either directly or indirectly, from Exception class. Most of the built-in exceptions are also derived form this class. """)
print(""" class CustomError(Exception):
    pass
# raise CustomError("An error occurred")  """)
class CustomError(Exception):
    pass
# raise CustomError("An error occurred")
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Example: User-Defined Exception in Python
 
  In this example, we will illustrate how user-defined exceptions can be used in a program to raise and catch errors.

This program will ask the user to enter a number until they guess a stored number correctly. To help them figure it out, hint is provided whether their guess is greater than or less than the stored number.""")
print(""" # define Python user-defined exceptions
class Error(Exception):
   \"\"\"Base class for other exceptions\"\"\"
   pass

class ValueTooSmallError(Error):
   \"\"\"Raised when the input value is too small\"\"\"
   pass

class ValueTooLargeError(Error):
   \"\"\"Raised when the input value is too large\"\"\"
   pass

# our main program
# user guesses a number until he/she gets it right

# you need to guess this number
number = 10

while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()

print("Congratulations! You guessed it correctly.")  """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Example 1: Creating Class and Object in Python
  """)
print("""class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))   """)

class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@Example 2 : Creating Methods in Python
   """)
print(""" class Parrot:
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())  """)

class Parrot:

    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)


# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())
class Parrot:

    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)


# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Example 3: Use of Inheritance in Python
  """)
print(""" # parent class
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

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()  """)


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


peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Example 5: Using Polymorphism in Python
  """)
print(""" class Parrot:

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
flying_test(peggy)  """)


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


# instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Defining a Class in Python
  """)
print(""" class MyClass:
    "This is my second class"
    a = 10
    def func(self):
        print('Hello')

# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

# Output: 'This is my second class'
print(MyClass.__doc__)  """)

class MyClass:
    "This is my second class"
    a = 10
    def func(self):
        print('Hello')

# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

# Output: 'This is my second class'
print(MyClass.__doc__)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Creating an Object in Python
  """)
print(""" class MyClass:
    "This is my second class"
    a = 10
    def func(self):
        print('Hello')

# create a new MyClass
ob = MyClass()

# Output: <function MyClass.func at 0x000000000335B0D0>
print(MyClass.func)

# Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
print(ob.func)

# Calling function func()
# Output: Hello
ob.func()  """)
class MyClass:
    "This is my second class"
    a = 10
    def func(self):
        print('Hello')

# create a new MyClass
ob = MyClass()

# Output: <function MyClass.func at 0x000000000335B0D0>
print(MyClass.func)

# Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
print(ob.func)

# Calling function func()
# Output: Hello
ob.func()

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Constructors in Python
 
  An interesting thing to note in the above step is that attributes of an object can be created on the fly. We created a new attribute attr for object c2 and we read it as well. But this did not create that attribute for object c1.

""")
print(""" class ComplexNumber:
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
c1.attr  """)

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
#c1.attr
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Deleting Attributes and Objects
  """)
print(""">>> c1 = ComplexNumber(2,3)
>>> del c1.imag
>>> c1.getData()
Traceback (most recent call last):
...
AttributeError: 'ComplexNumber' object has no attribute 'imag'

>>> del ComplexNumber.getData
>>> c1.getData()
Traceback (most recent call last):
...
AttributeError: 'ComplexNumber' object has no attribute 'getData'
   """)


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@We can even delete the object itself, using the del statement.

   """)
print(""">>> c1 = ComplexNumber(1,3)
>>> del c1
>>> c1
Traceback (most recent call last):
...
NameError: name 'c1' is not defined
   
 Actually, it is more complicated than that. When we do c1 = ComplexNumber(1,3), a new instance object is created in memory and the name c1 binds with it.

On the command del c1, this binding is removed and the name c1 is deleted from the corresponding namespace. The object however continues to exist in memory and if no other name is bound to it, it is later automatically destroyed.

This automatic destruction of unreferenced objects in Python is also called garbage collection.  """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
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
        self.sides = [float(input("Enter side "+format(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])


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
#t.inputSides()
t.sides[0] = 3.0
t.sides[1] = 5.0
t.sides[2] = 4.0

t.dispSides()
t.findArea()
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@Method Overriding in Python
  
  In the above example, notice that __init__() method was defined in both classes, Triangle as well Polygon. When this happens, the method in the derived class overrides that in the base class. This is to say, __init__() in Triangle gets preference over the same in Polygon.

Generally when overriding a base method, we tend to extend the definition rather than simply replace it. The same is being done by calling the method in base class from the one in derived class (calling Polygon.__init__() from __init__() in Triangle).

A better option would be to use the built-in function super(). So, super().__init__(3) is equivalent to Polygon.__init__(self,3) and is preferred. You can learn more about the super() function in Python.

 """)
print("""    super().__init__(3)
             equivaalente and better than
    Polygon.__init__(self,3)     """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Two built-in functions isinstance() and issubclass() are used to check inheritances. Function isinstance() returns True if the object is an instance of the class or other classes derived from it. Each and every class in Python inherits from the base class object.
  """)
print("isinstance(t,Triangle)")
print (isinstance(t,Triangle))
print("isinstance(t,Polygon)")
print (isinstance(t,Polygon))
print("isinstance(t,int)")
print (isinstance(t,int))
print("isinstance(t,object)")
print (isinstance(t,object))
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@   """)
print("""   """)
print("issubclass(Polygon,Triangle)")
print (issubclass(Polygon,Triangle))
print("issubclass(Triangle,Polygon)")
print (issubclass(Triangle,Polygon))
print("issubclass(bool,int)")
print (issubclass(bool,int))
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
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
print(issubclass(list,object))

# Output: True
print(isinstance(5.5,object))

# Output: True
print(isinstance("Hello",object))
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Method Resolution Order (MRO)
  So, in the above example of MultiDerived class the search order is [MultiDerived, Base1, Base2, object]. This order is also called linearization of MultiDerived class and the set of rules used to find this order is called Method Resolution Order (MRO).

MRO must prevent local precedence ordering and also provide monotonicity. It ensures that a class always appears before its parents and in case of multiple parents, the order is same as tuple of base classes.

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
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
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

class A(X,Y): pass
class B(Y,Z): pass

class M(B,A,Z): pass

# Output:
# [<class '__main__.M'>, <class '__main__.B'>,
# <class '__main__.A'>, <class '__main__.X'>,
# <class '__main__.Y'>, <class '__main__.Z'>,
# <class 'object'>]

print(M.mro())
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ What is operator overloading in Python?

Python operators work for built-in classes. But same operator behaves differently with different types. For example, the + operator will, perform arithmetic addition on two numbers, merge two lists and concatenate two strings.

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
To overload the + sign, we will need to implement __add__() function in the class. With great power comes great responsibility. We can do whatever we like, inside this function. But it is sensible to return a Point object of the coordinate sum.

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

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ What are iterators in Python?
Iterators are everywhere in Python. They are elegantly implemented within for loops, comprehensions, generators etc. but hidden in plain sight.

Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element at a time.

Technically speaking, Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.

An object is called iterable if we can get an iterator from it. Most of built-in containers in Python like: list, tuple, string etc. are iterables.

The iter() function (which in turn calls the __iter__() method) returns an iterator from them.

  """)
print("""   """)


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@Iterating Through an Iterator in Python

 We use the next() function to manually iterate through all the items of an iterator. When we reach the end and there is no more data to be returned, it will raise StopIteration. Following is an example.
 """)
print("""# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

## iterate through it using next() 

#prints 4
print(next(my_iter))

#prints 7
print(next(my_iter))

## next(obj) is same as obj.__next__()

#prints 0
print(my_iter.__next__())

#prints 3
print(my_iter.__next__())

## This will raise error, no items left
next(my_iter)   """)
# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

## iterate through it using next()

#prints 4
print(next(my_iter))

#prints 7
print(next(my_iter))

## next(obj) is same as obj.__next__()

#prints 0
print(my_iter.__next__())

#prints 3
print(my_iter.__next__())

print("""# This will raise error, no items left
next(my_iter)""")
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""

Technically speaking, Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.

An object is called iterable if we can get an iterator from it. Most of built-in containers in Python like: list, tuple, string etc. are iterables.

The iter() function (which in turn calls the __iter__() method) returns an iterator from them.""")
print("""   """)


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Iterating Through an Iterator in Python
We use the next() function to manually iterate through all the items of an iterator. When we reach the end and there is no more data to be returned, it will raise StopIteration. Following is an example.  """)
print(""" # define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

## iterate through it using next() 

#prints 4
print(next(my_iter))

#prints 7
print(next(my_iter))

## next(obj) is same as obj.__next__()

#prints 0
print(my_iter.__next__())

#prints 3
print(my_iter.__next__())

## This will raise error, no items left
next(my_iter)  """)

# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

## iterate through it using next()

#prints 4
print(next(my_iter))

#prints 7
print(next(my_iter))

## next(obj) is same as obj.__next__()

#prints 0
print(my_iter.__next__())

#prints 3
print(my_iter.__next__())

## This will raise error, no items left
#next(my_iter)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ A more elegant way of automatically iterating is by using the for loop. Using this, we can iterate over any object that can return an iterator, for example list, string, file etc.  """)
print("""   """)
mi_lista = [5, 7, 0, 3]
for element in mi_lista:
    print(element)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ In fact the for loop can iterate over any iterable
 Is actually implemented as.

 """)
print(""" # create an iterator object from that iterable
iter_obj = iter(iterable)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break  """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Building Your Own Iterator in Python
Building an iterator from scratch is easy in Python. We just have to implement the methods __iter__() and __next__().

The __iter__() method returns the iterator object itself. If required, some initialization can be performed.

The __next__() method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise StopIteration.

Here, we show an example that will give us next power of 2 in each iteration. Power exponent starts from zero up to a user set number.

  """)
print(""" lass PowTwo:
    Class to implement an iterator
    of powers of two

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

a = PowTwo(4)
i = iter(a)
print(next(i))
print(next(i))
#We can also use a for loop to iterate over our iterator class.
for i in PowTwo(5):
    print(i)  """)

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

a = PowTwo(4)
i = iter(a)
print(next(i))
print(next(i))
#We can also use a for loop to iterate over our iterator class.
for i in PowTwo(5):
    print(i)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@  Python Infinite Iterators
It is not necessary that the item in an iterator object has to exhaust. There can be infinite iterators (which never ends). We must be careful when handling such iterator.

Here is a simple example to demonstrate infinite iterators.

The built-in function iter() can be called with two arguments where the first argument must be a callable object (function) and second is the sentinel. The iterator calls this function until the returned value is equal to the sentinel. """)
print("""print(int())
inf = iter(int,1)
print(next(inf))   """)
print(int())
inf = iter(int,1)
print(next(inf))

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ We can see that the int() function always returns 0. So passing it as iter(int,1) will return an iterator that calls int() until the returned value equals 1. This never happens and we get an infinite iterator.

We can also built our own infinite iterators. The following iterator will, theoretically, return all the odd numbers.

  """)
print(""" class InfIter:
    Infinite iterator to return all
        odd numbers

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num
a = iter(InfIter())
print(next(a))
  
 Be careful to include a terminating condition, when iterating over these type of infinite iterators.

 """)

class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num
a = iter(InfIter())
print(next(a))
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ There's an easier way to create iterators in Python: Python generators using yield.
  Python generators are a simple way of creating iterators
  
  How to create a generator in Python?
It is fairly simple to create a generator in Python. It is as easy as defining a normal function with yield statement instead of a return statement.

If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. Both yield and return will return some value from a function.

The difference is that, while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls.""")
print("""   """)

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Differences between Generator function and a Normal function
Here is how a generator function differs from a normal function.

Generator function contains one or more yield statement.
When called, it returns an object (iterator) but does not start execution immediately.
Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
Once the function yields, the function is paused and the control is transferred to the caller.
Local variables and their states are remembered between successive calls.
Finally, when the function terminates, StopIteration is raised automatically on further calls.
Here is an example to illustrate all of the points stated above. We have a generator function named my_gen() with several yield statements.

  """)
print(""" 
  def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# It returns an object but does not start execution immediately.
a = my_gen()
# We can iterate through the items using next().
print(next(a))
# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and theirs states are remembered between successive calls.
print(next(a))
print(next(a))

  To restart the process we need to create another generator object using something like a = my_gen().

  """)


# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# It returns an object but does not start execution immediately.
a = my_gen()
# We can iterate through the items using next().
print(next(a))
# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and theirs states are remembered between successive calls.
print(next(a))
print(next(a))

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ One final thing to note is that we can use generators with for loops directly.

This is because, a for loop takes an iterator and iterates over it using next() function. It automatically ends when StopIteration is raised. Check here to know how a for loop is actually implemented in Python.  """)
print(""" f my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# Using for loop
for item in my_gen():
    print(item)    
  """)


# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Python Generators with a Loop
  """)
print(""" def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h
for char in rev_str("hello"):
     print(char)

       In this example, we use range() function to get the index in reverse order using the for loop.

It turns out that this generator function not only works with string, but also with other kind of iterables like list, tuple etc.""")


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h
for char in rev_str("hello"):
    print(char)

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Python Generator Expression
Simple generators can be easily created on the fly using generator expressions. It makes building generators easy.

Same as lambda function creates an anonymous function, generator expression creates an anonymous generator function.

  """)
print(""" # Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
print([x**2 for x in my_list])

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
print((x**2 for x in my_list))  """)
# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
print([x ** 2 for x in my_list])

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
print((x ** 2 for x in my_list))
########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@  We can see above that the generator expression did not produce the required result immediately. Instead, it returned a generator object with produces items on demand.

 """)
print(""" # Intialize the list
my_list = [1, 3, 6, 10]

a = (x**2 for x in my_list)
# Output: 1
print(next(a))

# Output: 9
print(next(a))

# Output: 36
print(next(a))

# Output: 100
print(next(a))

# Output: StopIteration
next(a)  """)
# Intialize the list
my_list = [1, 3, 6, 10]

a = (x ** 2 for x in my_list)
# Output: 1
print(next(a))

# Output: 9
print(next(a))

# Output: 36
print(next(a))

# Output: 100
print(next(a))

# Output: StopIteration
# next(a)

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Adaptacion Mia 1  """)
print(""" # Intialize the list
my_list = [1, 3, 6, 10]

a = (x**2 for x in my_list)

for numero in a:
    print(numero)  """)

# Intialize the list
my_list = [1, 3, 6, 10]

a = (x ** 2 for x in my_list)

for numero in a:
    print(numero)

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Adaptacion Mia 2  """)
print("""# Intialize the list
my_list = [1, 3, 6, 10]

for numero in (x**2 for x in my_list):
    print(numero)   """)

my_list = [1, 3, 6, 10]

for numero in (x ** 2 for x in my_list):
    print(numero)

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print(
    """@ Generator expression can be used inside functions. When used in such a way, the round parentheses can be dropped  """)
print(""" print(sum(x**2 for x in my_list))
print(max(x**2 for x in my_list))  """)
print(sum(x ** 2 for x in my_list))
print(max(x ** 2 for x in my_list))
########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Why generators are used in Python?

  1. Easy to Implement
sequence of power of 2's using generator function  """)
print("""def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

for i in PowTwoGen(4):
    print(i)   """)


def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


for i in PowTwoGen(4):
    print(i)

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ 3. Represent Infinite Stream  """)
print(""" Generators are excellent medium to represent an infinite stream of data. Infinite streams cannot be stored in memory and since generators produce only one item at a time, it can represent infinite stream of data.

The following example can generate all the even numbers (at least in theory).

 def all_even():
    n = 0
    while True:
        yield n
        n += 2 """)


def all_even():
    n = 0
    while True:
        yield n
        n += 2


########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ 4. Pipelining Generators  
Generators can be used to pipeline a series of operations. This is best illustrated using an example.

Suppose we have a log file from a famous fast food chain. The log file has a column (4th column) that keeps track of the number of pizza sold every hour and we want to sum it to find the total pizzas sold in 5 years.

Assume everything is in string and numbers that are not available are marked as 'N/A'. A generator implementation of this could be as follows.""")
print(""" #with open('sells.log') as file:
    pizza_col = (line[3] for line in file)
    per_hour = (int(x) for x in pizza_col if x != 'N/A')
    print("Total pizzas sold = ",sum(per_hour))   """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@  Closures
 Nonlocal variable in a nested function
Before getting into what a closure is, we have to first understand what a nested function and nonlocal variable is.

A function defined inside another function is called a nested function. Nested functions can access variables of the enclosing scope.

In Python, these non-local variables are read only by default and we must declare them explicitly as non-local (using nonlocal keyword) in order to modify them.

Following is an example of a nested function accessing a non-local variable.
 """)
print(""" def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    printer()

# We execute the function
# Output: Hello
print_msg("Hello")  """)
def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    printer()

# We execute the function
# Output: Hello
print_msg("Hello")

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Defining a Closure Function
In the example above, what would happen if the last line of the function print_msg() returned the printer() function instead of calling it? This means the function was defined as follows.  """)
print(""" def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    return printer  # this got changed

# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another() 
 The print_msg() function was called with the string "Hello" and the returned function was bound to the name another. On calling another(), the message was still remembered although we had already finished executing the print_msg() function.

This technique by which some data ("Hello") gets attached to the code is called closure in Python.

This value in the enclosing scope is remembered even when the variable goes out of scope or the function itself is removed from the current namespace.

Try running the following in the Python shell to see the output.

ef print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    return printer  # this got changed

# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()
del print_msg
another()
# Error
print_msg("Hello")
#Traceback (most recent call last):
#...
#NameError: name 'print_msg' is not defined
""")
def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    return printer  # this got changed

# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()
del print_msg
another()

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@When to use closures?
So what are closures good for?

Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object oriented solution to the problem.

When there are few methods (one method in most cases) to be implemented in a class, closures can provide an alternate and more elegant solutions. But when the number of attributes and methods get larger, better implement a class.

Here is a simple example where a closure might be more preferable than defining a class and making objects. But the preference is all yours.

   """)
print("""   """)
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Python Decorators
 A decorator takes in a function, adds some functionality and returns it. In this article, you will learn how you can create a decorator and why you should use it.
  
 Python has an interesting feature called decorators to add functionality to an existing code.

This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time. """)
print("""   """)


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ We must be comfortable with the fact that, everything in Python (Yes! Even classes), are objects. Names that we define are simply identifiers bound to these objects. Functions are no exceptions, they are objects too (with attributes). Various different names can be bound to the same function object.

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
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
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

print(operate(inc,3))
print(operate(dec,3))
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
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

#Outputs "Hello"
new()

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
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
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
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
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
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
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
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
    return a/b
print(divide(2,5))
#print(divide(2,0))


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
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

print(divide(2,5))
print(divide(2,0))

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@A keen observer will notice that parameters of the nested inner() function inside the 
decorator is same as the parameters of functions it decorates. Taking this into account, 
now we can make general decorators that work with any number of parameter.

In Python, this magic is done as function(*args, **kwargs). In this way, 
args will be the tuple of positional arguments and kwargs will be the dictionary 
of keyword arguments. An example of such decorator will be.
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

imprime(2,5,0)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
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
printer("Hello")

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ @property
 
 pythonic way to use getters and setters.
   
  let us first build an intuition on why it would be needed in the first place. """)
print("""   """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@An Example To Begin With
Let us assume that you decide to make a class that could store the temperature in degree Celsius. It would also implement a method to convert the temperature into degree Fahrenheit. One way of doing this is as follows.   """)
print(""" class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
# create new object
man = Celsius()
# set temperature
man.temperature = 37
# get temperature
print(man.temperature)
# get degrees Fahrenheit
print(man.to_fahrenheit())

The extra decimal places when converting into Fahrenheit is due to the floating point arithmetic error (try 1.1 + 2.2 in the Python interpreter).

Whenever we assign or retrieve any object attribute like temperature, as show above, Python searches it in the object's __dict__ dictionary.

print(man.__dict__)

print(man.__dict__)

Therefore, man.temperature internally becomes man.__dict__['temperature'].

Now, let's further assume that our class got popular among clients and they started using it in their programs. They did all kinds of assignments to the object.

One fateful day, a trusted client came to us and suggested that temperatures cannot go below -273 degree Celsius (students of thermodynamics might argue that it's actually -273.15), also called the absolute zero. He further asked us to implement this value constraint. Being a company that strive for customer satisfaction, we happily heeded the suggestion and released version 1.01 (an upgrade of our existing class).


""")
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
# create new object
man = Celsius()
# set temperature
man.temperature = 37
# get temperature
print(man.temperature)
# get degrees Fahrenheit
print(man.to_fahrenheit())

print(man.__dict__)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@Using Getters and Setters

temperatures cannot go below -273 degree Celsius. implement this value constraint 
  
 An obvious solution to the above constraint will be to hide the attribute temperature (make it private) and define new getter and setter interfaces to manipulate it. This can be done as follows. """)
print(""" class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value
          
          We can see above that new methods get_temperature() and set_temperature() were defined and furthermore, temperature was replaced with _temperature. An underscore (_) at the beginning is used to denote private variables in Python.

>>> c = Celsius(-277)
Traceback (most recent call last):
...
ValueError: Temperature below -273 is not possible

>>> c = Celsius(37)
>>> c.get_temperature()
37
>>> c.set_temperature(10)

>>> c.set_temperature(-300)
Traceback (most recent call last):
...
ValueError: Temperature below -273 is not possible
This update successfully implemented the new restriction. We are no longer allowed to set temperature below -273.

Please note that private variables don't exist in Python. There are simply norms to be followed. The language itself don't apply any restrictions.

>>> c._temperature = -300
>>> c.get_temperature()
-300
But this is not of great concern. The big problem with the above update is that, all the clients who implemented our previous class in their program have to modify their code from obj.temperature to obj.get_temperature() and all assignments like obj.temperature = val to obj.set_temperature(val).

This refactoring can cause headaches to the clients with hundreds of thousands of lines of codes.

All in all, our new update was not backward compatible. This is where property comes to rescue.

""")
class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

c = Celsius(37)
print(c.get_temperature())
c.set_temperature(10)
print(c.get_temperature())
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@The big problem with the above update is that, all the clients who implemented our previous class in their program have to modify their code from obj.temperature to obj.get_temperature() and all assignments like obj.temperature = val to obj.set_temperature(val).

This refactoring can cause headaches to the clients with hundreds of thousands of lines of codes.

All in all, our new update was not backward compatible. This is where property comes to rescue.

   """)
print("""   """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@The Power of @property
The pythonic way to deal with the above problem is to use property. Here is how we could have achieved it.   """)
print("""class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)
    c = Celsius()
    We added a print() function inside get_temperature() and set_temperature() to clearly observe that they are being executed.

The last line of the code, makes a property object temperature. Simply put, property attaches some code (get_temperature and set_temperature) to the member attribute accesses (temperature).

Any code that retrieves the value of temperature will automatically call get_temperature() instead of a dictionary (__dict__) look-up. Similarly, any code that assigns a value to temperature will automatically call set_temperature(). This is one cool feature in Python.

We can see above that set_temperature() was called even when we created an object.

Can you guess why?

The reason is that when an object is created, __init__() method gets called. This method has the line self.temperature = temperature. This assignment automatically called set_temperature().

>>> c.temperature
Getting value
0
Similarly, any access like c.temperature automatically calls get_temperature(). This is what property does. Here are a few more examples.

>>> c.temperature = 37
Setting value

>>> c.to_fahrenheit()
Getting value
98.60000000000001
By using property, we can see that, we modified our class and implemented the value constraint without any change required to the client code. Thus our implementation was backward compatible and everybody is happy.

Finally note that, the actual temperature value is stored in the private variable _temperature. The attribute temperature is a property object which provides interface to this private variable.

""")
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)

c = Celsius()
print(c.temperature)
c.temperature = 37
print(c.temperature)
print(c.to_fahrenheit())

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Digging Deeper into Property
  """)
print(""" n Python, property() is a built-in function that creates and returns a property object. The signature of this function is

property(fget=None, fset=None, fdel=None, doc=None)
where, fget is function to get value of the attribute, fset is function to set value of the attribute, fdel is function to delete the attribute and doc is a string (like a comment). As seen from the implementation, these function arguments are optional. So, a property object can simply be created as follows.

>>> property()
<property object at 0x0000000003239B38>
A property object has three methods, getter(), setter(), and delete() to specify fget, fset and fdel at a later point. This means, the line

temperature = property(get_temperature,set_temperature)
could have been broken down as

# make empty property
temperature = property()
# assign fget
temperature = temperature.getter(get_temperature)
# assign fset
temperature = temperature.setter(set_temperature)
These two pieces of codes are equivalent.

Programmers familiar with decorators in Python can recognize that the above construct can be implemented as decorators.

We can further go on and not define names get_temperature and set_temperature as they are unnecessary and pollute the class namespace. For this, we reuse the name temperature while defining our getter and setter functions. This is how it can be done.

  """)

class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Python Shallow Copy and Deep Copy
  """)
print("""Copy an Object in Python
In Python, we use = operator to create a copy of an object. You may think that this creates a new object; it doesn't. It only creates a new variable that shares the reference of the original object.

Let's take an example where we create a list named old_list and pass an object reference to new_list using = operator   """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@Example 1: Copy using = operator
   """)
print("""old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))
   """)
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))

print("""
As you can see from the output both variables old_list and new_list shares the same id i.e 140673303268168.

So, if you want to modify any values in new_list or old_list, the change is visible in both.

Essentially, sometimes you may want to have the original values unchanged and only modify the new values or vice versa. In Python, there are two ways to create copies:

Shallow Copy
Deep Copy
To make these copy work, we use the copy module.""")
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Copy Module
We use the copy module of Python for shallow and deep copy operations. Suppose, you need to copy the compound list say x. For example:

import copy
copy.copy(x)
copy.deepcopy(x)
Here, the copy() return a shallow copy of x. Similarly, deepcopy() return a deep copy of x.
  """)
print("""   """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@Shallow Copy
A shallow copy creates a new object which stores the reference of the original elements.

So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects. This means, a copy process does not recurse or create copies of nested objects itself.
   
Example 2: Create a copy using shallow copy
""")
print(""" import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)  """)
import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)

old_list[2][2] = 0
print("Old list:", old_list)
print("New list:", new_list)

new_list[2][2] = 5

print("Old list:", old_list)
print("New list:", new_list)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@Example 3: Adding [4, 4, 4] to old_list, using shallow copy
   """)
print("""
import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)

old_list[2][2] = 0
print("Old list:", old_list)
print("New list:", new_list)

new_list[2][2] = 5

print("Old list:", old_list)
print("New list:", new_list)

old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list) 
  
 new_list.append([3, 3, 3])

print("Old list:", old_list)
print("New list:", new_list)
 """)
import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)

old_list[2][2] = 0
print("Old list:", old_list)
print("New list:", new_list)

new_list[2][2] = 5

print("Old list:", old_list)
print("New list:", new_list)
old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)

new_list.append([3, 3, 3])

print("Old list:", old_list)
print("New list:", new_list)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Deep Copy
A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.

Let’s continue with example 2. However, we are going to create deep copy using deepcopy() function present in copy module. The deep copy creates independent copy of original object and all its nested objects.

  """)
print("""   """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Example 5: Copying a list using deepcopy()
  """)
print("""import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)
   """)
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Example 6: Adding a new nested object in the list using Deep copy  """)
print(""" import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)  """)
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ What is Assertion?
 
Assertions are simply boolean expressions that checks if the conditions return true or not. If it is true, the program does nothing and move to the next line of code. However, if it's false, the program stops and throws an error
  
 It is also a debugging tool as it brings the program on halt as soon as any error is occurred and shows on which point of the program error has occurred.
  
  """)
print("""   """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Python assert Statement
Python has built-in assert statement to use assertion condition in the program. assert statement has a condition or expression which is supposed to be always true. If the condition is false assert halts the program and gives an AssertionError.

Syntax for using Assert in Pyhton:
assert <condition>
assert <condition>,<error message> 
 
 n Python we can use assert statement in two ways as mentioned above.

assert statement has a condition and if the condition is not satisfied the program will stop and give AssertionError.
assert statement can also have a condition and a optional error message. If the condition is not satisfied assert stops the program and gives AssertionError along with the error message.
Let's take an example, where we have a function which will calculate the average of the values passed by the user and the value should not be an empty list. We will use assert statement to check the parameter and if the length is of the passed list is zero, program halts.""")
print("""   """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Example 1: Using assert without Error Message
  """)
print("""def avg(marks):
    assert len(marks) != 0
    return sum(marks)/len(marks)

mark1 = []
print("Average of mark1:",avg(mark1))
   
When we run the above program, the output will be:

AssertionError
We got an error as we passed an empty list mark1 to assert statement, the condition became false and assert stops the program and give AssertionError.

Now let's pass another list which will satisfy the assert condition and see what will be our output.
   
 def avg(marks):
    assert len(marks) != 0
    return sum(marks)/len(marks)

mark1 = []
print("Average of mark1:",avg(mark1))
  
""")
def avg(marks):
    assert len(marks) != 0
    return sum(marks)/len(marks)

mark1 = []
#print("Average of mark1:",avg(mark1))
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ Example 2: Using assert with error message
  """)
print("""def avg(marks):
    assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)

mark2 = [55,88,78,90,79]
print("Average of mark2:",avg(mark2))

mark1 = []
print("Average of mark1:",avg(mark1))
  
 When we run the above program, the output will be:

Average of mark2: 78.0
AssertionError: List is empty.
We passed a non-empty list mark2 and also an empty list mark1 to the avg() function and we got output for mark2 list but after that we got an error AssertionError: List is empty. The assert condition was satisfied by the mark2 list and program to continue to run. However, mark1 doesn't satisfy the condition and gives an AssertionError """)
def avg(marks):
    assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)

mark2 = [55,88,78,90,79]
print("Average of mark2:",avg(mark2))

mark1 = []
#print("Average of mark1:",avg(mark1))
#
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ https://docs.python.org/3/library/asyncio.ht
  """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ https://github.com/tulir/telethon-session-sqlalchemy""")

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ https://www.python-course.eu/sql_python.php
  """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ https://telethon.readthedocs.io/en/latest/extra/basic/asyncio-magic.html""")


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ https://github.com/LonamiWebs/Telethon/tree/sync
  """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ https://telethon.readthedocs.io/en/latest/index.html#""")
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ https://github.com/LonamiWebs/Telethon
  """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ https://github.com/PyMySQL/PyMySQL#""")


########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ https://github.com/LonamiWebs/Telethon/tree/sync
  """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ https://sahandsaba.com/understanding-asyncio-node-js-python-3-4.html""")
########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ https://telepot.readthedocs.io/en/latest/
  """)

########################################################################################################################
print("")
n = n + 1
print("-",n, "-------------------------------------------------------------------------------------------------------")
#**********************************************************************************************************************#
print("""@ https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/""")
