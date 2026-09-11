from abc import ABC, abstractmethod
class Animal(ABC):                                        # Parent Class
    @abstractmethod
    def sound(self):                                    # Abstract Method
        pass
# Every class that inherits from Animal must provide its own implementation
#     of sound() method

class Cat(Animal):            # Child class of Animal, it also implements sound() method
    def sound(self):
        print("Cat Meows!")

class Dog(Animal):
    def sound(self):
        print("Dog Barks!")

# Obj = Animal()                      # Cannot create object for Animal Class directly

obj1 = Cat()
obj1.sound()

obj2 = Dog()
obj2.sound()