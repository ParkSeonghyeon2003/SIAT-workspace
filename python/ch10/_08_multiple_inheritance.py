class RectangleArea:
    def rectangle_area(self, width, height):
        return width * height
    
import math

class CircleArea:
    def circle_area(self, radius):
        return math.pi * radius ** 2
    
class ShapeCalculator(RectangleArea, CircleArea): ...

calc = ShapeCalculator()

rect = calc.rectangle_area(3, 4)
print("사각형 면적:", rect)

circle = calc.circle_area(2)
print("원 면적:", circle)

# ShapeCalculator는 사각형 면적과 원의 면적 구하는 기능을 사용할 수 있습니다.
# 다중 상속을 기능 조합 (Mixin) 용도로 사용하고 있습니다.