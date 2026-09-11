# 1. Write a program to find the sum of all values in a dictionary.

mydict = {"A":1,"B":2,"C":3,"D":2,"E":3,"F":4}
sum = 0

for item in mydict.values():
    sum += item

print("Sum of Values in Dictionary is",sum)

