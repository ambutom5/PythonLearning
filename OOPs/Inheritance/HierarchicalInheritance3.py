class Company:
    def __init__(self):
        self.employee_id = ""
        self.name = ""
    def company_data(self):
        self.employee_id = int(input("Enter Employee ID: "))
        self.name = input("Enter Employee Name: ")
    def company_info(self):
        print("-------------Company Details-------------")
        print("Employee ID: ",self.employee_id)
        print("Employee Name: ",self.name)

class Developer(Company):
    def __init__(self):
        self.prog_lang = ""
        self.experience = ""
    def developer_data(self):
        self.prog_lang = input("Enter Programming Language: ")
        self.experience = int(input("Enter Years of Experience: "))
    def developer_info(self):
        print("-------------Developer Details-------------")
        print("Programming Language: ",self.prog_lang)
        print("Years of Experience: ",self.experience)

class Tester(Company):
    def __init__(self):
        self.testing_tool = ""
        self.bug_count = 0
    def tester_data(self):
        self.testing_tool  = input("Enter Tool Name: ")
        self.bug_count = int(input("Enter Bug Count: "))
    def tester_info(self):
        print("-------------Tester Details-------------")
        print("Testing Tool: ",self.testing_tool)
        print("Bug Count: ",self.bug_count)

class HR(Company):
    def __init__(self):
        self.department = ""
        self.employees_hired = 0
    def hr_data(self):
        self.department = input("Enter Department Name: ")
        self.employees_hired = int(input("Enter No of Employees Hired: "))
    def hr_info(self):
        print("-------------HR Details-------------")
        print("Department: ",self.department)
        print("No of Employees Hired: ",self.employees_hired)

class Manager(Company):
    def __init__(self):
        self.team_size = 0
        self.project_name = ""
    def manager_data(self):
        self.team_size = int(input("Enter Team Size: "))
        self.project_name = input("Enter Project Name: ")
    def manager_info(self):
        print("-------------Manager Details-------------")
        print("Team Size: ",self.team_size)
        print("Project Name: ",self.project_name)

obj1 = Developer()
obj1.company_data()
obj1.developer_data()
obj1.company_info()
obj1.developer_info()

obj2 = Tester()
obj2.company_data()
obj2.tester_data()
obj2.company_info()
obj2.tester_info()

obj3 = HR()
obj3.company_data()
obj3.hr_data()
obj3.company_info()
obj3.hr_info()

obj4 = Manager()
obj4.company_data()
obj4.manager_data()
obj4.company_info()
obj4.manager_info()




