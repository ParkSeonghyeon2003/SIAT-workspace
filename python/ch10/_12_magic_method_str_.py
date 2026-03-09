class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Person: {self.name}"

obj = Person("Alice")
print(obj)
print(str(obj))
print(obj.__str__())