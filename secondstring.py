# This program asks a user to input a string, and outputs
# every second letter in reverse order.
# Author: Fabio Fabrizi

# Steps (I did paper and pen first)
# Find Python function to reverse a string - There is none!
# 


# Found the solution from Googling - W3 schools.
# https://www.w3schools.com/python/python_howto_reverse_string.asp 
# Using slice, changed the step from -1 to -2
# txt = "The quick brown fox jumps over the lazy dog."[::-2]
# print(txt)
txt = input("Please enter some text: ")
print(txt[::-2])