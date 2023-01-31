from abc import ABC, abstractmethod

class App(ABC):
    @abstractmethod
    def new_game(self):
        pass

    @abstractmethod
    def draw_game(self):
        pass

    @abstractmethod
    def input(self):
        pass

    @abstractmethod
    def end_game_conditions(self):
        pass