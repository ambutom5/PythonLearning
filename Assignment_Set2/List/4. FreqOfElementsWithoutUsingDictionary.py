list1 = [1,2,3,1,5,4,2,1]
mylist = []

for item in list1:
    if item not in mylist:
        count = 0
        for items in list1:
            if item == items:
                count += 1
        print(item, count)
        mylist.append(item)

print()

# OR

for i in set(list1):
    print(i,list1.count(i))