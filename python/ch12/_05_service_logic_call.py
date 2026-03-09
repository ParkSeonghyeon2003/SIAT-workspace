from _02_CardPayment import CardPayment
from _03_BankTransfer import BankTransferPayment
from _04_service_logic import process_payment

def main() -> None:
    process_payment(CardPayment(), 10000)
    process_payment(BankTransferPayment(), 20000)

if __name__ == "__main__":
    main()