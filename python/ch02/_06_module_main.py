# 일부 함수 import - 모듈명 없이 바로 함수 사용 가능
# 모든 함수를 가져오고 싶으면 함수 명들 나열하는 대신 * 를 쓴다.
# 다만 외부 라이브러리에서 가져올 때는 사용을 지양하는 편
from _04_module import add, substract, multiply, divide
x = 20
y = 10

print(add(x, y))
print(substract(x, y))
print(multiply(x, y))
print(divide(x, y))