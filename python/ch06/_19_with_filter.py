def is_even(n):
    return n % 2 == 0

nums = [1, 2, 3, 4, 5, 6]
evens = filter(is_even, nums)
print(evens)
print(list(evens))

evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)

nums = [10, 15, 20, 25, 30]
filtered = list(filter(lambda x: 10 <= x <= 25, nums))
print(filtered)