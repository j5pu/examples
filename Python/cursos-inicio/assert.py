########################################################################################################################
n = 1
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ What is Assertion?

Assertions are simply boolean expressions that checks if the conditions return true or not. If it is true, the program does nothing and move to the next line of code. 
However, if it's false, the program stops and throws an error

 It is also a debugging tool as it brings the program on halt as soon as any error is occurred and shows on which point of the program error has occurred.

  """)
print("""   """)

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Python assert Statement
Python has built-in assert statement to use assertion condition in the program. assert statement has a condition or expression which is supposed to be always true. 
If the condition is false assert halts the program and gives an AssertionError.

Syntax for using Assert in Pyhton:
assert <condition>
assert <condition>,<error message> 

 n Python we can use assert statement in two ways as mentioned above.

assert statement has a condition and if the condition is not satisfied the program will stop and give AssertionError.
assert statement can also have a condition and a optional error message. 
If the condition is not satisfied assert stops the program and gives AssertionError along with the error message.
Let's take an example, where we have a function which will calculate the average of the values passed by the user and the value should not be an empty list. 
We will use assert statement to check the parameter and if the length is of the passed list is zero, program halts.""")
print("""   """)

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
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
    return sum(marks) / len(marks)


mark1 = []
#print("Average of mark1:",avg(mark1))
########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
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
We passed a non-empty list mark2 and also an empty list mark1 to the avg() function and we got output for mark2 list but after that we got an error AssertionError: List is empty. 
The assert condition was satisfied by the mark2 list and program to continue to run. However, mark1 doesn't satisfy the condition and gives an AssertionError """)


def avg(marks):
    assert len(marks) != 0, "List is empty."
    return sum(marks) / len(marks)


mark2 = [55, 88, 78, 90, 79]
print("Average of mark2:", avg(mark2))

mark1 = []
print("Average of mark1:",avg(mark1))
#