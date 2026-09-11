class Employee:
    def company(self):
        print("Company Name: Luminar")

class Manager(Employee):
    def manage(self):
        print("Manages the team!")

class Developer(Employee):
    def develop(self):
        print("Developer develops the code!")

obj1 = Manager()
obj1.manage()
obj1.company()

obj2 = Developer()
obj2.develop()
obj2.company()