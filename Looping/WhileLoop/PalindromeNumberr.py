num = int(input("Enter the number: "))
temp = num
sum = 0
while num > 0:
    digit = num % 10
    sum = sum * 10 + digit
    num = num//10

if sum == temp:
    print("Palindrome")
else:
    print("Not Palindrome")
