num = int(input("Enter a number: "))
length = len(str(num))
temp = num
sum =0

while num>0:
    digit = num % 10
    sum = sum + digit ** length
    num = num // 10

if sum == temp:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
