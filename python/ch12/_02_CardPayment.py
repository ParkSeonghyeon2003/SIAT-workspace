from _01_Payment import Payment

class CardPayment(Payment):
    def pay(self, amount: int) -> None:
        print(f"카드로 {amount}원 결제")
    def cancel(self, amount: int) -> None:
        print(f"카드 결제 {amount}원 취소")
