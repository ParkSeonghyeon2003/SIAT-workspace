class Parent:
    def __init__(self, name):
        self.name = name

    def method_parent(self):
        print("부모 메서드 호출")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


    def method_child(self):
        print("자식 메서드 호출")

c = Child("철수", 10)
c.method_child()
c.method_parent()

p = Parent("아버지")
p.method_parent()
# p.method_child() : 자식 꺼는 당연히 호출 못함