from typing import List, Generator

class Account:
    def __init__(self, owner: str, balance: int=0) -> None:
        self.owner = owner
        self.__balance = balance
        self.__transactions: List[str] = []
    
    def deposit(self, amount: int) -> None:
        if (amount >= 0):
            self.__balance += amount
            self.__transactions.append(f"입금: +{amount}원")
            print(f"{amount}원이 입금되었습니다.")
        else:
            print("입금액은 0보다 커야 합니다.")
    
    def withdraw(self, amount: int) -> None:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"출금: -{amount}원")
            print(f"{amount}원이 출금되었습니다.")
        else:
            print("잔액이 부족하거나 잘못된 금액입니다.")
    
    @property
    def balance(self) -> int:
        return self.__balance
    
    def __str__(self) -> str:
        return f"{self.owner}님의 계좌 (현재 잔액: {self.__balance}원)"
    
    def __len__(self) -> int:
        return len(self.__transactions)

    def __iter__(self) -> Generator[str, None, None]:
        print("--- 거래 내역 목록 ---")
        for ts in self.__transactions:
            yield ts

my_acc = Account("김철수", 1000)
my_acc.deposit(5000)
my_acc.withdraw(2000)
my_acc.deposit(10000)
print()
print(my_acc, end="\n\n")
print(f"현재 잔액(Property): {my_acc.balance}원", end="\n\n")
print(f"총 거래 횟수: {len(my_acc)}회", end="\n\n")
for ts in my_acc:
    print(ts)