
class Monostate:

    __state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__state
        return obj


if __name__ == '__main__':

    monostate1 = Monostate()
    print(f'Monostate {id(monostate1)}')
    print(monostate1.__dict__)

    monostate2 = Monostate()
    print(f'Monostate {id(monostate2)}')
    print(monostate2.__dict__)

    monostate2.name = 'I am Pablo Cavalcante...'

    # Although the instances are different, they have the same state.
    
    print(monostate1.__dict__)
    print(monostate2.__dict__)