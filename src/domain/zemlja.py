import logging
import random

from dataclasses import dataclass

from autologging import traced

from src.domain.hrana import Hrana
from src.domain.snake import Snake

log = logging.getLogger(__name__)


@dataclass
@traced
class Zemlja:
    sirina: int
    visina: int
    snake: Snake = None
    hrana: Hrana = None

    def __post_init__(self):
        self.snake = Snake(x=self.sirina / 2, y=self.visina / 2, dx=-1, dy=0, velikost=0)
        self.hrana = Hrana(
            x=random.randint(1, self.sirina - 1),
            y=random.randint(1, self.visina - 1))

    def nastavi_hrano(self):
        self.hrana.x = random.randint(1, self.sirina - 1)
        self.hrana.y = random.randint(1, self.sirina - 1)
