# 15.Write a program to check whether two dictionaries are equal.

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'c': 30, 'a': 10, 'b': 25}

# Even though the order of keys is different,
# equality depends only on keys and values, not order.

result = True

if dict1.keys() != dict2.keys():
    result = False
else:
    for key in dict1:
        if dict1[key] != dict2[key]:
            result = False
            break

print("Are two dictionaries equal?\n",result)

