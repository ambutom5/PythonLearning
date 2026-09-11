# 5. Write a program to merge two sorted lists into a single sorted list.

list1 = [2,3,6,10,12,15]
list2 = [1,4,5,7,8,9]
mylist = []
i = 0
j = 0

while i < len(list1) and j < len(list2):
    if list1[i]<list2[j]:
        mylist.append(list1[i])
        i += 1
    else:
        mylist.append(list2[j])
        j += 1

mylist.extend(list1[i:])
mylist.extend(list2[j:])
print(mylist)