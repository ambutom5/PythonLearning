# 14.Write a program to swap the first and last elements of a list.

list1 = [10,2,3,4,5,6,7,8,9,1]

temp = list1[0]
list1[0] = list1[-1]
list1[-1] = temp

print(list1)

