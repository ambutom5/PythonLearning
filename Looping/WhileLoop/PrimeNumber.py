num = int(input("Enter the limit of number: "))
flag = 0
i = 2
while i < num:
    if num %i == 0:
        flag = 1
        print("Not a prime number")
        break
    i = i + 1
if flag == 0:
    print("Prime Number")

