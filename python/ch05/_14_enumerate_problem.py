names = ["Kim", "Lee"]
ages = [20, 25]

for index, (name, age) in enumerate(zip(names, ages)):
    print(f"{index}번 이름: {name} 나이: {age}")
print()