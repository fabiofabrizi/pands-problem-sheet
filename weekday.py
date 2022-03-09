# This is from Week 5
# Write a program that outputs whether or not today is a weekday.

# Fabio Fabrizi

from datetime import datetime

from sniffio import current_async_library

# strftime() converts a datetime object to different string formats.
#print(datetime.today().strftime('%A')) # %A is the full weekday name
current_day = datetime.today().strftime('%A')
# print(current_day)

# Now write a simple loop
if (current_day == "Saturday") or (current_day == "Sunday"):
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday")