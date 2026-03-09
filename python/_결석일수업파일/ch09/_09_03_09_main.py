from my_module2 import add # import 시점에 "my_module2.py"의 __name__ 는 "my_module2" 로 변경됩니다.

print(add(100, 200))    # 300