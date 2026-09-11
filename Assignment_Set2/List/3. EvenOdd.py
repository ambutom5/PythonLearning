# 3. Write a program to separate even and odd numbers into two different lists.

mylist = [1,2,3,4,5,6,7,8,9,10]
list1 = []
list2 = []

for item in mylist:
    if item % 2 == 0:
        list2.append(item)
    else:
        list1.append(item)

print("Odd Number List  : ",list1)
print("Even Number List : ",list2)
