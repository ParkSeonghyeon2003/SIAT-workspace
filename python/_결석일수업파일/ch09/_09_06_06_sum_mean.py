# pip install numpy

# NumPy는 대규모 다차원 배열과 행렬 연산을 빠르게 처리하기 위한 파이썬 라이브러리입니다.
import numpy as np

# 배열의 합계와 평균
arr = np.array([10, 20, 30])
print(np.sum(arr), np.mean(arr))   # 60 20.0(평균)

# 정렬
arr = np.array([3, 1, 2])
print(np.sort(arr))     # [1 2 3]

# 최대값 위치
arr = np.array([10, 50, 30])
print(np.argmax(arr))   # 1 index[1] < 50