2# 13. Write a Python program to determine whether a given year is a leap year.

year = int(input("Enter the year: "))
flag = True

if year % 4 != 0:
    flag = False
elif year % 100 == 0 and year % 400 != 0:
    flag = False

print(flag)
