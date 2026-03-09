""" services.py """
from Account import Account

def process_deposit(account: Account, amount: int) -> None:
    if amount <= 0:
        raise ValueError("입금액은 0원보다 커야합니다.")
    account.deposit(amount)

def process_withdraw(account: Account, amount: int) -> None:
    balance = account.get_balance()
    if balance < amount:
        print("잔액이 부족합니다.")
        print(f"현재 잔액: {balance}원 / 부족 금액: {amount - balance}원")
        return
    account.withdraw(amount)