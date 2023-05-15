from abc import ABCMeta, abstractmethod

class JSONFormat(metaclass=ABCMeta):
    
    @abstractmethod
    def readJSON(self, json):
        pass

class YAMLFormat(metaclass=ABCMeta):
    
    @abstractmethod
    def readYAML(self, yaml):
        pass

class Algorithm1JSONFormat(JSONFormat):

    def readJSON(self, json):
        print(f'Reading JSON...\n{json}')

class Algorithm1YAMLFormat(YAMLFormat):

    def readYAML(self, yaml):
        print(f'Reading YAML...\n{yaml}')

class JSONToYAMLAdapter(JSONFormat):

    def __init__(self, yamlFormat: YAMLFormat) -> None:
        self.yamlFormat = yamlFormat

    def readJSON(self, yaml):
        self.yamlFormat.readYAML(yaml)

class JSONGenericReader:

    def __init__(self, jsonFormat: JSONFormat) -> None:
        self.jsonFormat = jsonFormat

    def readJSON(self, yaml) -> None:
        self.jsonFormat.readJSON(yaml)


if __name__ == "__main__":

    algorithm1JSONFormat = Algorithm1JSONFormat()
    algorithm1YAMLFormat = Algorithm1YAMLFormat()

    yamlToJSONAdapter = JSONToYAMLAdapter(algorithm1YAMLFormat)

    jSONGenericReader = JSONGenericReader(yamlToJSONAdapter)
    jSONGenericReader.readJSON('yaml')
    

