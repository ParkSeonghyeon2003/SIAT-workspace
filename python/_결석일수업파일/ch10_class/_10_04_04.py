class Parent:
    def method_parent(self):
        print("부모 메서드 호출")

# 자식 클래스 정의
class Child(Parent):
    def __init__(self, name, age):   
        self.name = name
        self.age = age

    def method_cihild(self):
        print("자식 메서드 호출")


# 객체 생성
# Child 인스턴스 생성 시 "철수"는 부모에게, 10은 자식에게 전달됩니다.
c = Child("철수", 10)

c.method_cihild()   # 자식 클래스에 있으므로 정상 호출
c.method_parent()   # 상속받았기 때문에 호출 가능

print(c.name)
print(c.age)

