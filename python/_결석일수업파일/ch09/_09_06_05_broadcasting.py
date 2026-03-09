# pip install numpy

# NumPy는 대규모 다차원 배열과 행렬 연산을 빠르게 처리하기 위한 파이썬 라이브러리입니다.
import numpy as np

# [1, 2, 3] => [11, 12, 13]
# 파이썬 기본 리스트
# 컴프리헨션으로
original = [1, 2, 3]
result = [i + 10 for i in original]
print(result)

# NumPy 배열이 데이터를 처리하는 방식
# 배열 전체에 10이라는 값을 한 번에 더합니다.
# 이를 브로드캐스팅(Broadcastion)이라고 부릅니다.
# 보통 연산을 하려면 배열들의 크기가 정확히 같아야 하지만,
# 넘파이는 특정 조건이 만족되면 작은 배열을 큰 배열의 크기에 맞춰 "확장"하여 연산을 수행합니다.
# 브로드 캐스팅 조건)
# 1. 두 배열의 해당 차원 크기가 동일할 때
# 2. 둘 중 하나의 차원 크기가 1일 때
np_result = np.array(original) + 10
print(np_result)


# https://numpy.org/doc/stable/user/basics.broadcasting.html
a = np.array([1.0, 2.0, 3.0])
b = 2.0
print(a*b)  # [2. 4. 6.]