

# 파이썬 클래스 명명 규칙: PascalCase (UpperCamelCase)
# 클래스 이름은 각 단어의 첫 글자를 대문자로 쓰고, 단어 사이를 붙여서 씁니다.
# 예) MyClass, StudentInfo

# 파이썬 표준 라이브러리 중 내장 자료형이 소문자로 되어 있습니다.
# 예: list, dict, int, float, str
# 파이썬 초기부터 존재했던 아주 기본적인 타입들이라 예외적으로 소문자를 유지하고 있습니다

# 함수 (Function), 변수 (Variable) 표기법은 snake_case
# 예) calculate_age(), get_data()

# 상수 (Constant) 표기법은 UPPER_SNAKE_CASE
# 예) PI, MAX_ITERATION

# 파이썬고등학교에 다니는 학생 두 명을 만듭니다.
class Student:
    school_name = "파이썬고등학교"      # 클래스 변수 (Class Variable)
                                    # 이 클래스로부터 생성된 모든 객체가 공유하는 데이터입니다.
    def __init__(self, name, age):
        self.name = name            # self.name : 인스턴스 변수
        self.age = age              # self.age  : 인스턴스 변수

    # 메서드
    def introduce(self):
        print(f"안녕하세요, 저는 {Student.school_name}에 다니는 {self.name}이고 {self.age}살입니다.")

# 객체(인스턴스) 생성
s1 = Student("홍길동",18)
s2 = Student("김철수",17)

# 메서드 호출
s1.introduce()      # 안녕하세요, 저는 파이썬고등학교에 다니는 홍길동이고 18살입니다.
s2.introduce()      # 안녕하세요, 저는 파이썬고등학교에 다니는 김철수이고 17살입니다.

# 클래스 변수 출력
print(Student.school_name)  # 파이썬고등학교

# 인스턴스 변수 출력 (개별적)
print(s1.name, s1.age)      # 홍길동 18
print(s2.name, s2.age)      # 김철수 17

# 클래스 변수 출력 (공유됨)
print(s1.school_name)       # 파이썬고등학교
print(s2.school_name)       # 파이썬고등학교

# 클래스 변수 변경
Student.school_name = "AI고등학교"

print(s1.school_name)       # AI고등학교
print(s2.school_name)       # AI고등학교