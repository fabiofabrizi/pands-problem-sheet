# Task 3:
# This program asks a user to input a string, and outputs
# every second letter in reverse order.
# Author: Fabio Fabrizi
"""
Steps (I did paper and pen first)

Found the solution from Googling - W3 schools.
https://www.w3schools.com/python/python_howto_reverse_string.asp 
Using slice, changed the step from -1 to -2
txt = "The quick brown fox jumps over the lazy dog."[::-2]
print(txt)
This was the first version
txt = input("Please enter some text: ")
print(txt[::-2])
Prompt the user for input, whilst checking if the user 
has actually entered a sentence using a loop.
The loop will always run whilst the input is empty, 
so the user is forced to enter something.

Notes: Anything entered via the console is a string, unless
explicitly converted to another type. Therefore, if the user
enters numbers, that will also work, as they are a string of numbers
"""
txt = ""

while len(txt) == 0:
    txt = input("Please enter a sentence: ")
    if len(txt) == 0:
        print("If you don't enter a sentence, it can't be reversed!")

# Function to reverse the string
# Notice the index is counting back every 2 
def second_string(txt):
    # Set result to empty string
    result = ""
    # Find index of last char with len(txt)
    index = len(txt) - 1
    while index >= 0:
        result += txt[index]
        index -= 2
    return result
second_string(txt)
# Below prints the result
print(second_string(txt))

