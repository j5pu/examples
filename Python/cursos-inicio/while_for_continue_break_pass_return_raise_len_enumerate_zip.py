# #!/usr/bin/python
# from __future__ import print_function
# """
# Loops and Control Statements (continue, break and pass) in Python
# Python programming language provides following types of loops to handle looping requirements.
#
# While Loop
#
# Syntax :
# while expression:
#     statement(s)
# In Python, all the statements indented by the same number of character spaces after a programming construct are considered to be part of a single block of code. Python uses indentation as its method of grouping statements.
# """
# # prints Hello Geek 3 Times
# count = 0
# while (count < 3):
#     count = count+1
#     print("Hello Geek")
#
# """
# See this for an example where while loop is used for iterators. As mentioned in the article, it is not recommended to use while loop for iterators in python.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
# Using Iterations in Python Effectively
# C-style approach:
# This approach requires prior knowledge of total number of iterations.
# """
# # A C-style way of accessing list elements
# cars = ["Aston", "Audi", "McLaren"]
# i = 0
# while (i < len(cars)):
#     print(cars[i])
#     i += 1
#
# """
# Important Points:
#
# This style of looping is rarely used by python programmers.
# This 4-step approach creates no compactness with single-view looping construct.
# This is also prone to errors in large-scale programs or designs.
# There is no C-Style for loop in Python, i.e., a loop like for (int i=0; i<n; i++)
#
#
# Use of for-in (or for each) style:
#
# This style is used in python containing iterator of lists, dictonary, n dimensional-arrays etc. The iterator fetches each component and prints data while looping. The iterator is automatically incremented/decremented in this construct.
# """
# # Accessing items using for-in loop
# print ('--- Este es el que dice bueno para loop, no el while ---')
# cars = ["Aston", "Audi", "McLaren"]
# for x in cars:
#     print (x)
# print ('--------------------------------------------------------')
# """
# See this for more examples of different data types.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
# Iterators in Python
# Iterator in python is any python type that can be used with a ‘for in loop’. Python lists, tuples, dicts and sets are all examples of inbuilt iterators. These types are iterators because they implement following methods. In fact, any object that wants to be an iterator must implement following methods.
#
# 	1. __iter__ method that is called on initialization of an iterator. This should return an object that has a next or __next__ (in Python 3) method.
# 	2. next ( __next__ in Python 3) The iterator next method should return the next value for the iterable. When an iterator is used with a ‘for in’ loop, the for loop implicitly calls next() on the iterator object. This method should raise a StopIteration to signal the end of the iteration.
#
# Below is a simple Python program that creates iterator type that iterates from 10 to given limit. For example, if limit is 15, then it prints 10 11 12 13 14 15. And if limit is 5, then it prints nothing.
# """
# # A simple Python program to demonstrate
# # working of iterators using an example type
# # that iterates from 10 to given value
#
# # An iterable user defined type
# class Test:
#
#     # Cosntructor
#     def __init__(self, limit):
#         self.limit = limit
#
#     # Called when iteration is initialized
#     def __iter__(self):
#         self.x = 10
#         return self
#
#     # To move to next element. In Python 3,
#     # we should replace next with __next__
#     def next(self):
#
#         # Store current value ofx
#         x = self.x
#
#         # Stop iteration if limit is reached
#         if x > self.limit:
#             raise StopIteration
#
#         # Else increment and return old value
#         self.x = x + 1;
#         return x
#
# # Prints numbers from 10 to 15
# for i in Test(15):
#     print(i)
#
# # Prints nothing
# for i in Test(5):
#     print(i)
#
# """
# Examples of inbuilt iterator types.
# """
# # Sample built-in iterators
#
# # Iterating over a list
# print("List Iteration")
# l = ["geeks", "for", "geeks"]
# for i in l:
#     print(i)
#
# # Iterating over a tuple (immutable)
# print("\nTuple Iteration")
# t = ("geeks", "for", "geeks")
# for i in t:
#     print(i)
#
# # Iterating over a String
# print("\nString Iteration")
# s = "Geeks"
# for i in s :
#     print(i)
#
# # Iterating over dictionary
# print("\nDictionary Iteration")
# d = dict()
# d['xyz'] = 123
# d['abc'] = 345
# for i in d :
#     print("%s  %d" %(i, d[i]))
#
# """
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#
# Indexing using Range function: We can also use indexing using range() in Python.
# """
# # Accessing items using indexes and for-in
#
# cars = ["Aston", "Audi", "McLaren"]
# for i in range(len(cars)):
#     print(cars[i])
#
# """
# Enumerate:
#
# Enumerate is built-in python function that takes input as iterator, list etc and returns a tuple containing index and data at that index in the iterator sequence. For example, enumerate(cars), returns a iterator that will return (0, cars[0]), (1, cars[1]), (2, cars[2]), and so on.
# """
# # Accessing items using enumerate()
#
# cars = ["Aston" , "Audi", "McLaren "]
# for i, x in enumerate(cars):
#     print (x)
#
# """
# Below solution also works.
# """
# # Accessing items and indexes enumerate()
#
# cars = ["Aston" , "Audi", "McLaren "]
# for x in enumerate(cars):
#     print (x[0], x[1])
# """
# We can also directly print returned value of enumerate() to see what it returns.
# """
# # Printing return value of enumerate()
#
# cars = ["Aston" , "Audi", "McLaren "]
# print (enumerate(cars))
# """
# Enumerate takes parameter start which is default set to zero. We can change this parameter to any value we like. In the below code we have used start as 1.
# """
# # demonstrating use of start in enumerate
#
# cars = ["Aston" , "Audi", "McLaren "]
# for x in enumerate(cars, start=1):
#     print (x[0], x[1])
#
# """
# enumerate() helps to embed solution for accessing each data item in iterator and fetching index of each data item.
#
# Looping extensions:
#
# i) Two iterators for a single looping construct: In this case, a list and dictionary are to be used for each iteration in a single looping block using enumerate function. Let us see example.
# """
# # Two separate lists
# cars = ["Aston", "Audi", "McLaren"]
# accessories = ["GPS kit", "Car repair-tool kit"]
#
# # Single dictionary holds prices of cars and
# # its accessories.
# # First two items store prices of cars and
# # next three items store prices of accessories.
# prices = {1:"570000$", 2:"68000$", 3:"450000$",
#           4:"890000$", 5:"4500$"}
#
# # Printing prices of cars
# for index, c in enumerate(cars, start=1):
#     print ("Car: %s Price: %s"%(c, prices[index]))
#
# # Printing prices of accessories
# for index, a in enumerate(accessories,start=1):
#     print ("Accessory: %s Price: %s"\
#            %(a,prices[index+len(cars)]))
#
# """
# ii) zip function (Both iterators to be used in single looping construct):
# This function is helpful to combine similar type iterators(list-list or dict- dict etc) data items at ith position. It uses shortest length of these input iterators. Other items of larger length iterators are skipped. In case of empty iterators it returns No output.
#
# For example, the use of zip for two lists (iterators) helped to combine a single car and its required accessory.
# """
# # Python program to demonstrate working of zip
#
# # Two separate lists
# cars = ["Aston", "Audi", "McLaren"]
# accessories = ["GPS", "Car Repair Kit",
#                "Dolby sound kit"]
#
# # Combining lists and printing
# for c, a in zip(cars, accessories):
#     print ("Car: %s, Accessory required: %s"\
#           %(c, a))
#
# """
# The reverse of getting iterators from zip function is known as unzipping using “*” operator.
#
# Use of enumerate function and zip function helps to achieve an effective extension of iteration logic in python and solves many more sub-problems of a huge task or problem.
# """
# # Python program to demonstrate unzip (reverse
# # of zip)using * with zip function
#
# # Unzip lists
# l1,l2 = zip(*[('Aston', 'GPS'),
#               ('Audi', 'Car Repair'),
#               ('McLaren', 'Dolby sound kit')
#            ])
#
# # Printing unzipped lists
# print(l1)
# print(l2)
#
# """
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#
# For in Loop
#
# In Python, there is no C style for loop, i.e., for (i=0; i<n; i++). There is “for in” loop which is similar to for each loop in other languages.
#
# Syntax:
#
# for iterator_var in sequence:
#     statements(s)
# It can be used to iterate over iterators and a range.
#
# """
# # Iterating over a list
# print("List Iteration")
# l = ["geeks", "for", "geeks"]
# for i in l:
#     print(i)
#
# # Iterating over a tuple (immutable)
# print("\nTuple Iteration")
# t = ("geeks", "for", "geeks")
# for i in t:
#     print(i)
#
# # Iterating over a String
# print("\nString Iteration")
# s = "Geeks"
# for i in s :
#     print(i)
#
# # Iterating over dictionary
# print("\nDictionary Iteration")
# d = dict()
# d['xyz'] = 123
# d['abc'] = 345
# for i in d :
#     print("%s  %d" %(i, d[i]))
#
# """
# Nested Loops
#
# Python programming language allows to use one loop inside another loop. Following section shows few examples to illustrate the concept.
# Syntax:
#
# for iterator_var in sequence:
#     for iterator_var in sequence:
#         statements(s)
#         statements(s)
# The syntax for a nested while loop statement in Python programming language is as follows:
#
# while expression:
#     while expression:
#         statement(s)
#         statement(s)
# A final note on loop nesting is that we can put any type of loop inside of any other type of loop. For example a for loop can be inside a while loop or vice versa.
# """
# #from __future__ import print_function
# for i in range(1, 5):
#     for j in range(i):
#          print(i, end=' ')
#     print()
#
#
# """
# Loop Control Statements
#
# Loop control statements change execution from its normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed. Python supports the following control statements.
# Continue Statement
# It returns the control to the beginning of the loop.
# """
# # Prints all letters except 'e' and 's'
# for letter in 'geeksforgeeks':
#     if letter == 'e' or letter == 's':
#          continue
#     print ('Current Letter :', letter)
#     var = 10
#
# """
# Break Statement
# It brings control out of the loop
# """
# for letter in 'geeksforgeeks':
#
#     # break the loop as soon it sees 'e'
#     # or 's'
#     if letter == 'e' or letter == 's':
#          break
#
# print ('Current Letter :', letter)
#
# """
# Pass Statement
# We use pass statement to write empty loops. Pass is also used for empty control statement, function and classes.
# """
# # An empty loop
# for letter in 'geeksforgeeks':
#     pass
# print ('Last Letter :', letter)
