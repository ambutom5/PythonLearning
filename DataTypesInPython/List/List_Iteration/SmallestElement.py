list1 = [11,20,35,4,5,6]
smallest = list1[0]

for item in range(len(list1)):
    if list1[item] < smallest:
        smallest = list1[item]

print(smallest)

