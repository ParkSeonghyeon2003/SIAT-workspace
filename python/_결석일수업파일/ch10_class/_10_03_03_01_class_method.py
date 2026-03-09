# 클래스 메서드 (Class Method)
# @classmethod 데코레이터 사용
# 첫 번째 매개변수는 cls -> 클래스 변수에 접근 가능


class Student:
    count = 0           # [클래스 변수] 모든 인스턴스가 공유하는 변수

    # 생성자
    # self: 현재 생성된 객체 자신을 참조
    def __init__(self):
        Student.count += 1      # 새로운 학생이 생성될 때마다 클래스 변수 count를 1씩 증가

    #[클래스 메서드 데코레이터] 이 메서드가 클래스 메서드임을 파이썬에 알립니다.
    @classmethod
    def print_count(cls):   # cls는 Student 클래스 그 자체입니다. cls.count는 Student.count와 똑같은 의미가 됩니다.
        print(f"{cls.count}명이 입학했습니다.")

# 클래스에서 직접 호출
Student.print_count()   # 0명이 입학했습니다.

# 객체 생성
kim = Student()
Student.print_count()   # 1명이 입학했습니다.

# 객체 생성
lee = Student()
Student.print_count()   # 2명이 입학했습니다.

kim.print_count()