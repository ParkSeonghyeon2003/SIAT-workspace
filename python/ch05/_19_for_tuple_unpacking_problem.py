student = (1, 100, 80, 90)

id, *scores = student

# 총점
score_sum = sum(scores)
# 평균
score_avg = score_sum / len(scores)
# 학점
grade = None
if (score_avg < 60):
    grade = "F"
elif (score_avg < 70):
    grade = "D"
elif (score_avg < 80):
    grade = "C"
elif (score_avg < 90):
    grade = "B"
else:
    grade = "A"
# 학점 추가
student = *student, grade

print("id:", id)
print("scores:", scores)
print("총점:", score_sum)
print("평균:", round(score_avg, 2))
print("등급:", grade)
print("최종 student:", student)