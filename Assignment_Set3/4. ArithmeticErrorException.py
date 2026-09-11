# 4. Write a Python program that executes division and handles an ArithmeticError
# exception if there is an arithmetic error.

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1/num2
    print(result)

except ArithmeticError:
    print("Arithmetic Error!")


