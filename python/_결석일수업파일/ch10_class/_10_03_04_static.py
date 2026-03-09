# 스태틱 메서드 (Static Metho)
# @staticmethod 데코레이터 사용
# self, cls 모두 받지 않음 -> 클래스/인스턴스 변수에 접근 불가
# 인스턴스를 생성하지 않고도 클래스이름.메서드() 형태로 바로 호출할 수 있습니다.

class Calculator:
    @staticmethod
    def add(a,b):
        return a + b
    
    @staticmethod
    def is_positive(number):
        return number > 0

# 인스턴스 생성 없이 클래스에서 직접 호출
print(Calculator.add(10,20))        # 출력: 30
print(Calculator.is_positive(-5))      # 출력: False