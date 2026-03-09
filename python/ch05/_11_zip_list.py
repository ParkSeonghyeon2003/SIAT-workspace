names = ["Kim", "Lee"]
ages = [20, 25]

zipped = zip(names, ages)

result = list(zipped) # zipped는 순회가 끝남 (StopIteration)

print(result[0])
print(type(result[0]))

empty = list(zipped) # 더 이상 순회할 수 없어서 empty.
print(f"값이 비었나요? => {empty}")