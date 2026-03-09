# super()는 MRO 상 다음 클래스의 메서드를 호출한다.

class A:
    def __init__(self):
        print("A init")
        super().__init__()

class B:
    def __init__(self):
        print("B init")
        super().__init__()

class C(A, B):
    def __init__(self):
        print("C init")
        super().__init__()

print(C.mro())
c = C()