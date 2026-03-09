def introduce(name, age, city):
    return f"이름: {name}, 나이: {age}, 도시: {city}"

response = introduce("박민수", 25, "서울")
print(response)

response = introduce(age=30, name="최지훈", city="부산")
print(response)

response = introduce("홍길동", city="대전", age=22)
print(response)