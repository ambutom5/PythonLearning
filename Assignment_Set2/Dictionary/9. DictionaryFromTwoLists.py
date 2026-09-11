# 9. Write a program to create a dictionary from two lists (one containing keys
# and the other values).

keys = ["A","B","C","D","E"]
values = [1,2,3,4,5]

mydict = {keys[i]:values[i] for i in range(len(keys))}

print(mydict)
