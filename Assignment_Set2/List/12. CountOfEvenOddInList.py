# 12.Write a program to count the number of even and odd numbers in a list.

mylist = [1,2,3,4,5,6,7,8,9,10]

even_count = 0
odd_count = 0

for item in mylist:
    if item % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Count of Even Numbers is : ",even_count)
print("Count of Odd Numbers is : ",odd_count)
