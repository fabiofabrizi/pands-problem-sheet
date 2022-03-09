# This is an attempt at the task for Week 6.
# Write a program that takes a positive floating-point number as it's input 
# and outputs an approximation of it's square root.
# A function called sqrt has to be created - not allowed to use the built-in 
# square root function.
# I looked at the following websites for the calculations:
# https://www.school-for-champions.com/algebra/square_root_approx.htm#.YheTzOjP0Q8
# https://en.wikipedia.org/wiki/Newton%27s_method

# I'm going to check whether the user enters a positive float and if not, prompt them to do so.
# I'm also going to set guess initially to 5, but will check as I go along how close the 
# iteration is to the square root of num, then stop.
# As we're talking of iterations, a loop is needed. 

# Author: Fabio Fabrizi

# Formula:
# √num = 0.5 * ((num/guess) + guess)

def newtonSquareRoot(num):
    guess = 0.5*num
    numRoot = 0.5 * (guess + (num/guess))
    while numRoot != guess:
        guess = numRoot
        numRoot = 0.5*(guess + (num/guess))
    return guess
# print(newtonSquareRoot(num))

# guess = 5

while True:
    num = float(input("Please enter a positive number: "))
    if num < 0:
        print("That wasn't a positive number. Please try again.")
    else:
        print("The square root of {} is {}".format(num, newtonSquareRoot(num)))
        
        # Test the loop
        # print("The square of your number is " + str(round(num ** 2)))
        # Calculation time

        # Don't forget to add a break to break out the loop after checking iteration
        break
    
print("Thanks for following instructions!") # You can put final message here
