class College:
    def __init__(self):
        self.college_name = ""
        self.location = ""
        self.contact_number = 0
    def college_data(self):
        self.college_name = input("Enter College Name: ")
        self.location = input(("Enter College Location: "))
        self.contact_number = int(input("Enter Contact Number: "))
    def college_info(self):
        print("-----------------College Info-----------------")
        print("College Name: ",self.college_name)
        print("College Location: ",self.location)
        print("Contact Number: ",self.contact_number)

class Department(College):
    def __init__(self):
        self.Dept_Id = 0
        self.dept_name = ""
        self.HOD = ""
    def department_data(self):
        self.Dept_Id = int(input("Enter Dept Id: "))
        self.dept_name = input("Enter Dept Name: ")
        self.HOD = input("Enter HOD Name: ")
    def department_info(self):
        print("-----------------Department Info-----------------")
        print("Department Id: ",self.Dept_Id)
        print("Department Name: ",self.dept_name)
        print("HOD: ",self.HOD)

class Student(Department):
    def __init__(self):
        self.Stud_Id = 0
        self.Name = ""
        self.Course = ""
        self.place = ""
        self.mobile = 0
    def student_data(self):
        self.Stud_Id = input("Enter Student Id: ")
        self.Name = input("Enter Student Name: ")
        self.Course = input("Enter Course: ")
        self.place = input("Enter Place: ")
        self.mobile = input("Enter Mobile Number: ")
    def student_info(self):
        print("-----------------Student Info-----------------")
        print("Student Id:",self.Stud_Id)
        print("Student Name: ",self.Name)
        print("Course: ",self.Course)
        print("Place: ",self.place)
        print("Mobile Number: ",self.mobile)

obj1 = Student()
obj1.student_data()
obj1.department_data()
obj1.college_data()
obj1.student_info()
obj1.department_info()
obj1.college_info()
