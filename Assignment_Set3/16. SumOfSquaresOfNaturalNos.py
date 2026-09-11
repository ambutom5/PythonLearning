# 16. Python Program for Sum of squares of first n natural numbers

n = int(input("Enter N: "))
sum = 0
for i in range(n+1):
    sum += i*i
print("Sum is : ", sum)

