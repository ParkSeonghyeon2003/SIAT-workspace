def display(*args, end="\n"):
    print(*args, end=end)

display("안녕하세요")
display("안녕하세요", "파이썬")
display("안녕하세요", "파이썬", "공부 중입니다.")

display("사과", "배", "포도", end=" *** ")
display("과일 목록 끝")

display()