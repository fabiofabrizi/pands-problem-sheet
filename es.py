# This is the weekly task for Week 7
# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line
#
# The filename is a plain text version of 'Songs of Innocence and Experience' by William Blake.
# Downloaded from the website below.
# https://www.gutenberg.org/ebooks/search/?query=Songs+of+Innocence+and+Experience&submit_search=Go%21

# Author: Fabio Fabrizi

# Assumptions that I'm making:

# 1) The user has a text file that is 'Songs_Of_Innocence.txt' - I have included this.
# Failing that, the user has a text file that is in the same folder where the python 
# script will be run.
# 2) Comparing user input with text files in path using what 
# we've learned in week 7. If no text file exists, a message will be printed to the user.
# References:
# https://stackoverflow.com/questions/7033987/get-a-file-from-cli-input Where I found out about sys.argv
# https://docs.python.org/3/library/sys.html (to find out what sys.argv did)
#
# Was also looking at https://docs.python.org/3/library/fileinput.html
# which can be used for multiple file inputs.
# 
# I had to specify encoding as it wasn't working for me.

# Notes: Right now, it works, but looks messy to me.
# I'm going to try and tidy up and make the checking part into a function
# and use Python's built-in count() method to make it tidier.

import os
import sys
filename = sys.argv[-1] # Get the last 

# Get Extension
get_ext = os.path.splitext(filename)
#print(get_ext[1]) # to test what happens

# Check Extension
ext = get_ext[1]
# print(ext) # To check it's working
if (ext != '.txt'):
    print("Please enter a plain text file (.txt) to check")
else:
    # print("correct extension")
    # Can start the process here
    
    # Function
    def letterFrequency(filename, letter):
    # User is prompted for a text file.
    #fileName = input('Enter name of text file: ')
        with open(filename,'r', encoding="utf8") as file:
    
            # store content of the file in a variable
            text = file.read()
    
        # declare count variable
        count = 0
    
        # iterate through each character
        for char in text:
    
            # compare each character with
            # the given letter
            if char == letter:
                count += 1
    
        # return letter count
        #print(count)
        if count == 0:
            print("The letter " + letter + " is not contained in the txt file.")
        return count

 
    # call function and display the letter count
    print(letterFrequency(filename, 'e'))