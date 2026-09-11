class Person:
    def __init__(self):
        self.Name = ""
        self.Age = 0
        self.Place = ""
        self.MobileNumber = 0
        self.EmailId = ""
    def person_details(self):
        self.Name = input("Enter Person Name: ")
        self.Age = int(input("Enter Age: "))
        self.Place = input("Enter Place: ")
        self.MobileNumber = int(input("Enter Mobile Number: "))
        self.EmailId = input("Enter Email Id: ")
    def person_info(self):
        print("----------Person Details------------")
        print("Person Name: ",self.Name)
        print("Age: ",self.Age)
        print("Place: ",self.Place)
        print("Mobile Number: ",self.MobileNumber)
        print("Email Id: ",self.EmailId)

class Salary:
    def __init__(self):
        self.basic_salary = 0
        self.bonus = 0
        self.doj = 0
    def salary_details(self):
        self.basic_salary = int(input("Enter Basic Salary: "))
        self.bonus = int(input("Enter Bonus Pay: "))
        self.doj = int(input("Enter DOJ: "))
    def salary_info(self):
        print("----------Salary Details------------")
        print("Basic Salary: ",self.basic_salary)
        print("Bonus: ",self.bonus)
        print("DOJ: ",self.doj)

class Employee(Person,Salary):
    def __init__(self):
        self.EmployeeId = 0
        self.designation = ""
    def employee_details(self):
        self.EmployeeId = int(input("Enter Employee Id: "))
        self.designation = input("Enter Designation: ")
    def employee_info(self):
        print("----------Employee Details------------")
        print("Employee Id: ",self.EmployeeId)
        print("Designation: ",self.designation)

obj1 = Employee()
obj1.person_details()
obj1.employee_details()
obj1.salary_details()

obj1.person_info()
obj1.employee_info()
obj1.salary_info()

