students = (1, 100, 80, 90, "A")

id, *scores, grade = students

score_sum = sum(scores)
score_avg = score_sum / len(scores)

print("id:", id)
print("scores:", scores)
print("총점:", score_sum)
print("평균:", score_avg)
print("등급:", grade)