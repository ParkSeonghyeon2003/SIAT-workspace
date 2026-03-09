def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times2 = make_multiplier(2)
times3 = make_multiplier(3)

print(times2(5))
print(times3(5))