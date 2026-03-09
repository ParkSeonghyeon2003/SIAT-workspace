NUM_STUDENTS = 5
students = []
kor_sum, eng_sum, math_sum = 0, 0, 0
for i in range(1, NUM_STUDENTS + 1):
    print(f"{i}번째 학생 정보 입력")
    name = input("이름: ")
    kor, eng, math = map(int, input("국어 영어 수학 점수(공백 구분): ").split())
    total = kor + eng + math
    kor_sum += kor
    eng_sum += eng
    math_sum += math
    avg = total / 3
    grade = ""
    if avg < 60:
        grade = "F"
    elif avg < 70:
        grade = "D"
    elif avg < 80:
        grade = "C"
    elif avg < 90:
        grade = "B"
    else:
        grade = "A"
    students.append({
        "name": name, "kor": kor, "eng": eng, "math": math,
        "total": total, "avg": avg, "grade": grade
    })
kor_avg = round(kor_sum / NUM_STUDENTS)
eng_avg = round(eng_sum / NUM_STUDENTS)
math_avg =round(math_sum / NUM_STUDENTS)

def printTable():
    print("=" * 60)
    print("이름\t\t국어\t영어\t수학\t총점\t평균\t학점")
    print("-" * 60)
    for student in students:
        name, kor, eng, math, total, avg, grade = student.values()
        print(f"{name}\t\t{kor:>3}\t{eng:>3}\t{math:>3}\t{total:>3}\t{avg:>6.2f}\t{grade:>3}")
    print("-" * 60)
    print(f"과목 총점\t{kor_sum:>3}\t{eng_sum:>3}\t{math_sum:>3}")
    print(f"과목 평균\t{kor_avg:>3}\t{eng_avg:>3}\t{math_avg:>3}")
    print("=" * 60)

printTable()