num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print("Before swapping, Value of Num1: ",num1)
print("Before swapping, Value of Num2: ",num2)

num1=num1+num2
num2=num1-num2
num1=num1-num2

print("After swapping, Value of Num1: ",num1)
print("After swapping, Value of Num2: ",num2)