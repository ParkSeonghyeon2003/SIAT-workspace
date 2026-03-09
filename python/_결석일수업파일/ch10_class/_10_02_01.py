# 파이썬 커뮤니티의 표준 규칙인 PEP 8에서는 클래스 명명 규칙

# 파이썬 클래스 명명 규칙: PascalCase (UpperCamelCase)
# 클래스 이름은 각 단어의 첫 글자를 대문자로 쓰고, 단어 사이를 붙여서 씁니다.
# 예) MyClass, StudentInfo

# 파이썬 표준 라이브러리 중 내장 자료형이  소문자로 되어 있습니다.
# 예: list, dict, int, float, str
# 파이썬 초기부터 존재했던 아주 기본적인 타입들이라 예외적으로 소문자를 유지하고 있습니다.

# 함수(Function), 변수(Variable) 표기법은 snake_case
# 예) calculate_age(), get_data()

# 상수 (Constant) 표기법은 UPPER_SNAKE_CASE
# 예) PI, MAX_ITERATION


class Student:      # 클래스

    # 메서드
    def introduce(self):    # self: 현재 생성된 객체 자신을 참조
        print(f"안녕하세요")


# 객체 생성
s1 = Student()

# 메서드 호출
s1.introduce()  # 안녕하세요