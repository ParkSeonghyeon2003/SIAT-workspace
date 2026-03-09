f = open("result5.txt", "w", encoding="utf-8")

name = input("이름을 입력하세요>")

print(f"입력한 이름은 {name} 입니다.", file=f, end="")

f.close()