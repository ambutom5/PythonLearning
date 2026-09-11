class Student:                                          #
    def __init__(self,name,course):
        self.StudentName = name
        self.Course = course
    def display(self):
        print("Student Name :",self.StudentName)
        print("Course :",self.Course)

obj1 = Student("Ambu","Python")
obj1.display()

obj2 = Student("Anu","DB2")
obj2.display()