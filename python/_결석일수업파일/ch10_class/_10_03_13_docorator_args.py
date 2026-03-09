# 기존 함수를 수정하지 않고, 그 함수에 앞뒤에 새로운 기능을 추가하고 싶을 때 사용합니다.

# 인자를 받는 함수 예제
def decorator_with_args(func):
    def wrapper(*args, **kwargs):

        print("함수 시작!")
        print(f"인자: args=-{args}, kwargs={kwargs}")

        result = func(*args, **kwargs)
        print(result)

        print ("함수 끝!")

        return result
    return wrapper

@decorator_with_args
def greet(name,**kwargs):
    return f"{name}님, 안녕하세요! (전달된 정보: {kwargs})"

greet("홍길동")

greet("홍길동", ctiy = "서울", bobby= "코딩")