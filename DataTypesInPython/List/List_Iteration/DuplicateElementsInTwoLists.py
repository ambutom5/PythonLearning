list1 = [11,2,20,35,4,2,20,5,6,2,4]
list2 = [1,2,35,3,6]
mylist = []

for i in list1:
    for j in list2:
        if i == j and i not in mylist:
            mylist.append(i)
print(mylist)

# OR
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i] == list2[j] and list1[i] not in mylist:
#             mylist.append(list1[i])
#
# print(mylist)

