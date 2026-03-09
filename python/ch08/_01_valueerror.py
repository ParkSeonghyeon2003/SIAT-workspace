try:
    num = int(input("정수를 입력하세요."))
    print("입력한 숫자는", num)
except ValueError:
    print("숫자를 입력해야 합니다.")