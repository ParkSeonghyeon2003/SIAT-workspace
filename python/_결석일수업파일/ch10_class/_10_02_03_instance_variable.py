# 클래스의 기본 구조

# 학생 두 명을 만듭니다.
class Student:
    # 생성자
    # self: 현재 생성된 객체 자신을 참조
    def __init__(self, name, age): # 생성자 메서드, 객체가 생성될 때 자동 호출됨
        self.name = name           # self.name : 인스턴스 변수
        self.age = age
    
    # 메서드
    def introduce(self):        # self: 현재 생성된 객체 자신을 참조
        print(f"안녕하세요, 저는 {self.name}이고 {self.age}입니다.")

# 객체 생성
s1= Student("홍길동", 20)   # 클래스이름() 형태를 생성자 함수라고 합니다.
s2= Student("김철수", 22)

# 메서드 호출
s1.introduce()  # 안녕하세요, 저는 홍길동이고 20입니다.
s2.introduce()  # 안녕하세요, 저는 김철수이고 22입니다.

