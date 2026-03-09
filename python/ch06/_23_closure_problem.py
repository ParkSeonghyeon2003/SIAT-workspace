def counter():
    count = 0
    def _counter():
        nonlocal count
        count += 1
        return count
    return _counter

c = counter()
print(c()) # 1
print(c()) # 2