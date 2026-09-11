list1 = [1,2,3,4,5]
mylist = []

# Without Using List Comprehension
for i in list1:
    mylist.append(i**2)
print(mylist)

# Using List Comprehension
mylist = [i**2 for i in list1]
print(mylist)
