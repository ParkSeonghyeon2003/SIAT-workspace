# 데코레이터는 함수를 인자로 받아 새로운 함수를 반환하는 함수입니다.
# 그 반환값이 기존 함수 이름에 다시 바인딩됩니다.
# 기존 함수를 수정하지 않고, 그 함수의 앞뒤에 새로운 기능을 추가하고 싶을 때 사용합니다.

def my_decorator(func):
    def wrapper():
        print("--- 함수 실행 시작 ---")
        func()  # 실제 함수 호출
        print("--- 함수 실행 종료 ---")
    return wrapper


# 함수 위에 @기호와 데코레이터 이름을 붙이면 hello = my_decorator(hello) 와 같이 동작합니다.
# 원래의 hello 함수는 데코레이터에 전달되고 데코레티어가 변환한 새로운 함수가 hello 라는 이름에 다시 할당됩니다.
@my_decorator
def hello():
    print("안녕하세요!")

# 데코레이터
hello()