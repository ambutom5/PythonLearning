# 7. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def substraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "Error! Division by Zero"

    def result(self):
        print("Addition Result          :   ", self.addition())
        print("Substraction Result      :   ", self.substraction())
        print("Multiplication Result    :   ", self.multiplication())
        print("Division Result          :   ", self.division())

obj1 = Calculator(10,0)
obj1.result()



