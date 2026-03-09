# 1. 기본 오름차순 정렬
nums = [4, 1, 3, 2]
nums.sort()
print(nums) # [1, 2, 3, 4]

# 2. 내림차순 정렬
nums = [4, 1, 3, 2]
nums.sort(reverse=True)
print(nums) # [4, 3, 2, 1]

# 3. 문자열 정렬 (사전 순)
words = ["banana", "apple", "cherry"]
words.sort()
print(words) # ["apple", "banana", "cherry"]

# 4. 문자열 길이 기준 정렬 (key=len)
words = ["apple", "kiwi", "banana", "fig"]
words.sort(key=len)
print(words) # ["fig", "kiwi", "apple", "banana"]

# 5. 문자열 길이 기준 내림차순
words = ["apple", "kiwi", "banana", "fig"]
words.sort(key=len, reverse=True)
print(words) # ["banana", "apple", "kiwi", "fig"]

# 6. 문자열 정렬
names = ["apple", "Banana", "cherry", "Apple"]
names.sort()
print(names) # ["Apple", "Banana", "apple", "cherry"]

# 7. 대소문자 무시하고 문자열 정렬
names = ["apple", "Banana", "cherry", "Apple"]
names.sort(key=str.lower)
print(names) # ["apple", "Apple", "Banana", "cherry"]
# 파이썬의 sort는 안정 정렬(Stable Sort)을 하는거 같음.