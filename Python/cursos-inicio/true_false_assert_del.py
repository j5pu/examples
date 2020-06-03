#!/usr/bin/python
"""
This article aims at providing a detailed insight to these keywords.

1. True : This keyword is used to represent a boolean true. If a statement is truth, “True” is printed.

2. False : This keyword is used to represent a boolean false. If a statement is False, “False” is printed.
True and False in python are same as 1 and 0.Example:
"""

print (False == 0)
print (True == 1)
 
print (True + True + True)
print (True + False + False)

""" 
3. None : This is a special constant used to denote a null value or a void. Its important to remember, 0, any empty container(e.g empty list) do not compute to None.
It is an object of its own datatype – NoneType. It is not possible to create multiple None objects and can assign it to variables.
"""
# Python code to demonstrate 
# True, False, None, and, or , not
 
# showing that None is not equal to 0
# prints False as its false.
print (None == 0)
 
# showing objective of None
# two None value equated to None
# here x and y both are null
# hence true
x = None
y = None
print (x == y)
 
# showing logical operation 
# or (returns True)
print (True or False)
 
# showing logical operation 
# and (returns False)
print (False and True)
 
# showing logical operation 
# not (returns False)
print (not True)

"""
7. assert : This function is used for debugging purposes. Usually used to check the correctness of code. If a statement evaluated to true, nothing happens, but when it is false, “AssertionError” is raised . One can also print a message with the error, separated by a comma.

8. break : “break” is used to control the flow of loop. The statement is used to break out of loop and passes the control to the statement following immediately after loop.

9. continue : “continue” is also used to control the flow of code. The keyword skips the current iteration of the loop, but does not end the loop.

Illustrations of break and continue keywords can be seen in the article below.

Loops and Control Statements (continue, break and pass) in Python
10. class : This keyword is used to declare user defined classes.For more info. click here.

11. def : This keyword is used to declare user defined functions.For more info. click here.

12. if : It is a control statement for decision making. Truth expression forces control to go in “if” statement block.

13. else : It is a control statement for decision making. False expression forces control to go in “else” statement block.

14. elif : It is a control statement for decision making. It is short for “else if”

if, else and elif conditional statements are explained in detail here article.

15. del : del is used to delete a reference to an object. Any variable or list value can be deleted using del.
"""
# Python code to demonstrate
# del and assert

# initialising list
a = [1, 2, 3]

# printing list before deleting any value
print ("The list before deleting any value")
print (a)

# using del to delete 2nd element of list
del a[1]

# printing list after deleting 2nd element
print ("The list after deleting 2nd element")
print (a)

# demonstrating use of assert
# prints AssertionError
assert 5 < 3, "5 is not smaller than 3"


