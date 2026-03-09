text = "  Hello Python World  "
print("원본:", text)
print("원본 길이:", len(text))

##### 문자열 공백 제거 #####
result = text.strip()
print("strip:", result)
print("공백 제거 후 문자열 길이:", len(result))
print("원본 길이:", len(text))

result = text.lstrip()
print("공백 제거 후 문자열 길이:", len(result))

result = text.rstrip()
print("공백 제거 후 문자열 길이:", len(result))

##### 문자열 분리 #####
words = text.split()
print("split:", words)

data = "python,java,c++,html"
result = data.split(",")
print(result)

#### 문자열 결합 #####
print("join:", "-".join(words))