class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __hash__(self):
        return hash((self.title, self.author))

b1 = Book("파이썬 입문", "홍길동")
b2 = Book("파이썬 입문", "홍길동")

print(f"b1 해시: {hash(b1)}")
print(f"b2 해시: {hash(b2)}")
print(f"해시값이 같은가? {hash(b1) == hash(b2)}")