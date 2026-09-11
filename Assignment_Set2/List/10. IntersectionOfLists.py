# 10.Write a program to find the intersection of two lists without using sets.

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
mylist = []

mylist = [item for item in list1 if item in list2]

# for i in list1:
#     for j in list2:
#         if i == j and i not in mylist:
#             mylist.append(i)

print(mylist)

