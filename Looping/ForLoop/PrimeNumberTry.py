num = int(input("Enter a number: "))
check = 0

for i in range(2,num):
    remainder = num % i
    # print(remainder)
    if remainder == 0:
        check = 1
        break

if check == 1:
    print("Not Prime Number")
else:
    print("Prime Number")
