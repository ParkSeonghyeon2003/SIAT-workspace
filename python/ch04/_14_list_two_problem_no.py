# 1. 5행 4열 데이터 생성
students = [
    ["이철수", 90, 80, 100],
    ["김영희", 100, 80, 90],
    ["최길동", 85, 70, 75],
    ["박민수", 95, 85, 80],
    ["정수지", 80, 95, 90]
]

# Header
print("이름\t국어\t영어\t수학\t총점")
print("-" * 40)

# Body
print(f"{students[0][0]}\t{students[0][1]}\t{students[0][2]}\t{students[0][3]}\t{sum(students[0][1:])}점")
print(f"{students[1][0]}\t{students[1][1]}\t{students[1][2]}\t{students[1][3]}\t{sum(students[1][1:])}점")
print(f"{students[2][0]}\t{students[2][1]}\t{students[2][2]}\t{students[2][3]}\t{sum(students[2][1:])}점")
print(f"{students[3][0]}\t{students[3][1]}\t{students[3][2]}\t{students[3][3]}\t{sum(students[3][1:])}점")
print(f"{students[4][0]}\t{students[4][1]}\t{students[4][2]}\t{students[3][3]}\t{sum(students[4][1:])}점")
print("-" * 40)

# Footer
korean_sum = sum([students[0][1], students[1][1], students[2][1], students[3][1], students[4][1]])
english_sum = sum([students[0][2], students[1][2], students[2][2], students[3][2], students[4][2]])
math_sum = sum([students[0][3], students[1][3], students[2][3], students[3][3], students[4][3]])
print(f"총점\t{korean_sum}\t{english_sum}\t{math_sum}")