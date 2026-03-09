from MyError import MyError

def check_number(n):
    if n < 0:
        raise MyError("음수는 허용되지 않습니다.")
    return n * 2

result = check_number(-5)