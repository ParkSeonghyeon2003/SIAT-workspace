from _01_Payment import Payment

def process_payment(payment: Payment, amount: int) -> None:
    if amount <= 0:
        raise ValueError("결제 금액 오류")
    payment.pay(amount)