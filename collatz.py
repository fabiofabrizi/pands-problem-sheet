# An attempt at the Collatz conjecture in python. 
# We ask the user to input a positive integer, then:
# If input is even, divide by 2 and add 1
# or
# If input is odd, multiply be 3 and add 1
# The program ends if the input is 1, or the current value is 1.
# Sounds like a while loop, i.e "while it's not 1, do calculations"

# Author: Fabio Fabrizi

posInt = int(input("Please enter a positive integer: "))
# checking as I go along
#out = print("the number you entered was", posInt)
if posInt == 1:
    print("Sorry, you've already reached the end of the conjecture.")
else:  
    while posInt > 1:
        if posInt % 2 == 0:
            posInt = posInt // 2
            print(posInt) # Print out the even number result
        elif posInt % 2 == 1:
            posInt = (posInt * 3) + 1
            print(posInt) # Print out the odd number result
