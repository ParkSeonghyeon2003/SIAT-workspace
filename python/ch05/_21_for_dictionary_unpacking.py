# *은 key만 unpacking하고, **를 쓰면 키값 쌍이 같이 unpacking 된다.

students = {"name": "Alice", "age": 26}
print(*students)
print()

info = {"name": "Kim"}
scores = {"kor": 90, "eng": 85}
full_data = {**info, **scores}
print(full_data) # {"name": "Kim", "kor": 90, "eng": 85}
print()

full_data = info | scores
print(full_data) # {"name": "Kim", "kor": 90, "eng": 85}
print()

def show_info(name, age):
    print(f"{name} is {age} years old.")

show_info(*students)
print()
show_info(**students)
print