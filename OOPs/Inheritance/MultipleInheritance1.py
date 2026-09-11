class Father:
    def fathers_skills(self):
        print("Driving!")

class Mother:
    def mother_skills(self):
        print("Cooking!")

class Child(Father,Mother):
    def child_skills(self):
        print("Studying")

obj = Child()
obj.fathers_skills()
obj.mother_skills()
obj.child_skills()