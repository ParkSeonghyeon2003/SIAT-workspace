from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self): ...

try:
    a = Animal()
except TypeError as e:
    print(f"에러 발생: {e}")
