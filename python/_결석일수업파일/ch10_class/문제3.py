class Book:
    library = "시립 도서관"
    
    def __init__ (self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"책 제목: {self.title}, 저자: {self.author}")

    @classmethod
    def library_info(cls):
        print(f"이 책은 {Book.library}에 있습니다")
                        # cls.library
    @staticmethod
    def greeting():
        print("도서관에 오신 것을 환영합니다!")

t1 = Book("파이썬 프로그래밍", "홍길동")
t1.info()
Book.library_info()
Book.greeting()