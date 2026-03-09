def add(a, b):
    return a + b

def substract(a, b):
    return a - b

print("my_module2의 __name__ 값은", __name__, "입니다.")

if __name__ == "__main__":
    print("이 코드는 my_module2.py를 직접 실행했을 때만 보입니다!")
    print(add(10, 20))
