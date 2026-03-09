num = 3

if num % 2 == 0:
    result = "even"
else:
    result = "odd"
print(result)

result = "even" if num % 2 == 0 else "odd"
print(result)

result = ["even" if i % 2 == 0 else "odd" for i in range(5)]
print(result)