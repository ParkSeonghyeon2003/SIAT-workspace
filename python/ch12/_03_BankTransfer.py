from _01_Payment import Payment

class BankTransferPayment(Payment):
    def pay(self, amount: int) -> None:
        print(f"계좌이체로 {amount}원 결제")
    def cancel(self, amount: int) -> None:
        print(f"계좌이체 결제 {amount}원 취소")
