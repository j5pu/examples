#!/usr/bin/python
#Python code to demonstrate working of iskeyword()
 
# importing "keyword" for keyword operations
import keyword
 
# initializing strings for testing
s = "for"
s1 = "geeksforgeeks"
s2 = "elif"
s3 = "elseif"
s4 = "nikhil"
s5 = "assert"
s6 = "shambhavi"
s7 = "True"
s8 = "False"
s9 = "akshat"
s10 = "akash"
s11 = "break"
s12 = "ashty"
s13 = "lambda"
s14 = "suman"
s15 = "try"
s16 = "vaishnavi"
 
# checking which are keywords
if keyword.iskeyword(s):
        print ( s + " is a python keyword")
else :  print ( s + " is not a python keyword")
 
if keyword.iskeyword(s1):
        print ( s1 + " is a python keyword")
else :  print ( s1 + " is not a python keyword")
 
if keyword.iskeyword(s2):
        print ( s2 + " is a python keyword")
else :  print ( s2 + " is not a python keyword")
 
if keyword.iskeyword(s3):
        print ( s3 + " is a python keyword")
else :  print ( s3 + " is not a python keyword")
 
if keyword.iskeyword(s4):
        print ( s4 + " is a python keyword")
else :  print ( s4 + " is not a python keyword")
 
if keyword.iskeyword(s5):
        print ( s5 + " is a python keyword")
else :  print ( s5 + " is not a python keyword")
 
if keyword.iskeyword(s6):
        print ( s6 + " is a python keyword")
else :  print ( s6 + " is not a python keyword")
 
if keyword.iskeyword(s7):
        print ( s7 + " is a python keyword")
else :  print ( s7 + " is not a python keyword")
 
if keyword.iskeyword(s8):
        print ( s8 + " is a python keyword")
else :  print ( s8 + " is not a python keyword")
 
if keyword.iskeyword(s9):
        print ( s9 + " is a python keyword")
else :  print ( s9 + " is not a python keyword")
 
if keyword.iskeyword(s10):
        print ( s10 + " is a python keyword")
else :  print ( s10 + " is not a python keyword")
 
if keyword.iskeyword(s11):
        print ( s11 + " is a python keyword")
else :  print ( s11 + " is not a python keyword")
 
if keyword.iskeyword(s12):
        print ( s12 + " is a python keyword")
else :  print ( s12 + " is not a python keyword")
 
if keyword.iskeyword(s13):
        print ( s13 + " is a python keyword")
else :  print ( s13 + " is not a python keyword")
 
if keyword.iskeyword(s14):
        print ( s14 + " is a python keyword")
else :  print ( s14 + " is not a python keyword")
 
if keyword.iskeyword(s15):
        print ( s15 + " is a python keyword")
else :  print ( s15 + " is not a python keyword")
 
if keyword.iskeyword(s16):
        print ( s16 + " is a python keyword")
else :  print ( s16 + " is not a python keyword")

print('-------------------------------------------------------------------')
#Python code to demonstrate working of iskeyword()
 
# importing "keyword" for keyword operations
import keyword
 
# printing all keywords at once using "kwlist()"
print ("The list of keywords is : ")
print (keyword.kwlist)
