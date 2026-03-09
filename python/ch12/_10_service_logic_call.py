from _02_CardPayment import CardPayment
from _03_BankTransfer import BankTransferPayment
from _07_KakaoPay import KakaoPayPayment
from _09_service_logic_cancel import process_payment

def main() -> None:
    process_payment(CardPayment(), 10000) # 기존 방식대로 호출해도 가능 (디폴트 파라미터)
    process_payment(BankTransferPayment(), 20000, True) # 세 번째 인자로 취소 요청인건지 확인
    process_payment(KakaoPayPayment(), 30000, False) # 물론 명시적으로 False를 줘도 됨

if __name__ == "__main__":
    main()