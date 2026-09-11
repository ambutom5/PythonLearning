mylist = [30,44,98,66,909]


for item in range(len(mylist)):
    num = mylist[item]
    temp = num
    length = len(str(temp))
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum = sum + digit * 10 ** (length - 1)
        temp = temp // 10
        length -= 1

    if sum == num:
        print(mylist[item])
