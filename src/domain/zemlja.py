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
        self.snake = Snake(x=self.sirina / 2, y=self.visina / 2, dx=-1, dy=0)
        self.hrana = Hrana(
            x=random.randint(0, self.sirina),
            y=random.randint(0, self.visina))

    def nastavi_hrano(self):
        self.hrana.x = random.randint(0, self.sirina)
        self.hrana.y = random.randint(0, self.sirina)

    def konec(self) -> bool:
        # če je kača v okviru dimenzij zemlje
        if 0 <= self.snake.x < self.sirina and 0 <= self.snake.y < self.visina:
            return True
        else:
            return False

    def dodaj_del_kace_in_nastavi_hrano(self) -> int:
        if self.snake.x == self.hrana.x and self.snake.y == self.hrana.y:
            self.snake.dodaj_del_kace()
            self.nastavi_hrano()
            return 1
        else:
            return 0


