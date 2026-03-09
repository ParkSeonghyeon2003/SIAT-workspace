""" PointCard.py """
from Account import Account

class PointCard(Account):
    def __init__(self, owner: str, balance: int=0):
        super().__init__(owner, balance)
        self.point: int = 0
    
    def deposit(self, amount: int) -> None:
        super().deposit(amount)
        plus_point:int = int(amount * 0.001)
        self.point += plus_point
        print(f"[포인트 적립] {plus_point}P가 쌓였습니다. (총 포인트: {self.point}P)")

    def withdraw(self, amount: int) -> None:
        self._balance -= amount
        print(f"[출금] {amount}원 처리 완료. (잔액: {self._balance}원)")
    
    def get_info(self) -> str:
        return f"{self.owner}님의 카드 상태 - 잔액: {self._balance}원, 포인트: {self.point}P"

if __name__ == "__main__":
    from services import process_deposit, process_withdraw
    
    print("[3]출력결과")
    test_card = PointCard("지민", 10000)
    process_deposit(test_card, 10000)
    process_withdraw(test_card, 5000)
    print(test_card.get_info())