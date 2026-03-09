# pip install numpy

# NumPy는 대규모 다차원 배열과 행렬 연산을 빠르게 처리하기 위한 파이썬 라이브러리입니다.
import numpy as np

# numpy의 array는 동일한 타입으로만 이루어 집니다.

# 파이썬의 기본 리스트([ ])를 NumPy의 배열 객체(ndarray)로 변환하여 변수 arr에 저장합니다.
arr = np.array([1, 2, 3, 4, 5])

# 생성된 배열의 내용을 출력합니다.
# 파이썬 리스트와 달리 요소 사이에 쉼표(,)가 없이 공백으로 구분되어 출력되는 것이 특징입니다.
print(arr)          # [1 2 3 4 5]


# arr 변수의 자료형(Type)을 확인합니다.
# numpy.ndarray라고 출력되는데, 이는 N-Dimensional Array(n차원 배열)의 약자입니다.
print(type(arr))    # <class 'numpy.ndarray'>

# arr.shape (배열의 형태): 배열이 몇 행, 몇 열로 구성되어 있는지 튜플 형태로 보여줍니다.
# 위 코드에서는 (5,)가 출력되며, 이는 요소가 5개인 1차원 배열이라는 뜻입니다.
print(arr.shape, arr.ndim)  # (5,) 1

# 대괄호 ([])의 중첩 개수가 차원의 깊이를 나타냅니다.
# 2차원 배열
matrix = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)
print(matrix)
# [[1 2 3]]
#  [[4 5 6]]

# matrix.shape(2, 3): 배열 형태를 나타냅니다
# 앞의 숫자 2는 행(Row)의 개수, 뒤의 숫자 3은 열(Column)의 개수를 의미합니다.
# matrix.ndim(2): 이 배열이 2차원임을 나타냅니다.
print(matrix.shape, matrix.ndim)    #(2, 3) 2