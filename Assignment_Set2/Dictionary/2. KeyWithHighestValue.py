# 2. Write a program to find the key with the highest value.
from enum import nonmember

mydict = {"A":1,"B":2,"C":3,"D":2,"E":3,"F":4}
highestkey = None
highest = 0

for key,value in mydict.items():
    if value > highest:
        highest = value
        highestkey = key

print("Key with highest value is :",highestkey)

