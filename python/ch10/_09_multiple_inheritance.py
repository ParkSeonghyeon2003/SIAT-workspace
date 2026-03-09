class RectangleArea:
    def area(self, width, height):
        print("RectangleArea의 area()")
        return width * height

class TriangleArea:
    def area(self, width, height):
        print("TriangleArea의 area()")
        return (width + height) / 2

class ShapeCalculator(RectangleArea, TriangleArea): ...

calc = ShapeCalculator()

rect = calc.area(3, 4)
print(rect)

tri = calc.area(2, 3)
print(tri) # RectangleArea 메서드가 호출됨

# Method Resolution Order
print(ShapeCalculator.mro())