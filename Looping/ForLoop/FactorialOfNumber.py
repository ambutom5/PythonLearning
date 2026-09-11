num = int((input("enter a number:")))
factorial = 1

for i in range(1,num+1,1):

    print(factorial,"*",i)
    # factorial = factorial * i
    factorial *= i


print(factorial)