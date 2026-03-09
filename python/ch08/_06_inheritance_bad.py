try:
    result = 10 / 0
except Exception:
    print("오류가 발생했습니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")