class Employee:
    def __init__(self):
        self.name = "Anu"
        self.__salary = 20000
    def display(self):
        print("Name : ",self.name)
        print("Salary: ",self.__salary)

obj1 = Employee()
obj1.display()

print("-----Outside Class-----")
print(obj1.name)
# print(obj1.__salary)             # Cannot access private variable outside the class