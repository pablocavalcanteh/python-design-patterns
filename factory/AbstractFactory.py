from abc import ABCMeta, abstractmethod


class FurnitureFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass

    @abstractmethod
    def create_coffee_table(self):
        pass

# Concrete Factory

class VictorianFurnitureFactory(FurnitureFactory):
    
    def create_chair(self):
        return VictorianChair()

    def create_sofa(self):
        return VictorianSofa()

    def create_coffee_table(self):
        return VictorianCoffeTable()

# Concrete Factory

class ArtDecFurnitureFactory(FurnitureFactory):
    
    def create_chair(self):
        return ArtDecChair(self)

    def create_sofa(self):
        return ArtDecSofa()

    def create_coffee_table(self):
        return ArtDecCoffeTable()

# Concrete Factory

class ModernFurnitureFactory(FurnitureFactory):

    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()

    def create_coffee_table(self):
        return ModernCoffeTable()

class Chair(metaclass=ABCMeta):
    
    @abstractmethod
    def sit_on(self):
        pass

class Sofa(metaclass=ABCMeta):
    
    @abstractmethod
    def sit_on(self):
        pass

class CoffeTable(metaclass=ABCMeta):
    
    @abstractmethod
    def put_on(self):
        pass

# Concrete Chair

class VictorianChair(Chair):
    
    def sit_on(self):
        return 'Sit'

class ArtDecChair(Chair):

    def sit_on(self):
        return 'Sit'

class ModernChair(Chair):
    
    def sit_on(self):
        return 'Sit'

# Concrete Sofa

class VictorianSofa(Sofa):

    def sit_on(self):
        return 'Sit'

class ArtDecSofa(Sofa):
    
    def sit_on(self):
        return 'Sit'

class ModernSofa(Sofa):
    
    def sit_on(self):
        return 'Sit'

# Concrete CoffeTable

class VictorianCoffeTable(CoffeTable):

    def put_on(self):
        return 'Put'

class ArtDecCoffeTable(CoffeTable):
    
    def put_on(self):
        return 'Put'

class ModernCoffeTable(CoffeTable):
    
    def put_on(self):
        return 'Put'


if __name__ == "__main__":
    

    furniture_factory = VictorianFurnitureFactory()

    chair = furniture_factory.create_chair()
    sofa = furniture_factory.create_sofa()
    coffe_table = furniture_factory.create_coffee_table()

    print(f'{type(chair).__name__}')
    print(f'{type(sofa).__name__}')
    print(f'{type(coffe_table).__name__}')