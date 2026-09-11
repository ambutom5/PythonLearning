# 5. Write a program to find the index of a given element without using the
# index() method.

mytuple = ("Apple","Banana","Cherry","Mango")
mydict = {}

for i in range(len(mytuple)):
    mydict[mytuple[i]] = i

for key,value in mydict.items():
    print(key,":",value)

print(mydict["Banana"])
