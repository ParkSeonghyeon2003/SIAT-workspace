text = "  Hello Python World  "
print("원본:", text)

##### 문자열 변환 #####

# 대문자 변환
result = text.upper()
print("upper:", result)
print("원본:", text)

# 소문자 변환
result = text.lower()
print("lower:", result)
print("원본:", text)



text = "banana"
print(text.replace("a", "o"))
print(text.replace("a", "o", 1)) # 세 번째 매개변수는 갯수