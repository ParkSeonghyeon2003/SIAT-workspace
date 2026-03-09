# _04_00_matrix.py - SIAT 10기 박성현 shpark8267@gmail.com
# 
# import numpy as np
# 행렬 클래스
class Matrix:
    def __init__(self, mats: list):
        self.mats = mats
    
    def __add__(self, other):
        if not isinstance(other, Matrix): # Type Check
            raise TypeError("행렬 끼리만 합을 해주세요.")
        return Matrix([
            [self.mats[i][j] + other.mats[i][j] for j in range(len(self.mats[0]))]
            for i in range(len(self.mats))
            ])
        # return Matrix((np.array(self.mats) + np.array(other.mats)).tolist())

    def __repr__(self):
        return "Matrix(\n  "+"\n  ".join(map(str, self.mats))+"\n)"

# 테스트 코드
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

# 동작 원리: m1 + m2 -> m1.__add__(m2) 호출
result = m1 + m2

print("Matrix 1:", m1)
print("Matrix 2:", m2)
print("결과 (m1 + m2):", result)