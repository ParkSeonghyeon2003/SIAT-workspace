students = {"Alice": 90, "Bob": 85}
new_students = {}
for name, score in students.items():
    new_students[name] = score + 5
print(new_students)

c_new_students = {name: score + 5 for name, score in students.items()}
print(c_new_students)

passed = {}
for name, score in students.items():
    if score >= 90:
        passed[name] = score
print(passed)

c_passed = {name: score for name, score in students.items() if score >= 90}
print(c_passed)

numbers = {"a": 1, "b": 2, "c": 3, "d": 4}
even_odd_dict = {}
for key, value in numbers.items():
    if value % 2 == 0:
        even_odd_dict[key] = "even"
    else:
        even_odd_dict[key] = "odd"
print(even_odd_dict)

c_even_odd_dict = {key: "even" if value % 2 == 0 else "odd" for key, value in numbers.items()}
print(c_even_odd_dict)