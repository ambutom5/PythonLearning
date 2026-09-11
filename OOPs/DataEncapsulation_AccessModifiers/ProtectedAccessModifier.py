class Student:
    def __init__(self):
        self._marks = 90                                    # Protected Variable
    def display(self):
        #Accessing in the same class
        print("Total Marks: ",self._marks)

class Myclass(Student):
    def class_data(self):
        print("------------ Student Data ------------")
        # Accessing in the child class
        print("Total Marks: ",self._marks)

object1 = Myclass()
object1.display()
object1.class_data()

# Accessing is possible outside the class.
# Python doesn't support protected access modifier.
print(object1._marks)