from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Any

class Builder(metaclass=ABCMeta):

    @property
    @abstractmethod
    def sandwich(self) -> None:
        pass

    @abstractmethod
    def add_meat(self) -> None:
        pass

    @abstractmethod
    def add_lettuce(self) -> None:
        pass

    @abstractmethod
    def add_tomato(self) -> None:
        pass

    @abstractmethod
    def add_onion(self) -> None:
        pass

    @abstractmethod
    def add_bread(self) -> None:
        pass

    @abstractmethod
    def add_sauce(self) -> None:
        pass

    @abstractmethod
    def add_olive(self) -> None:
        pass

    @abstractmethod
    def add_pepperoni_pepper(self) -> None:
        pass

    @abstractmethod
    def add_egg(self) -> None:
        pass

    @abstractmethod
    def sizeSmall(self) -> None:
        pass

    @abstractmethod
    def sizeMedium(self) -> None:
        pass

    @abstractmethod
    def sizeBig(self) -> None:
        pass

class Sandwich():
    
    def __init__(self) -> None:
        self._parts = []
    
    def add(self, part: Any) -> None:
        self._parts.append(part)

class SandwichBuilder(Builder):

    def __init__(self) -> None:
        self._sandwich = Sandwich()

    @property
    def sandwich(self) -> SandwichBuilder:
        return self._sandwich
    
    def reset(self) -> None:
        self._sandwich = Sandwich()

    def add_meat(self) -> SandwichBuilder:
        self._sandwich.add('Meat')
        return self

    def add_lettuce(self) -> SandwichBuilder:
        self._sandwich.add('Lettuce')
        return self

    def add_tomato(self) -> SandwichBuilder:
        self._sandwich.add('Tomato')
        return self

    def add_onion(self) -> SandwichBuilder:
        self._sandwich.add('Onion')
        return self

    def add_bread(self) -> SandwichBuilder:
        self._sandwich.add('Bread')
        return self

    def add_sauce(self) -> SandwichBuilder:
        self._sandwich.add('Sauce')
        return self

    def add_olive(self) -> SandwichBuilder:
        self._sandwich.add('Olive')
        return self

    def add_pepperoni_pepper(self) -> SandwichBuilder:
        self._sandwich.add('Pepperoni Pepper')
        return self

    def add_egg(self) -> SandwichBuilder:
        self._sandwich.add('Egg')
        return self

    def sizeSmall(self) -> SandwichBuilder:
        self._sandwich.add('Small')
        return self

    def sizeMedium(self) -> SandwichBuilder:
        self._sandwich.add('Medium')
        return self

    def sizeBig(self) -> SandwichBuilder:
        self._sandwich.add('Big')
        return self


if __name__ == "__main__":

    builder = SandwichBuilder()
    sandwich1 = builder.add_bread().add_lettuce().add_tomato().add_egg()
    print(sandwich1._sandwich._parts)


    builder.reset()
    sandwich2 = builder.add_bread().add_meat().add_bread().add_olive().add_onion()
    print(sandwich2._sandwich._parts)