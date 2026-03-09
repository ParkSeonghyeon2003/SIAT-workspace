class Car:
    car_wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def info(self):
        print(f"이 차는 {self.brand}브랜드의 {self.color}색 자동차 입니다.\n바퀴는 {Car.car_wheels}개가 달려있습니다.")

    def drive(self):
        print(f"{self.brand} 자동차가 주행을 시작합니다!")

c1 = Car("현대","red")
c2 = Car("기아","blue")

c1.info()
c1.drive()
print("-"* 30)
c2.info()
c2.drive()