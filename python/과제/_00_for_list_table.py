students = [
    ["이철수", 90, 80, 100],
    ["김영희", 100, 80, 90],
    ["최길동", 85, 70, 75],
    ["박민수", 95, 85, 80],
    ["정수지", 80, 95, 90]
]
cols = tuple(zip(*students))
kor_sum, eng_sum, math_sum = map(sum, cols[1:])

print("=" * 40)
print("이름", "국어", "영어", "수학", "총점", sep="\t")
print("-" * 40)
for name, kor, eng, math in students:
    score_sum = kor + eng + math
    print(name, kor, eng, math, str(score_sum)+"점", sep="\t")
print("-" * 40)
print("총점", kor_sum, eng_sum, math_sum, sep="\t")
print("=" * 40)