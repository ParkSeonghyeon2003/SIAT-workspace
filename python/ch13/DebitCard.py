""" DebitCard.py """
from Account import Account

class DebitCard(Account):
    def __init__(self, owner: str, balance: int=0) -> None:
        super().__init__(owner, balance)
        self._total_spent = 0
    
    def withdraw(self, amount: int) -> None:
        self._balance -= amount
        self._total_spent += amount

        print(f"[결제 성공] {self.owner}님 {amount}원 결제 완료.")
        print(f"현재 잔액: {self._balance}원")
    
    def deposit(self, amount: int) -> None:
        super().deposit(amount)
    
    def get_card_info(self) -> str:
        return f"--- {self.owner}님의 직불카드 정보 ---\n"+\
                f"현재 잔액: {self._balance}원\n"+\
                f"총 사용 금액: {self._total_spent}원"

if __name__ == "__main__":
    from services import process_deposit, process_withdraw

    print("[2] 출력 결과\n[출력 결과]")
    test_card = DebitCard("지민", 50000) # 50,000원
    process_withdraw(test_card, 20000) # 잔액: 30,000원

    print("\n--- 잔액 초과 결제 시도 ---")
    process_withdraw(test_card, 40000) # 실패: 잔액보다 큰 결제액
    process_deposit(test_card, 10000)  # 잔액: 40,000원

    print("\n--- 입금 후 재결제 ---")
    process_withdraw(test_card, 40000) # 잔액: 0원

    print("\n"+test_card.get_card_info())
    print()