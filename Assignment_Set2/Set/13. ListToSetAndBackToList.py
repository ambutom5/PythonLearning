# 13.Write a program to convert a list into a set and then back into a list without
# duplicate elements.

mylist = [5,3,2,3,1,4]
print(mylist)

myset = set(mylist)

mylist = list(myset)
print(mylist)

