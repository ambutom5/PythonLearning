# 15.Write a program to split a list into two equal halves.

mylist = [1,2,3,4,5,6,7,8,9,10]
length = len(mylist)
mid = length//2

list1 = mylist[:mid]
list2 = mylist[mid:]

print(list1)
print(list2)



