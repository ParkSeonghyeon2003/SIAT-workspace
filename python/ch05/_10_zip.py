names = ["Kim", "Lee"]
ages = [20, 25]

zipped = zip(names, ages)

print(type(zipped))
print(zipped)
print(next(zipped))
print(next(zipped))

zipped = zip(names, ages)
for tup in zipped:
    print("DEBUG:", tup)