""" Account.py """
from abc import ABC, abstractmethod


class Account(ABC):
    """ 모든 카드의 부모 클래스 """
    def __init__(self, owner: str, balance: int=0) -> None:
        self.owner = owner
        self._balance = balance

    @abstractmethod
    def withdraw(self, amount: int) -> None:
        """ 출금 로직 """
        pass

    def deposit(self, amount: int) -> None:
        """ 입금 로직 """
        if amount > 0:
            self._balance += amount

    def get_balance(self) -> int:
        return self._balance