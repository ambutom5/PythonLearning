num = int(input("Enter a number: "))
check = 0

if num < 0:
    print("Enter a positive integer!")
elif num == 0:
    print("Number is zero!")
elif num == 1:
    print("1 is a composite number!")
else:
    for i in range(2, num):
            if num % i == 0:
                print("Not Prime Number")
                break

    else:
        print("Prime Number")






