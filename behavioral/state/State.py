from abc import ABCMeta

class ComputerState(metaclass=ABCMeta):

    state: str = 'Turn On'
    states: list[str] = []
    
    def change(self, state):

        if state.state in self.states:
            print(f'Next state: {state.state}')
            self.__class__ = state
        else:
            print(f'Currently: {self}')
    

    def __str__(self):
        return self.state
    
class TurnOnComputer(ComputerState):
    state: str = 'Turn On'
    states: list[str] = ['Turn Off', 'Suspend', 'Hibernate']


class TurnOffComputer(ComputerState):
    state: str = 'Turn Off'
    states: list[str] = ['Turn On']

class SuspendedComputer(ComputerState):
    state: str = 'Suspended'
    states: list[str] = ['Turn On']

class HibernateComputer(ComputerState):
    state: str = 'Hibernate'
    states: list[str] = ['Turn On']


class Computer:

    def __init__(self):
        self.state = TurnOffComputer()
    
    def change(self, state):
        self.state.change(state)

if __name__ == '__main__':
    
    computer = Computer()

    computer.change(TurnOnComputer)
    computer.change(TurnOffComputer)
    computer.change(TurnOnComputer)
    computer.change(SuspendedComputer)
    computer.change(HibernateComputer)
    computer.change(TurnOnComputer)
    computer.change(TurnOffComputer)