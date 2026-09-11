# 3. Write a program to find the maximum and minimum elements in a tuple.

mytuple = (1,20,3,6,4,5,3,9)
lowest = mytuple[0]
highest = mytuple[0]

for item in mytuple:
    if item > highest:
        highest = item
print("Maximum is: ",highest)

for items in mytuple:
    if items < lowest:
        lowest = items
print("Minimum is: ",lowest)


