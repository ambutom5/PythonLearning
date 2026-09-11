class Company:

    def __init__(self):
        self.companyname = ""
        self.location = ""

    def companydata(self):
        self.companyname = input("Enter company name: ")
        self.location = input("Enter company location: ")

    def companyinfo(self):
        print("------Company Details------")
        print("Company Name : ",self.companyname)
        print("Location : ",self.location)

class Employee(Company):
    
    def __init__(self):
        self.employeename = ""
        self.email = ""
        self.designation = ""

    def employeedata(self):
        self.employeename = input(("Enter Employee Name: "))
        self.email = input(("Enter email id: "))
        self.designation = input("Enter Employee designation: ")

    def employeeinfo(self):
        print("--------Employee Details--------")
        print("Employee Name: ",self.employeename)
        print("Email: ",self.email)
        print("Designation: ",self.designation)

obj1 = Employee()
obj1.employeedata()
obj1.companydata()
obj1.employeeinfo()
obj1.companyinfo()