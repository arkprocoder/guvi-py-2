from abc import ABC, abstractmethod
import math


# abstract base classs 
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi*self.radius*self.radius

    def perimeter(self):
        return 2*math.pi*self.radius

    def hobby(self):
        print("hobby ")

        
obj=Circle(5)

print(f"Circle area is {obj.area()} & perimeter is {obj.perimeter()}")