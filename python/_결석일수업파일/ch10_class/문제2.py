class Student:
    school_name = "파이썬 고등학교"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"안녕하세요, 제 이름은 {self.name}이고 {self.age}살 입니다.")

    @classmethod
    def school_info (cls):
        print(f"저희 학교는 {Student.school_name}입니다.")

    @staticmethod
    def welcome():
        print("학생 여러분, 환영합니다!")

s1 = Student("홍길동",18)
s1.introduce()

Student.school_info()
Student.welcome()