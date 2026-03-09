students = []
NUM_STUDENTS = 5

for i in range(NUM_STUDENTS):
    print(f"\n{i+1}번째 학생 정보 입력]")
    name = input("이름: ")
    kor, eng, math = map(int, input("국어 영어 수학 점수(공백 구분): ").split())

    total = kor + eng + math
    avg = round(total / 3, 2)

    grade = ("A" if avg >= 90 else
            "B" if avg >= 80 else
            "C" if avg >= 70 else
            "D" if avg >= 60 else
            "F")
    
    student = {
        "name": name, "kor": kor, "eng": eng,
        "math": math, "total": total, "avg": avg, "grade": grade
    }
    students.append(student)

kor_sum = sum([student["kor"] for student in students])
eng_sum = sum([student["eng"] for student in students])
math_sum = sum([student["math"] for student in students])
kor_avg = round(kor_sum / NUM_STUDENTS)
eng_avg = round(eng_sum / NUM_STUDENTS)
math_avg = round(math_sum / NUM_STUDENTS)

print("=" * 60)

print("이름\t\t국어\t영어\t수학\t총점\t평균\t학점")

print("-" * 60) 
for student in students:
    print(f"{student["name"]}\t\t{student["kor"]:>3}\t{student["eng"]:>3}\t\
            {student["math"]:>3}\t{student["total"]:>3}\t{student["avg"]:>6.2f}\t\
            {student["grade"]:>3}")
print("-" * 60)

print(f"과목 총점\t{kor_sum:>3}\t{eng_sum:>3}\t{math_sum:>3}")
print(f"과목 평균\t{kor_avg:>3}\t{eng_avg:>3}\t{math_avg:>3}")

print("=" * 60)