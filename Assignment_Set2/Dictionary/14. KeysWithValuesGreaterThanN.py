# 14.Write a program to print all keys whose values are greater than a given
# number.

mydict = {'a': 10, 'b': 20, 'c': 30,'d': 40}

num = 25

for key,value in mydict.items():
    if value > num:
        print(key,":",value)

