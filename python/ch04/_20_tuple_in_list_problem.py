# 리스트 안에 튜플
students = [("Kim", 90, 80, 90), ("Lee", 85, 75, 75), ("Park", 95, 90, 90)]

# Calculated
sum_0 = sum(students[0][1:])
sum_1 = sum(students[1][1:])
sum_2 = sum(students[2][1:])
kor_sum = sum([students[0][1], students[1][1], students[2][1]])
eng_sum = sum([students[0][2], students[1][2], students[2][2]])
mat_sum = sum([students[0][3], students[1][3], students[2][3]])

# Header
print("이름", "국어", "영어", "수학", "총점", sep="\t")
print("-" * 40)

# Body
print(students[0][0], students[0][1], students[0][2], students[0][3], str(sum_0)+"점", sep="\t")
print(students[1][0], students[1][1], students[1][2], students[1][3], str(sum_1)+"점", sep="\t")
print(students[2][0], students[2][1], students[2][2], students[2][3], str(sum_2)+"점", sep="\t")
print("-" * 40)

# Footer
print("총점", kor_sum, eng_sum, mat_sum, sep="\t")