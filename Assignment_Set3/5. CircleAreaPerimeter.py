# 5. Write a Python program to create a class representing a Circle. Include methods
# to calculate its area and perimeter.

class Circle:
    def __init__(self,r):
        self.radius = r
        
    def area_circle(self):
        self.area = 3.14 * (self.radius**2)
        print("Area of Circle: ",self.area)

    def perimeter_circle(self):
        self.perimter = 2 * 3.14 * self.radius
        print("Perimeter of Circle: ", self.perimter)

obj1 = Circle(7)
obj1.area_circle()
obj1.perimeter_circle()