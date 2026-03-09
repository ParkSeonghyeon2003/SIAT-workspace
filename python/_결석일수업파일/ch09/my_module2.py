# my_module2.py
def add(a,b):
    return a + b

def subtract(a, b):
    return a - b


# 이 파일을 바로 실행하면 "my_module2의 __name__값은 __main__입니다." 출력됩니다.
# 이 파일이 다른 곳에서 import 되면 "my_module2의 __name__값은 my_module2 입니다."로 출력됩니다.
# 즉 프로그램 시작이 이곳(만든 곳)인 경우에만 __name__ == "__main__" 됩니다.

print("my_module2의__name__값은",__name__, "입니다.")   # 이 파일이 다른 파일에서 import 되면 my_module2 로 바뀝니다.

# 테스트를 위해 넣어둔 코드
if __name__ == "__main__":
    print("이 코드는 my_module2.py를 직접 실행했을 때만 보입니다!")
    print(add(10,20))