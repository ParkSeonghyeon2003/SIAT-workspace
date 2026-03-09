f = open("result3.txt", "w", encoding="utf-8")

print("안녕하세요", file=f)

print("파이썬 print file 옵션", file=f, end="")

f.close()