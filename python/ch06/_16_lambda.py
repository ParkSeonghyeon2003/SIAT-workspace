add_lambda = lambda x, y: x + y
print(add_lambda(y=10, x=5))

add_all = lambda *args: sum(args)

print(add_all(1, 2, 3, 4, 5))
print(add_all(1, 2, 3))

complex_lambda = lambda a, b=10, *args: a + b + sum(args)
print(complex_lambda(1, 2, 3, 4))

get_sum = lambda **kwargs: sum(kwargs.values())
print(get_sum(a=10, b=20, c=30))
