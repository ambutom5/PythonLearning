# 7. Write a program to reverse a tuple without using slicing.

mytuple = (1,2,3,4,5,6,7,8,9,10)
mylist = []

for i in range(len(mytuple)-1,-1,-1):
    mylist.append(mytuple[i])
print(tuple(mylist))

