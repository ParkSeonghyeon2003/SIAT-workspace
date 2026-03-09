import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])

# flatten()의 역할: 2차원 이상의 고차원 배열을 무조건 1차원으로 쭉 펼쳐줍니다.
flat = arr.flatten()

print(flat)     # [1 2 3 4 5 6]


# 딥러닝에서 이미지(2D) 데이터를 특징 추출(Covbolution)한 뒤,
# 마지막에 분류(Classification)를 하기 위해 숫자를 한 줄로 쭉 늘어뜨려야 할 때 이 flatten 과정을 거치게 됩니다.
