# 2. Write a program to find the second largest and second smallest elements in a
# list without using the sort() method.

from math import inf

mylist = [12,1,7,19,5]
largest = secondlargest = float(-inf)
smallest = secondsmallest  = float(inf)

for num in mylist:
    if num > largest:
        secondlargest = largest
        largest = num
    elif num > secondlargest and num != largest:
        secondlargest = num

    if num < smallest:
        secondsmallest = smallest
        smallest = num
    elif num < secondsmallest and num != smallest:
        secondsmallest = num

print("Second Smallest Number Is: ",secondsmallest)
print("Second Largest Number Is: ",secondlargest)
