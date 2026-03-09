students = {'name': 'Alice', "age": 26}

key1, key2 = students
print(key1, key2)
print()

value1, value2 = students.values()
print(value1, value2)
print()

for key, value in students.items():
    print(key, value)
print()