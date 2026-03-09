def add(x, y):
    return x + y

response = add(3, 5)
print(response)

add_lambda = lambda x, y: x + y
response = add_lambda(3, 5)
print(response)

def max(a, b):
    return a if a > b else b
print(max(10, 7))

max_lambda = lambda a, b: a if a > b else b
print(max_lambda(10, 7))