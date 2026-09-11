# 4. Write a program to convert a tuple into a list and remove duplicate elements.

mytuple = (1,2,3,1,4,5,3,1)
mylist = list(mytuple)
mylist1 = []

for item in mylist:
    if item not in mylist1:
        mylist1.append(item)

print(mylist1)


