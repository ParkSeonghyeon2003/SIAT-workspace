from _01_Payment import Payment

def process_payment(payment: Payment, amount: int, isCancel: bool=False) -> None:
    # Validation
    if amount <= 0:
        raise ValueError("금액 오류")
    
    if not isCancel: # 결제 요청
        payment.pay(amount)
    else: # 취소 요청
        payment.cancel(amount)