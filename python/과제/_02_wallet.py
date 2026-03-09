"""
과제._02_wallet.py
"""

# 지갑을 생성합니다. owner는 주인의 이름, initial_balance는 초기 잔액입니다.(기본값 0)
def create_wallet(owner, initial_balance=0):
    # 초기 잔액으로 지갑 잔액을 초기화합니다.
    balance = initial_balance

    # amount만큼 출금합니다.
    def spend(amount):
        nonlocal balance # closure
        if amount > balance:
            return f"{owner}님, 잔액이 부족합니다! (잔액: {amount:,}원)"
        balance -= amount
        return f"{amount:,}원 지출. (남은 잔액: {balance:,}원)"
    
    # amount만큼 입금합니다.
    def deposit(amount):
        nonlocal balance # closure
        balance += amount
        return f"{amount:,}원 입금. (현재 잔액: {balance:,}원)"
    
    # 내부 함수를 dict로 묶어 return합니다.
    return {"spend": spend, "deposit": deposit}

# 테스트 코드입니다.
def test_code():
    my_wallet = create_wallet("Alice", 50000)
    print(my_wallet["spend"](20000))
    print(my_wallet["deposit"](10000))

    my_wallet = create_wallet("Dooli", 500)
    print(my_wallet["spend"](20000))
    print(my_wallet["deposit"](100000))

test_code()