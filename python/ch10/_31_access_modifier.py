class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name =name
        self._nickname = "친구"
        self.__age = age

    def show_info(self) -> None:
        print(f"이름: {self.name}, 닉네임: {self._nickname}, 나이: {self.__age}")

p1 = Person("지민", 25)
print(p1.name)
print(p1._nickname)

print(p1._Person__age)

p1.show_info()