# 6. Write a program to sort a dictionary by its keys.

mydict = {'b': 20, 'a': 10, 'd': 40, 'c': 30}

sorteddict = dict(sorted(mydict.items()))                                    # Sort by Key

# sorteddict = dict(sorted(mydict.items(),reverse="True"))                   # Reverse Order

# sorteddict = dict(sorted(mydict.items(),key= lambda item:item[0]))         # Sort by Key

print(sorteddict)
