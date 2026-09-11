# 15.Write a program to check whether two dictionaries are equal.

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'c': 30, 'a': 10, 'b': 20}

# Even though the order of keys is different,
# equality depends only on keys and values, not order.

if dict1 == dict2:
    print("The dictionaries are equal")
else:
    print("The dictionaries are not equal")

