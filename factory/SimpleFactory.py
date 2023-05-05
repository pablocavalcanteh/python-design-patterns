from abc import ABCMeta, abstractmethod

# Factory

class Factory:

    def create_animal(self, type):
        return eval(type)()


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        print('Au au au!')

class Cat(Animal):

    def speak(self):
        print('Miau!')


if __name__ == "__main__":

    factory = Factory()

    animal = factory.create_animal('Cat')
    animal.speak()

    animal = factory.create_animal('Dog')
    animal.speak()