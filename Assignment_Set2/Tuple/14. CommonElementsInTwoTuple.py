# 14.Write a program to compare two tuples and display the common elements.

tuple1 = (8,2,3,5,1,4,7,6)
tuple2 = (10,12,3,5,15,20)
mylist = []

for item in tuple1:
    for items in tuple2:
        if item == items and item not in mylist:
            mylist.append(item)

print(mylist)

