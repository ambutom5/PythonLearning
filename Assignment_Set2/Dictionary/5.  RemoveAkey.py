# 5. Write a program to remove a key from a dictionary without using the pop() method.

mydict = {'a': 10, 'b': 20, 'c': 30,'d': 40}

keytoremove = 'd'

if keytoremove in mydict:
    del mydict[keytoremove]

print(mydict)

