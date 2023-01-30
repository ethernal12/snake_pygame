from dataclasses import dataclass

from autologging import traced


@dataclass
@traced
class Snake:
    x: int
    y: int
    velikost: int

    def premik(self, dx: int, dy: int):
        self.x += dx
        self.y += dy
