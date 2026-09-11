# 11.Write a program to check whether a given key exists in a dictionary.

dict1 = {'a': 10, 'b': 20, 'c': 30}

mykey = input("Enter the key: ").upper()

if mykey in dict1:
    print(mykey,"present in the dictionary")
else:
    print(mykey,"not present in the dictionary")

    