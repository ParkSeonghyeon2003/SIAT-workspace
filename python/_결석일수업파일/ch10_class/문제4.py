from datetime import datetime

def logger(func):
    def wrapper(*args, **kwargs):
        a = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"[{a}][호출] 함수명:{func.__name__}")
        print(f"인자: args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"[{a}][완료] 결과값: {result}")
        print("-" * 30)

        return result
    return wrapper

@logger
def add(a,b):
    return a+b

@logger
def greet(name, message="안녕하세요"):
    return f"{name}님, {message}"
    
x = add(10, 20)
y = greet("지민", message="반갑습니다")


