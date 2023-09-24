from abc import ABC, abstractmethod
from collections import deque
from typing import Deque

# Command
class Order(ABC):

    @abstractmethod
    def execute(self) -> None:
        ...

class Action:

    def buy(self) -> None:
        print('Buying stocks...')
    
    def sell(self) -> None:
        print('Selling stocks...')

class PurchaseOrder(Order):

    def __init__(self, action: Action):
        self.action = action
    
    def execute(self) -> None:
        self.action.buy()

class SalesOrder(Order):

    def __init__(self, action: Action):
        self.action = action
    
    def execute(self) -> None:
        self.action.sell()

class Agent:

    def __init__(self):
        self.__orders_stack: Deque[Order] = deque()
    
    def add_order_on_stack(self, order: Order):
        self.__orders_stack.append(order)
        order.execute()


if __name__ == "__main__":

    # Client
    action: Action = Action() # Receiver
    purchase_order: Order = PurchaseOrder(action)
    sell_order: Order = SalesOrder(action)

    # Invoker
    agent = Agent()
    agent.add_order_on_stack(purchase_order)
    agent.add_order_on_stack(sell_order)