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

# First, import modules needed to get current working directory
# NB - This is important, as I'm making assumption that 
# the text file is located where the python code is being run.
# This time, convert to lowercase and then put in modules
import sys
import os
from typing import final

try: 
    filename = sys.argv[-1] # Get the last 
    get_ext = os.path.splitext(filename)
    ext = get_ext[1]
except (FileNotFoundError):
    cwd = os.getcwd()
    print("Your current working directory (cwd) is :\n\n{0}".format(cwd))
    print("\n")
    print("Please make sure that the text file to be checked \nis in your cwd and ends in .txt")
    print("\n")


if (ext != '.txt'):
        print("Please enter a plain text file (.txt) at the command line after running the script")
        print("The file should be entered as: es.py <filename.txt> when running")
        print("the python script from the command line")
        #print("Your current working directory (cwd) is :\n\n{0}".format(cwd))
    #break
else:
    #print(get_ext[1]) # to test what happens
    #print(filename)

    # Function
    def letterCount(filename, letter):
    # Use open() to open file
        with open(filename,'r', encoding="utf8") as file:

            # store content of the file in a variable
            text = file.read()

        # declare count variable
        count = 0

        # iterate through each character
        for char in text:
            # Convert to lowercase here
            k = char.lower()
            if k == letter:
                count += 1

        if count == 0:
            print("The letter " + letter + " is not contained in the txt file.")
        return count


    # call function and display the letter count
    print(letterCount(filename, 'e'))