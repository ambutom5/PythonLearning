# 1. Write a program to remove duplicate elements from a list while preserving
# the original order.

# list1 = [1,2,3,1,4,3,5,1,2]
list1 = ["Apple","Banana","Apple","Apple","Guava"]
mylist = []

for item in list1:
    if item not in mylist:
        mylist.append(item)

print(mylist)