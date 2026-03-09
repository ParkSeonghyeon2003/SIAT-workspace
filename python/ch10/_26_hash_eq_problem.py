class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            raise TypeError("Rectangle 객체 끼리만 == 연산이 가능합니다.")
        return self.width == other.width and self.height == other.height
    
    def __hash__(self) -> int:
        return hash((self.width, self.height))

r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
r3 = Rectangle(20, 10)

print(r1 == r2)
print(r1 == r3)

s = {r1, r2, r3}
print(len(s))