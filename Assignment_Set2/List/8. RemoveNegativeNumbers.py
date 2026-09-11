# 8. Write a program to remove all negative numbers from a list.

list1 = [2,-3,0,-7,4,13,-87,1,17,-6,8,11,12]

for item in list1:
    if item<0:
        list1.remove(item)

print(list1)

