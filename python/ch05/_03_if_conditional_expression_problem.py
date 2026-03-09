# 1. 정수 num이 양수면 "양수", 아니면 "음수 또는 0"
num = -3
result = "양수" if num > 0 else "음수 또는 0"
print(result)

# 2. 점수 score가 60점 이상이면 "합격", 아니면 "불합격"
score = 58
status = "합격" if score >= 60 else "불합격"
print(status)

# 3. 문자열 ch가 빈 문자열이면 "비어 있음", 아니면 "값 있음"
ch = ""
result = "비어 있음" if ch == "" else "값 있음"
print(result)

# 4. 정수 age가 20 이상이면 "성인", "아니면 "미성년자"
age = 17
result = "성인" if age >= 20 else "미성년자"
print(result)

# 5. 정수 num이 10의 배수이면 "10의 배수", 아니면 "아님"
num = 40
result = "10의 배수" if num % 10 == 0 else "아님"
print(result)

# 6. 두 정수 a, b 중 더 큰 값을 max_value에 저장(같으면 b 저장)
a = 7
b = 9
max_value = a if a > b else b
print(max_value)

# 7. 두 정수 a, b 중 더 작은 값을 min_value에 저장(같으면 b 저장)
a = 7
b = 9
min_value = a if a < b else b
print(min_value)

# 8. 정수 num이 0이면 "zero", 아니면 "non-zero"
num = 0
result = "zero" if num == 0 else "non-zero"
print(result)

# 9. 문자열 word의 길이가 5 이상이면 "긴 문자열", 아니면 "짧은 문자열"
word = "python"
result = "긴 문자열" if len(word) >= 5 else "짧은 문자열"
print(result)

# 10. 회문 판단 문장 - 회문이면 "회문입니다", 아니면 "회문이 아닙니다"
word = "level"
result = "회문입니다" if word == word[::-1] else "회문이 아닙니다"
print(result)