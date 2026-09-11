class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.place = ""
    def student_data(self):
        self.name = input("Enter Student Name: ")
        self.age = int(input("Enter the age: "))
        self.place = input("Enter the place: ")
    def display(self):
        print("----------------------------")
        print("Student Name : ",self.name)
        print("Age: ",self.age)
        print("Place: ",self.place)

obj1 = Student()
obj1.student_data()
obj1.display()