# An attempt at the Collatz conjecture in python. 
# We ask the user to input a positive integer, then:
# If input is even, divide by 2 and add 1
# or
# If input is odd, multiply be 3 and add 1
# The program ends if the input is 1, or the current value is 1.
# Sounds like a while loop, i.e "while it's not 1, do calculations"

# Author: Fabio Fabrizi

# Old version
"""
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
"""
# New version below - Checks that the user has entered a valid integer
# and if so, carries on with calculating collatz.
# Also made the output a bit nicer - put into list, appended and printed 
# as that's what it looked like on the page.
#
# Put the collatz conjecture into a module and separated the error checking
# Lots more lines of code but maybe more robust?
# Looking down the road - maybe something like Numpy for big exploration of conjecture?

if __name__ == '__main__':
    number = 0
    while True:
        num = input("Please enter an integer: ")
        nice_Out = [] # Have it in the format displayed on the page - horizontally
        try:
            posInt = int(num)
            #print("Input is an integer number.")
            #print("Input number is: ", posInt)
            break
        except ValueError:
            print("This is not an integer. Please enter an integer: ")
            #break
    number = num
    #print(number)
    def collatz(posInt):
        #number = posInt
        posInt = int(posInt)
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
            #print(nice_Out)
        # code above here
        #break
        if len(nice_Out) > 1:
            return nice_Out
        else:
            return posInt
    print(collatz(number))