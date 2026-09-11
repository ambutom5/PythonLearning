# Sample Input
# 08 05 2015

# Sample Output
# WEDNESDAY

import datetime

month, day, year = map(int, input().split())                         # Read input

x = datetime.date(year, month, day)                         # Create a date object

print(x.strftime("%A").upper())                 # Print the weekday name in uppercase


# Input format: month day year (problem statement).
# Python’s datetime.date: year, month, day (ISO standard).