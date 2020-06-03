########################################################################################################################
print("")
n = 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Python Shallow Copy and Deep Copy
  """)
print("""Copy an Object in Python
In Python, we use = operator to create a copy of an object. You may think that this creates a new object; it doesn't. It only creates a new variable that shares the reference of the original object.

Let's take an example where we create a list named old_list and pass an object reference to new_list using = operator   """)

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
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
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
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
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
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
print('ID of Old List:', id(old_list))
print('ID of New List:', id(new_list))

old_list[2][2] = 0
print("Old list:", old_list)
print("New list:", new_list)

new_list[2][2] = 5

print("Old list:", old_list)
print("New list:", new_list)

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
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
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
print("""@ Deep Copy
A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.

Let’s continue with example 2. However, we are going to create deep copy using deepcopy() function present in copy module. The deep copy creates independent copy of original object and all its nested objects.

  """)
print("""   """)

########################################################################################################################
print("")
n = n + 1
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
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
print("-", n, "-------------------------------------------------------------------------------------------------------")
# **********************************************************************************************************************#
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