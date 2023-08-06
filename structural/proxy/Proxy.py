from abc import ABCMeta, abstractmethod
from typing import Union, Any

class Wallet(metaclass=ABCMeta):
    
    @abstractmethod
    def pay(self) -> Union[None, bool]:
        pass

class Bank(Wallet):
    
    def __init__(self) -> None:
        self.__card = None
        self.__account = None
    
    def pay(self) -> Union[None, bool]:
        
        if self.has_balance():
            print('Paid!')
        else:
            print('Sorry, but you dont have enough balance!')

    def has_balance(self) -> bool:
        return True
    
    def get_account(self) -> Any:
        self.__account = self.__card
        return self.__account
    
    def set_card(self, card) -> None:
        self.__card = card

# This class is the proxy one.
class DebitCard(Wallet):

    def __init__(self) -> None:
        self.__bank = Bank()
    
    def pay(self) -> Union[None, bool]:
        self.__bank.set_card('123-456-789-000')
        self.__bank.pay() # Who really pays is the bank...

# Client role here.
if __name__ == "__main__":

    debit_card = DebitCard()
    debit_card.pay()
