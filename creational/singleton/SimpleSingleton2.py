
class Singleton:

    __instance = None

    def __init__(self) -> None:
    
        if Singleton.__instance != None:
           pass
        else:
            Singleton.__instance = self
    
    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance


if __name__ == "__main__":
    
    singleton1 = Singleton()
    singleton2 = Singleton()

    print(f'Singleton 1: {id(singleton1.getInstance())}')
    print(f'Singleton 2: {id(singleton2.getInstance())}')

    print(f'{singleton1.getInstance() is singleton2.getInstance()}')
