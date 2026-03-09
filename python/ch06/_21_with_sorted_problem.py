students = [
    ("Kim", 82),
    ("Lee", 91),
    ("Park", 82),
    ("Choi", 91),
    ("Han", 78)
]

# 점수 오름차순 -> 이름 오름차순
sorted_students = sorted(students, key=lambda student: (student[1], student[0]))

print(sorted_students)