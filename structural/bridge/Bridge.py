from abc import ABCMeta, abstractmethod

class Device(metaclass=ABCMeta):

    @abstractmethod
    def isEnabled(self) -> bool:
        pass
    
    @abstractmethod
    def enable_or_disable_toggle(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

class Remote(metaclass=ABCMeta):

    @abstractmethod
    def power() -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

class TV(Device):


    def __init__(self) -> None:
        self.on = False

    def isEnabled(self) -> bool:
        return self.on
    
    def enable_or_disable_toggle(self) -> None:
        self.on = not self.on

    def __str__(self) -> str:
        return f'TV + '

class Computer(Device):

    def __init__(self) -> None:
        self.on = False

    def isEnabled(self) -> bool:
        self.on = False
    
    def enable_or_disable_toggle(self) -> None:
        self.on = not self.on

    def __str__(self) -> str:
        return f'Compute + '

class BasicRemote(Remote):

    def __init__(self, device: Device) -> None:
        self.device = device

    def power() -> None:
        pass

    def __str__(self) -> str:
        return f'{self.device.__str__()}Basic Remote'

class MediumRemote(Remote):

    def __init__(self, device: Device) -> None:
        self.device = device

    def power() -> None:
        pass

    def __str__(self) -> str:
        return f'{self.device.__str__()}Medium Remote'
    
if __name__ == "__main__":

    device1: Device = TV()
    device2: Device = Computer()

    basic_remote1: Remote = BasicRemote(device1)
    basic_remote2: Remote = BasicRemote(device2)
    
    medium_remote1: Remote = MediumRemote(device1)
    medium_remote2: Remote = MediumRemote(device2)

    print(basic_remote1)
    print(basic_remote2)
    print(medium_remote1)
    print(medium_remote2)