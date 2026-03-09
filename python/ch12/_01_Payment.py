from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount: int) -> None:
        """ 결제를 수행하는 메서드 """

    @abstractmethod
    def cancel(self, amount: int) -> None:
        """ 결제를 취소하는 메서드 """
