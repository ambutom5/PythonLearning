lower = int(input("Enter a lower limit: "))
upper = int(input("Enter an upper limit: "))

for num in range(lower, upper + 1):
    length = len(str(num))
    temp = num
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum + digit ** length
        num = num // 10
        length -= 1
    if sum == temp:
        print(temp)
