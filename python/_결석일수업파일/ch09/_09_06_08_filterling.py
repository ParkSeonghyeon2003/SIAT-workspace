# pip install numpy

# NumPy는 대규모 다차원 배열과 행렬 연산을 빠르게 처리하기 위한 파이썬 라이브러리입니다.
import numpy as np

# 불리언 결과 배열 (Boolean Mask)
arr=    np.array([1, 2, 3, 4])
print(arr > 2)  # [False False  True  True]

# 필터링 (Boolean Indexing)
# arr >= 30이라는 조건이 먼저 실행되어 [False, False, True, True]라는 불리언 배열을 만들고,
# 이 중 True인 위치의 값만 추출합니다.
arr = np.array([10, 20, 30, 40])
result = arr[arr >= 30]
print(arr>=30)
print(result)   # [30 40]

# 슬라이싱 (Slicing)
arr = np.array([1, 2, 3, 4, 5])
print(arr[1:4]) # [2 3 4] 인덱스 1, 2, 3 까지만 가져오라는 의미 [strat:end-1]

# 1차원 인덱싱
arr = np.array([10, 20, 30])
print(arr[1])   # 인덱스의 1요소인 20을 가져옵니다.

# 2차원 인덱싱
arr = np.array([[1, 2], [3, 4]])
print(arr[0,1]) # 0행1열의 데이터를 가져옵니다 => 2