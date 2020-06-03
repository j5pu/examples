#!/usr/local/bin/python3.7
'https://realpython.com/python-f-strings/'
'''
f-Strings: A New and Improved Way to Format Strings in Python
'''
name = "Eric"
age = 74
print(f"Hello, {name}. You are {age}.")

'''
Arbitrary Expressions
'''
print(f"{2 * 37}")

def to_lowercase(input):
    return input.lower()
name = "Eric Idle"

'call functions'
print(f"{to_lowercase(name)} is funny.")

'call method'
print(f"{name.lower()} is funny.")

'use objects created from classes with f-strings'
class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"


new_comedian = Comedian("Eric", "Idle", "74")
print(f"{new_comedian}")
print(f"{new_comedian!r}")

'''
Multiline f-strings
'''
name = "Eric"
profession = "comedian"
affiliation = "Monty Python"
message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
)
print(message)

message = f"""
    Hi {name}.
    You are a {profession}.
    You were in {affiliation}.
    """
print(message)

'''
Dictionaries
'''
# If you are going to use single quotation marks for the keys of the dictionary,
# then remember to make sure you’re using double quotation marks for the f-strings containing the keys.
comedian = {'name': 'Eric Idle', 'age': 74}
print(f"The comedian is {comedian['name']}, aged {comedian['age']}.")

'''
Braces
'''
print(f"{{74}}")

'''
Backslashes
'''
' print(f"{\"Eric Idle\"}") # ERROR '
# evaluating the expression beforehand and using the result in the f-string
name = "Eric Idle"
print(f"{name}")

'''
Inline Comments
'''
' print(f"Eric is {2 * 37 #Oh my!}.") # ERROR '