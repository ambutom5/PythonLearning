# 12.Write a program to find all duplicate elements in a tuple.

mytuple = (3,1,2,3,1,2,3,3,4,5,6,8)
mylist = []

for i in range(len(mytuple)):
    for j in range(i+1,len(mytuple)):
        if mytuple[i] == mytuple[j] and mytuple[i] not in mylist:
            mylist.append(mytuple[i])

print(mylist)


