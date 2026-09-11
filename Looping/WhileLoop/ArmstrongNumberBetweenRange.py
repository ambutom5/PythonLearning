lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

for num in range(lower,upper+1):
    temp = num
    length = len(str(num))
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum + digit ** length
        num = num // 10

    if sum == temp:
        print(temp)