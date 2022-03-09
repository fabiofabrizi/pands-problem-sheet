# This is the weekly task from Week 8
# Write a program called plottask.py that displays a plot 
# of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the 
# range [0, 4] on the one set of axes.
#
# Fabio Fabrizi
# References:
# https://stackoverflow.com/questions/24391892/printing-subscript-in-python
# https://unicode-table.com/en/00B3/

# From the instructions, sounds like the initial array can 
# be put into numpy, then manipulated in order to get the plots needed.

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(0, 4))
# for f(x)
ypoints = xpoints
ypoints2 = xpoints * xpoints
ypoints3 = xpoints ** 3
plt.plot(xpoints, ypoints, marker = "d", label = "f(x) = x")
plt.plot(xpoints, ypoints2, marker = "o", label = "g(x) = x\u00b2", color = "red")
plt.plot(xpoints, ypoints3, marker = "v", label = "h(x) = x\u00b3", color = "green")
plt.title("Week 8 Weekly Task")
plt.xlabel("Input Range")
plt.ylabel("Output Results")
plt.legend()

plt.show()