# 13.Write a program to update the value of a key only if the key exists in the
# dictionary.

mydict = {'a': 10, 'b': 20, 'c': 30,'d': 40}
print(mydict)

key = input("Enter the key to be updated: ")
value = input("Enter the new value of the key: ")

if key in mydict:
    mydict[key] = value

print(mydict)

