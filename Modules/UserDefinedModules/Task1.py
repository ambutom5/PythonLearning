import mymodule
from mymodule import substraction
import mymodule as x

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(mymodule.addition(num1, num2))
print(substraction(num1,num2))
print(x.multiply(num1,num2))
print(x.division(num1,num2))
