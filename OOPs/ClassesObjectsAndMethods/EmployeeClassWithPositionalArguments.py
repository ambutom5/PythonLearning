class Employee():
    def __init__(self, id, name, place, company,salary, designation):
        self.EmployeeId = id
        self.EmployeeName = name
        self.Place = place
        self.Company = company
        self.Salary = salary
        self.Designation = designation
    def display(self):
        print("Employee ID: ",self.EmployeeId)
        print("Employee Name: ",self.EmployeeName)
        print("Place: ",self.Place)
        print("Company: ",self.Company)
        print("Salary: ",self.Salary)
        print("Designation: ",self.Designation)

obj1 = Employee(101,"Ambu","Kochi","CTS",5000,"Associate")
obj1.display()

obj2 = Employee(102,"Anu","NZ","CTS",9000,"SA")
obj2.display()

obj3 = Employee(103,"Leo","Kochi","Rajagiri",10,"Student")
obj3.display()
