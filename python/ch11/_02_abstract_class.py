from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self) -> str: ...

class Dog(Animal):
    def sound(self) -> str:
        return "멍멍"

class Cat(Animal):
    def sound(self) -> str:
        return "야옹"

dog = Dog()
cat = Cat()

print(dog.sound())
print(cat.sound())
