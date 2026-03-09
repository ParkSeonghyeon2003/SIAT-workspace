# len, str같은 내장 함수는 객체에 해당하는 메서드가 구현되어 있어야 동작함.

class A:
    """
    def __len__(self):
        return 20030325
    """

a = A()

print(len(a))