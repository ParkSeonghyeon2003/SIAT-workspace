a = 10
b = 0

try:
    print(a / b)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

print("프로그램 정상 종료")