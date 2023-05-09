from abc import ABCMeta, abstractmethod

class IProtoType(metaclass=ABCMeta):

    @abstractmethod
    def clone():
        pass

class Post(IProtoType):

    def __init__(self, title = None, text = None, author = None, date = None):
        self.__title = title
        self.__text = text
        self.__author = author
        self.__date = date
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, text):
        self.text = text

    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, date):
        self.__date = date
    
    def clone(self):

        return type(self) (
            self.__title,
            self.__text,
            self.__author,
            self.__date
        )
    
    def __str__(self) -> str:
        return f'Title: {self.__title}\nText: {self.__text}\nAuthor: {self.__author}\nDate: {self.__date}'

if __name__ == "__main__":

    post = Post('My Post 001', 'This is an post very cool.', 'Pablo Cavalcante', '09-05-2023')
    print(post)
    print(f'Object ID: {id(post)}')
    print('\n')
    post_copy = post.clone()
    print(post_copy)
    print(f'Object ID: {id(post_copy)}')
    
    
