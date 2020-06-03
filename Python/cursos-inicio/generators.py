n = 1
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

