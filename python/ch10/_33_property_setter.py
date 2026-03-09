class Person:
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str) -> None:
        if len(value) > 1:
            self.__name = value
        else:
            print("이름이 너무 짧습니다.")

p = Person("Alice")
print(p.name)
p.name = "Bob"
print(p.name)
p.name = "A"
print(p.name)