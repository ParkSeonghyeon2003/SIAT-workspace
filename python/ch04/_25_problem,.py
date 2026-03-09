"""
numbers = [1, 2, 2, 5, 3, 4, 4, 0]

중복을 제거한 후
정렬된 리스트로 만들어 주세요
"""

numbers = [1, 2, 2, 5, 3, 4, 4, 0]

numbers = sorted(list(set(numbers)))
print(numbers)

##### sorted() #####
# 정렬된 List를 반환한다.
# 인자로는 리스트 말고도 튜플, 집합, 문자열 등이 들어갈 수 있다.

# 딕셔너리 자체를 인자로 하면 키를 기준으로 정렬되며, 키 리스트만 return 된다.
print(sorted({"b": 2, "a": 1, "c": 3})) # ["a", "b", "c"]
# items() 메서드는 튜플 원소의 리스트 형태로 return된다.
d = {"b": 2, "a": 1, "c": 3}
print(sorted(d.items())) # [("a": 1), ("b": 2), ("c": 3)]
print(sorted(d.values())) # [1, 2, 3]