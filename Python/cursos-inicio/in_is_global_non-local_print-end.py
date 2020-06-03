#!/usr/bin/python
"""
More keywords:

16. try : This keyword is used for exception handling, used to catch the errors in the code using the keyword except. Code in “try” block is checked, if there is any type of error, except block is executed.

17. except : As explained above, this works together with “try” to catch exceptions.

18. raise : Also used for exception handling to explicitly raise exceptions.

19. finally : No matter what is result of the “try” block, block termed “finally” is always executed. Detailed article –Exception Handling in Python

20. for : This keyword is used to control flow and for looping.

21. while : Has a similar working like “for” , used to control flow and for looping.

22. pass : It is the null statement in python. Nothing happens when this is encountered. This is used to prevent indentation errors and used as a placeholder

Detailed Article – for, while, pass

23. import : This statement is used to include a particular module into current program.

24. from : Generally used with import, from is used to import particular functionality from the module imported.

25. as : This keyword is used to create the alias for the module imported. i.e giving a new name to the imported module.. E.g import math as mymath.

Detailed Article – import, from and as

26. lambda : This keyword is used to make inline returning functions with no statements allowed internally. Detailed Article – map, filter, lambda

27. return : This keyword is used to return from the function. Detailed article –  Return values in Python.

28. yield : This keyword is used like return statement but is used to return a generator. Detailed Article – yield keyword

29. with : This keyword is used to wrap the execution of block of code within methods defined by context manager.This keyword is not used much in day to day programming.

30. in : This keyword is used to check if a container contains a value. This keyword is also used to loop through the container.

31. is : This keyword is used to test object identity, i.e to check if both the objects take same memory location or not.
"""

# Python code to demonstrate working of
# in and is
 
# using "in" to check 
if 's' in 'geeksforgeeks':
       print ("s is part of geeksforgeeks")
else : print ("s is not part of geeksforgeeks")
 
# using "in" to loop through
for i in 'geeksforgeeks':
    print (i,end=" ")
 
print ("\r")
     
# using is to check object identity
# string is immutable( cannot be changed once alloted)
# hence occupy same memory location
print (' ' is ' ')
 
# using is to check object identity
# dictionary is mutable( can be changed once alloted)
# hence occupy different memory location
print ({} is {})
print ({} == {})

""" 
32. global : This keyword is used to define a variable inside the function to be of a global scope.

33. non-local : This keyword works similar to the global, but rather than global, this keyword declares a variable to point to variable of outside enclosing function, in case of nested functions.

"""
# Python code to demonstrate working of
# global and non local
 
#initializing variable globally
a = 10
 
# used to read the variable
def read():
    print (a)
 
# changing the value of globally defined variable
def mod1():
    global a 
    a = 5
 
# changing value of only local variable
def mod2():
    a = 15
 
# reading initial value of a
# prints 10
read()
 
# calling mod 1 function to modify value
# modifies value of global a to 5
mod1()
 
# reading modified value
# prints 5
read()
 
# calling mod 2 function to modify value
# modifies value of local a to 15, doesn't effect global value
mod2()
 
# reading modified value
# again prints 5
read()
 
# demonstrating non local 
# inner loop changing the value of outer a
# prints 10
print ("Value of a using nonlocal is : ",end="")
def outer():
    a = 5
    def inner():
        nonlocal a 
        a = 10
    inner()
    print (a)
 
outer()
 
# demonstrating without non local 
# inner loop not changing the value of outer a
# prints 5
print ("Value of a without using nonlocal is : ",end="")
def outer():
    a = 5
    def inner():
        a = 10
    inner()
    print (a)
 
outer()
