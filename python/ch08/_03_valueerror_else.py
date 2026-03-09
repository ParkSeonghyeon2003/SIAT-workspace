try:
    num = int(input("정수를 입력하세요."))
except ValueError:
    print("숫자를 입력해야 합니다.")
else:
    print("else문 입력한 숫자는", num)
finally:
    print("예외 상관없이 실행되는 곳입니다.")