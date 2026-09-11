class Company:
    def __init__(self):
        self.company_name = "Luminar"                               # Public Variable
    def company_info(self):                                         # Public Method
        # Accessing inside the same class
        print("Company Name: ",self.company_name)

class Employee(Company):
    def employee_info(self):
        # Accessing in the child class
        print("Company Name: ", self.company_name)

object1 = Company()                                 # Parent Class Object
object1.company_info()

object2 = Employee()                                # Child Class Object
object2.employee_info()

print(object1.company_name)                         # Accessing outside the class
