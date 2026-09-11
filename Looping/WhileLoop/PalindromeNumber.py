num = int(input("Enter the number: "))
length = len(str(num))
temp = num
sum = 0

while num>0:
    digit = num % 10
    sum = sum + digit * 10**(length-1)
    num = num//10
    length -= 1

if sum == temp:
    print("Palindrome")
else:
    print("Not Palindrome")
