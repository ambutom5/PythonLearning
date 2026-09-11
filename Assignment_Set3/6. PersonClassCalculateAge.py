from datetime import date,datetime

class Person:
    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        # dob should be a string in YYYY-MM-DD format
        self.dob = datetime.strptime(dob,"%Y-%m-%d").date()
    def calculate_age(self):
        today = date.today()
        age =  today.year - self.dob.year
        # Adjust if birthday hasn’t occurred yet this year
        if (today.month,today.day) < (self.dob.month,self.dob.day):
            age -= 1
        return age
    def display_age(self):
        print("Name    : ",self.name)
        print("Country : ", self.country)
        print("Dob     : ", self.dob)
        print("Age     : ", self.calculate_age())

obj1 = Person("Alice", "India", "1990-10-05")
obj1.display_age()
