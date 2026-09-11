# 7. Write a program to find all prime numbers present in a list.

list1 = [2,3,7,4,13,87,1,17,6,8,11,12]
mylist = []

for item in list1:
    for i in range(2,item):
        if item % i == 0:
            break
    else:
        if item != 1 and item != 2:
            mylist.append(item)

print(mylist)
