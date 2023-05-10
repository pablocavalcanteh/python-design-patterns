
class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


if __name__ == "__main__":
    
    singleton1 = Singleton()
    singleton2 = Singleton()

    print(f'Singleton 1: {id(singleton1)}')
    print(f'Singleton 2: {id(singleton2)}')
