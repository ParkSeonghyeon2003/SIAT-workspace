name = "Alice"
age = 25
height = 165.5
is_student = True

age_float = float(age)
print(age_float)

pi = float("3.141592")
print(pi)

pi = float(is_student)
print(pi)

age_str = str(age)
print("형 변환 결과:", age_str, "는 ", type(age), "=>", type(age_str))

print(str(is_student))

height_int = int(height)
print("형 변환 결과:", height, "는 ", height_int, "로 변경", type(height), "=>", type(height_int))

p = int("3")
print(p)

is_student_int = int(is_student)
print(is_student_int)

print(bool(0))
print(bool(""))
print(bool(None))