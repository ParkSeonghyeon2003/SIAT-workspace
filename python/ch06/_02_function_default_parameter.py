def greet(name, msg="안녕하세요"):
    return f"{name}님, {msg}"

response = greet("김철수")
print(response)

response = greet("이영희", "뒤져!")
print(response)

# def error_fn(msg="흠...", name):
#     return f"{name}님, {msg}"