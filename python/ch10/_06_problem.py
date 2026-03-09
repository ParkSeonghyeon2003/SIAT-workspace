import math

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

def get_area(obj: Shape):
    return obj.area()

r = Rectangle(3, 4)
c = Circle(2)

print(f"Rectangle Area: {get_area(r)}")
print(f"Circle Area: {get_area(c)}")