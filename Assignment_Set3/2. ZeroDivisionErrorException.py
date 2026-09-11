# 2. Write a Python program to handle a ZeroDivisionError exception when dividing
# a number by zero.

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1/num2
    print(result)

except ZeroDivisionError:
    print("Division By Zero Error!")






