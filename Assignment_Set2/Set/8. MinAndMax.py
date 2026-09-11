# 8. Write a program to find the maximum and minimum elements in a set.

numbers = {12, 45, 7, 23, 89, 3, 15}

max = None
min = None

for num in numbers:
    if min == None or num < min:
        min = num
    if max == None or num > max:
        max = num

print("Minimum: ",min)
print("Maximum: ",max)
