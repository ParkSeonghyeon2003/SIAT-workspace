from _02_CardPayment import CardPayment
from _03_BankTransfer import BankTransferPayment
from _04_service_logic import process_payment
from _07_KakaoPay import KakaoPayPayment

def main() -> None:
    process_payment(CardPayment(), 10000)
    process_payment(BankTransferPayment(), 20000)
    process_payment(KakaoPayPayment(), 30000)

if __name__ == "__main__":
    main()