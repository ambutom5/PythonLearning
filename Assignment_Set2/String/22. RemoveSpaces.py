# 22.Write a program to remove all spaces from a string without using the
# replace() method.

mystring = "This is a python program"

words = mystring.split()

newstring = "".join(words)

print(newstring)



