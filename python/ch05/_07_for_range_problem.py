for i in range(5, 51, 5):
    print(i, end=" ")
print()
print("=" * 140)

for dan in range(2, 10):
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}", end="\t")
    print()
print()