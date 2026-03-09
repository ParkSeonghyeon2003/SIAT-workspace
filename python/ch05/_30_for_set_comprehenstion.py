names = ["apple", "banana", "cherry", "apple", "cherry", "DRAGONFRUIT"]

# 모든 이름을 소문자로 바꾸면서 중복 제거
unique_fruits = {f.lower() for f in names}
print(unique_fruits)

# Set Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6]

# 5보다 큰 짝수만 골라내어 중복 없이 저장
even_set = {n for n in numbers if n > 5 and n % 2 == 0}
print(even_set)

# 문자열에서 사용된 알파벳 추출
word = "abracadabra"
unique_chars = {char for char in word if char != "a"}
print(unique_chars)

numbers = {1, 2, 3, 4, 5, 6}
new_numbers = {
    num if num % 2 != 0 else num * 10
    for num in numbers}
print(new_numbers)