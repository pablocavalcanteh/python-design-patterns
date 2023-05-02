
class LazySingleton:

    __instance = None

    def __init__(self):
        if not LazySingleton.__instance:
            print('There is no yet.')

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance


if __name__ == "__main__":

    singleton1 = LazySingleton(); # It hasn't been created yet, just the class has been initialized.
    singleton1.get_instance()
    singleton2 = LazySingleton();
    singleton3 = LazySingleton()

    print(f'Singleton2: {id(singleton2.get_instance())}')
    print(f'Singleton3: {id(singleton3.get_instance())}')