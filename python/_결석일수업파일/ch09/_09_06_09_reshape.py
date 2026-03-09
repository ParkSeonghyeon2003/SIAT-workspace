# pip install numpy

# NumPy는 대규모 다차원 배열과 행렬 연산을 빠르게 처리하기 위한 파이썬 라이브러리입니다.
import numpy as np

# reshape 함수는 Numpy에서 가장 자주 사용되는 기능 중 하나로,
# 데이터의 내용은 그대로 유지한 채 배열의 차원과 모양(Shape)만 바꿉니다.
arr = np.arange(6)
print(arr)  # [0 1 2 3 4 5]

# 1차원 배열 => 6개의 요소를 2행 3열의 2차원으로 변경합니다.
# 조건) 원래 배열의 크기가 6이라면 변환할 배열도 전체 요소의 갯수가 6이어야 합니다.
print(arr.reshape(2,3)) # 변경 가능 2행 3열

print(arr.reshape(3,2)) # 변경 가능 3행 2열


# -1 사용
arr = np.arange(12)

# "열은 4개로 고정하고, 행의 개수는 네가 알아서 계산해줘"
new_arr = arr.reshape(-1, 4)
print(new_arr)  # 3행 4열
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]