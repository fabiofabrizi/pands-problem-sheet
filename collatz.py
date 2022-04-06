# An attempt at the Collatz conjecture in python. 
# We ask the user to input a positive integer, then:
# If input is even, divide by 2 and add 1
# or
# If input is odd, multiply be 3 and add 1
# The program ends if the input is 1, or the current value is 1.
# Sounds like a while loop, i.e "while it's not 1, do calculations"

# Author: Fabio Fabrizi

# Seperated the error checking and conjecture into functions
# Error checking of the input is below.
# https://docs.python.org/3/tutorial/errors.html#handling-exceptions
#
# Grouped the Exceptions together to try and make it tidier

def main():
    while True:
        try:
            number = int(input("Please enter a positive integer: "))
            assert number > 0
            print("The number you entered was ", number)
            posInt = number
            #if num > 0:
            break
        except (ValueError, TypeError, AssertionError):
            print("You have to enter a positive integer")
    #print("The value of x is ", posInt)
    return posInt

x = main()
posInt = x
# Collatz conjecture implemented below
def collatz(posInt):
        #posInt = x
        #posInt = int(posInt)
        nice_Out = [] # Have it in the format displayed on the page - horizontally
        if posInt == 1:
            print("Sorry, you've already reached the end of the conjecture.")
        else:  
            while posInt > 1:
                if posInt % 2 == 0:
                    posInt = posInt // 2
                    #print(posInt) # Print out the even number result
                    nice_Out.append(posInt)
                elif posInt % 2 == 1:
                    posInt = (posInt * 3) + 1
                    #print(posInt) # Print out the odd number result
                    nice_Out.append(posInt)
            print(nice_Out)
        # code above here
        #break
        if len(nice_Out) > 1:
            return nice_Out
        else:
            return posInt
        #print(collatz(posInt))
collatz(posInt)
