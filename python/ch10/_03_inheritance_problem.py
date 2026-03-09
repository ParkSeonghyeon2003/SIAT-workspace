class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"안녕하세요, 저는 {self.name}입니다.")

class Student(Person):
    def study(self):
        print(f"{self.name}이(가) 공부합니다.")

class Teacher(Person):
    def teach(self):
        print(f"{self.name} 선생님이 수업을 합니다.")

student = Student("철수")
student.greet()
student.study()

teacher = Teacher("민수")
teacher.greet()
teacher.teach()