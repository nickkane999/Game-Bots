from abc import ABC, abstractmethod


class MenuTemplate(ABC):
    # Initializing Object
    def __init__(self):
        self.class_name = self.getClass()

    @abstractmethod
    def selectMenu(self):
        pass

    def getClass(self):
        # print(type(self).__name__)
        return type(self).__name__
