text = "  Hello Python World  "
print("원본:", text)

result = len(text)
print("문자열 길이:", result)

result = text.count("a")
print(result)
result = text.count("l")
print(result)

result = text.find("h")
print(result)
result = text.find("ha")
print(result)

sample = "python"
print("startswith:", sample.startswith("py"))
print("endswith:", sample.endswith("on"))