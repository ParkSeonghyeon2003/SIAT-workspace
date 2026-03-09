try:
    num = int(input("정수를 입력하세요."))
except ValueError:
    print("숫자를 입력해야 합니다.")
else:
    print("입력한 숫자는", num)