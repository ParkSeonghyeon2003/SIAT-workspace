# pip install numpy

# NumPy는 대규모 다차원 배열과 행렬 연산을 빠르게 처리하기 위한 파이썬 라이브러리입니다.
import numpy as np

# 모든 요소가 0으로 채워진 2행 3열의 2차원 배열을 생성합니다.
# zeros() 안에 (2, 3)처럼 괄호를 하나 더 써서 튜플(Tuple) 형태로 크기를 전달해야 합니다.
z = np.zeros((2,3)) # dtype=float이 기본
print(z)
# 머신러닝, 딥러닝 등에서 가중치 초기화에 사용됩니다.

# 모든 요소가 1로 채워진 길이 5의 1차원 배열을 생성합니다.
o = np.ones((2,3))      # dtype=float이 기본
print(o)            # [1. 1. 1. 1. 1.]

# 2행 3열 모두 5로 채워집니다.
f = np.full((2,3), 5)   # dtyp을 설정하지 않으면 두 번째 매개변수 값으로 채웁니다.
print(f)

f_float = np.full((2,3), 5, dtype=float)
print(f_float)

# 연속된 정수 생성 : arange(start, end-1)
print(np.arange(1,10))  # [1 2 3 4 5 6 7 8 9]

# arange(start, end-1, step)
print(np.arange(1,10,2))    # [1 3 5 7 9]

# 실수 단위 간격 가능
# 0부터 1 미만까지 0.2씩 증가
print(np.arange(0, 1, 0.2)) # [0.   0.2 0.4 0.6 0.8]

