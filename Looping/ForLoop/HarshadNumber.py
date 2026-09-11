num = int(input("Enter a number: "))

sum = 0

for i in str(num):
    print(i)
    sum = sum + int(i)

print("Sum of digits is: ", sum)

if num % sum == 0:
    print("Harshad Number!")
else:
    print("Not Harshad Number!")