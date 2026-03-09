f = open("example.txt", "r", encoding="utf-8")
for line in f:
    print(line.strip())
f.close