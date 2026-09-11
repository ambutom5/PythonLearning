num = int(input("Enter a number: "))
temp = num
sum = 0

while num>0:
    digit = num % 10
    sum= sum + digit
    num = num // 10
    
print(sum)

if temp % sum == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")