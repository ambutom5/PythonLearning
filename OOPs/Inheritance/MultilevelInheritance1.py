class Grandfather:
    def house(self):
        print("Grandfathers House!")
class Father(Grandfather):
    def bike(self):
        print("Fathers Bike!")
class Son(Father):
    def laptop(self):
        print("Sons Laptop!")

obj1 = Son()
obj1.house()
obj1.bike()
obj1.laptop()