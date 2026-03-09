class Person:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Person('{self.name}')"

p1 = Person("Alice")
print(p1)

# 파이썬은 __str__을 확인해서 사용자용 문자열이 먼저 있는지를 확인한다.
# 만약 __str__이 없으면 __repr__을 사용한다.

people = [Person("Alice"), Person("Bob")]
print(people)

print(repr(people))