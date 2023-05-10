from abc import ABCMeta, abstractmethod

class Section(metaclass=ABCMeta):

    @abstractmethod
    def __repr__(self):
        pass


class PrivateSection(Section):

    def __repr__(self):
        return 'Private Section'

class AlbumSection(Section):

    def __repr__(self):
        return 'Album Section'
    
class ProjectSection(Section):

    def __repr__(self):
        return 'Project Section'
    

class Profile(metaclass=ABCMeta):

    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections
    
    def add_section(self, section):
        self.sections.append(section)


class Linkedin(Profile):

    def create_profile(self):
        self.add_section(PrivateSection())
        self.add_section(ProjectSection())

class Facebook(Profile):

    def create_profile(self):
        self.add_section(PrivateSection())
        self.add_section(AlbumSection())

if __name__ == "__main__":
    
    social_network = eval('Linkedin')()
    print(f'{type(social_network).__name__}')
    print(f'{social_network.get_sections()}')
