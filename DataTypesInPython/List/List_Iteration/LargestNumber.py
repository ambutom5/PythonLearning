list1 = [11,20,35,4,5,6]
largest = list1[0]

for item in range(len(list1)):
    if list1[item] > largest:
        largest = list1[item]

print(largest)

#BuiltIn Functions
print(max(list1))
print(min(list1))
print(sum(list1))