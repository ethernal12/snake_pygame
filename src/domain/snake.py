from dataclasses import dataclass

from autologging import traced


@dataclass
@traced
class Snake:
    x: int
    y: int
    dx: int
    dy: int
    velikost: int

    def smer_premika(self, dx: int, dy: int):
        self.dx = dx
        self.dy = dy

    def premikanje(self):
        self.x += self.dx
        self.y += self.dy

