# 다음 조건에 맞는 코드를 list의 메서드를 이용해서 작성하세요.

# 1. 리스트 numbers에 [1, 2, 3] 값을 할당 후 4를 추가
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

# 2. 리스트 ["a", "b", "c"]의 마지막 요소를 제거
lst = ["a", "b", "c"]
print("제거된 요소:", lst.pop(), "/ 제거 후 리스트:", lst)

# 3. 리스트 [5, 3, 8, 1]을 오름차순으로 정렬
lst = [5, 3, 8, 1]
lst.sort()
print("정렬된 리스트:", lst)

# 4. 리스트 [1, 2, 2, 3, 2]에서 2의 개수 세기
lst = [1, 2, 2, 3, 2]
print("리스트 원소 2의 개수:", lst.count(2))