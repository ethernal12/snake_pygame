from abc import ABC, abstractmethod

class App(ABC):
    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def input(self):
        pass

    @abstractmethod
    def konec(self):
        pass

