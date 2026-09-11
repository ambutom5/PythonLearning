# 8. Write a program to find the sum of all numeric elements in a tuple.

mytuple = ("Apple",1,2,3,"Banana",4.0,"Cherry",3+2j)
sum = 0

for item in mytuple:
    if type(item) in (int,float,complex):
        sum += item

print("Sum of Numeric Elements: ",sum)


