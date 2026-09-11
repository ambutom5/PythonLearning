class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addition(self):
        sum = self.a + self.b
        print(sum)
    def difference(self):
        diff = self.a - self.b
        print(diff)
    def multiplication(self):
        mult = self.a * self.b
        print(mult)
    def division(self):
        try:
            div = self.a/self.b
        except ZeroDivisionError:
            print("Error! Division By zero!")
        else:
            print(div)

obj1 = Calculator(10,0)

while True:

    print("------------CALCULATOR----------")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    choice = int(input("Enter a choice: "))

    if choice == 1:
        obj1.addition()
    elif choice == 2:
        obj1.difference()
    elif choice == 3:
        obj1.multiplication()
    elif choice == 4:
        obj1.division()
    elif choice == 5:
        break
    else:
        print("Invalid Choice")
