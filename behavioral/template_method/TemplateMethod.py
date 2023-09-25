from abc import ABCMeta, abstractmethod

class Recipe(metaclass=ABCMeta):

    @abstractmethod
    def pick_out_ingredients(self):
        pass

    @abstractmethod
    def pre_preparation(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def serve(self):
        pass

    def cooking_recipe(self):
        self.pick_out_ingredients()
        self.pre_preparation()
        self.cook()
        self.serve()


class Cake(Recipe):

    def pick_out_ingredients(self):
        print('Picking out cake ingredients...')

    def pre_preparation(self):
        print('Pre-preparating...')

    def cook(self):
        print('Cooking cake...')

    def serve(self):
        print('Serving the cake...')

class Noodle(Recipe):

    def pick_out_ingredients(self):
        print('Picking out noodle ingredients...')

    def pre_preparation(self):
        print('Pre-preparating...')

    def cook(self):
        print('Cooking noodle...')

    def serve(self):
        print('Serving the noodle...')


if __name__ == '__main__':

    cake: Recipe = Cake()
    noodle: Recipe = Noodle()

    cake.cooking_recipe()
    print('----', end='\n')
    noodle.cooking_recipe()
