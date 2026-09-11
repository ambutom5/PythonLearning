num = int(input("Enter the number: "))
temp = num
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10

if sum == temp:
    print("Armstrong Number")

else:
    print("Not an Armstrong Number")

