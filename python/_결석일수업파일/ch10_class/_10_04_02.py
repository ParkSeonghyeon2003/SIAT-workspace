# 자식 클래스에 생성자가 없는 경우
# 자식 클래스에 __init__이 없으면, 부모 클래스의 __init__이 자동으로 호출됩니다.

# 자식 클래스는 부모 클래스의 메서드를 사용할 수 있습니다.

# 부모 클래스 정의
class Parent:
    def __init__(self, name):
        self.name = name

    def method_parent(self):
        print("부모 메서드 호출")

# 자식 클래스 정의
class Child(Parent):    # Parent 상속
                    # 생성자가 없어 부모의 __init__(self, name)를 호출
    def method_cihild(self):
        print("자식 메서드 호출")

# 객체 생성
c = Child("철수")
c.method_cihild()   # 자식 클래스에 있으므로 정상 호출
c.method_parent()   # 상속받았기 때문에 호출 가능

p = Parent("아버지")
p.method_parent()   # 부모 클래스에 존저해는 메서드 호출 가능
# p.method_child()      # 부모 클래스는 자식 클래스의 메서드를 사용할 수 없습니다.