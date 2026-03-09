matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print(list(zip(matrix))) # 의도대로 Transpose 되지 않는다. zip의 인자로 하나의 리스트만 들어간 꼴이기 때문이다.
print(list(zip(*matrix))) # Unpacking