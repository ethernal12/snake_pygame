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
    tocke: int = 0

    def __post_init__(self):
        self.snake = Snake(x=self.sirina / 2, y=self.visina / 2, dx=-1, dy=0)
        self.hrana = Hrana(
            x=random.randint(0, self.sirina),
            y=random.randint(0, self.visina))

    def nastavi_hrano(self):
        # dodano 1 in -1, da ni pozicija hrane izven meja zemlje
        self.hrana.x = random.randint(1, self.sirina - 1)
        self.hrana.y = random.randint(1, self.sirina - 1)

    def konec(self) -> bool:
        # če ima kača več kot 2 dela glej za dotik
        if len(self.snake.deli) > 1:
            for d in self.snake.deli:
                # poglej za dotik glave in del kače
                if d.x == self.snake.x and d.y == self.snake.y:
                    return False
        # če je kača v okviru dimenzij zemlje
        if 0 <= self.snake.x <= self.sirina and 0 <= self.snake.y <= self.visina:
            return True
        else:
            return False

    def dodaj_del_kace_in_nastavi_hrano(self) -> int:
        if self.snake.x == self.hrana.x and self.snake.y == self.hrana.y:
            self.snake.dodaj_del_kace()
            self.nastavi_hrano()
            self.tocke += 1
