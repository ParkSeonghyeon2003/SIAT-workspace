# 리스트 특정 구간을 0으로 초기화
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers[2:-2] = [0, 0, 0]
print(numbers) # [1, 2, 0, 0, 0, 6, 7]

# 리스트 맨 앞에 요소들 추가
numbers = [4, 5, 6]
numbers[0:0] = [1, 2, 3]
print(numbers) # [1, 2, 3, 4, 5, 6]

# 리스트 맨 뒤에 요소들 추가
numbers = [1, 2, 3]
numbers[3:3] = [4, 5, 6]
print(numbers) # [1, 2, 3, 4, 5, 6]

# 짝수 인덱스 요소들만 교체
numbers = [0, 0, 0, 0, 0]
numbers[::2] = [1, 1, 1]
print(numbers) # [1, 0, 1, 0, 1]

# 리스트 전체 내용물 비우기
numbers = [1, 2, 3, 4, 5]
numbers[:] = []
print(numbers) # []

# 리스트 중간에 삽입
numbers = [1, 2, 5, 6]
numbers[2:2] = [3, 4]
print(numbers) # [1, 2, 3, 4, 5, 6]