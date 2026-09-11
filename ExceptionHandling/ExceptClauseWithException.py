try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print(num1/num2)

except ZeroDivisionError:
    print("Division By Zero! You can't divide by Zero")