# 7. Write a program to sort a dictionary by its values.

mydict = {'b': 40, 'a': 10, 'd': 20, 'c': 30}

# sorteddict = dict(sorted(mydict.items(),key= lambda item:item[0]))        # Sort by Key
sorteddict = dict(sorted(mydict.items(),key= lambda item:item[0]))          # Sort by Value

print(sorteddict)

