# This is the weekly task from Week 2, Programming and Scripting
#
# Author: Fabio Fabrizi
#
"""
Formula from https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_1.html#:~:text=With%20the%20metric%20system%2C%20the,by%2010%2C000%2C%20can%20be%20used.
From above, this gives two formulas:
weight (kg) / [height (m)]**2
OR
[weight (kg) / height (cm) / height (cm)] x 10,000

https://en.wikipedia.org/wiki/Unicode_subscripts_and_superscripts
The above was used to get the output exactly like how it is in the 
instructions, ie superscript
I'm going to start with the first formula as it looks simpler

"""
weight = input("Enter your weight (kg): ")
height = input("Enter your height (cm): ")

# Was using the below to check inputs
# print("Your weight is " + weight, "and your height is " + height)

# Rough version 
# print(int(weight) / (int(height)/100)**2)

# Assign calculation to variable and print
bmi = int(weight) / (int(height)/100)**2
bmi2 = float(weight) / (float(height)/100)**2
# Check to see rounding works - we want two decimal places like instructions
#print(round(bmi,2))

result = str(round(bmi,2))
#print("Your BMI (kg/m2) is " + result)
print("Your BMI (kg/m\u00b2) is {}".format(result))


# The decision to use round() was based on having accuracy to one decimal place.
# integer division was initally used, i.e. x // y, but I felt that the calculation
# with the decimal point was more accurate.
