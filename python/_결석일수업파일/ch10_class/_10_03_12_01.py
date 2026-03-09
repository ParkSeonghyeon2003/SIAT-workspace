def my_decorator(func):
    def wrapper():
        print("--- 함수 실행 시작 ---")
        func()  # 실제 함수 호출
        print("--- 함수 실행 종료 ---")

    return wrapper


def hello():
    print("안녕하세요!")


# 지금까지의 함수 호출 방법
hello = my_decorator(hello)

# 함수 호출
hello()