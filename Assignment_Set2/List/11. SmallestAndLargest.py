# 11.Write a program to find the largest and smallest elements in a list without
# using max() and min().

mylist = [10,2,3,4,1,15,6,7,8,9,10]

smallest = mylist[0]
largest = mylist[0]

for item in mylist:
    if item < smallest:
        smallest = item
    elif item > largest:
        largest = item

print("Largest Element is: ",largest)
print("Smallest Element is: ",smallest)