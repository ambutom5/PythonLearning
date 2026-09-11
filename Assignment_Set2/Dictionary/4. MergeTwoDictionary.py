# 4. Write a program to merge two dictionaries. If a key exists in both, add their
# values.

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

print(dict1)
print(dict2)

merged = dict1.copy()

for key,value in dict2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value
print(merged)
