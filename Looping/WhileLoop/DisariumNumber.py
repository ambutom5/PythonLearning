num = int(input("Enter the number: "))
length = len(str(num))
temp = num
sum = 0
while num >0:
    digit = num % 10
    sum += digit ** length
    num = num // 10
    length -= 1

if sum == temp:
    print("Disarium Number")
else:
    print("Not a Disarium Number")

