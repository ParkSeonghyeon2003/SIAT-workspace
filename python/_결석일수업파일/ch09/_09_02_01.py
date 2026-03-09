# 모듈(Module)은 파이썬 코드가 들어 있는 하나의 파일(.py)입니다.
# 함수, 클래스, 변수 등을 한 파일에 모아두고, 다른 파일에서 import로 불러 사용합니다.

# import 모듈
import my_module

response = my_module.add(3,5)   
print(response) # 8

response = my_module.subtract(5,3)
print(response) # 2