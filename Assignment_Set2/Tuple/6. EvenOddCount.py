# 6. Write a program to count the number of even and odd numbers in a tuple.

mytuple = (1,2,3,4,5,6,7,8,9)
evencount = 0
oddcount =0

for item in mytuple:
    if item % 2 == 0:
        evencount +=1
    else:
        oddcount +=1

print("Count of Even : ",evencount)
print("Count of Odd  : ",oddcount)