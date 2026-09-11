list1 = [5,4,3,2,1]
print(list1)

print(list1[::-1])

mylist = []
for i in range(len(list1)-1,-1,-1):
    mylist.append(list1[i])
print(mylist)
