# 13.Write a program to create a new list containing only the duplicate elements
# from a given list.

list1 = [1,2,3,1,4,3,5,1,2]
mylist = []

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] == list1[j] and list1[j] not in mylist:
            mylist.append(list1[j])

print(mylist)


