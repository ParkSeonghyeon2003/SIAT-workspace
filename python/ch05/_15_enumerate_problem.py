names = ["홍길동", "이순신"]
scores = [100, 90]
grades = ["Best", "Good"]

for name, score, grade in zip(names, scores, grades):
    print(f"{name}: {score}({grade})")
print()