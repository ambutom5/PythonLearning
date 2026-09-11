class Employee:
    def __init__(self, id, name, company, designation, salary):
        self.id = id
        self.name = name
        self.company = company
        self.designation = designation
        self.salary = salary

    def display(self):
        print("------------------------------")
        print("Employee Id: ",self.id)
        print("Employee Name: ", self.name)
        print("Company Name: ", self.company)
        print("Designation: ", self.designation)
        print("Salary: ", self.salary)

obj1 = Employee(id = 101,name="Anu",company="CTS",salary=5000,designation="SA")
obj1.display()

obj2 = Employee(id = 102,name="Ambu",company="CTS",salary=1000,designation="A")
obj2.display()
