list1 = [11,2,20,35,4,2,20,5,6,2,4]
mylist = []

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] == list1[j] and list1[i] not in mylist:
            mylist.append(list1[i])

print(mylist)

