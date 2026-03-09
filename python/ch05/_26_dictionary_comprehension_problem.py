users_json = [
    {"id": 1, "name": "Alice", "age": 25, "active": True},
    {"id": 2, "name": "Bob", "age": 17, "active": False},
    {"id": 3, "name": "Charlie", "age": 30, "active": True}
]

result = {user.get("name"): ("active" if user.get("active") else "inactive") for user in users_json}
print(result)

result2 = {
    user["name"]: user["age"] for user in users_json
    if user["age"] >= 20
}
print(result2)