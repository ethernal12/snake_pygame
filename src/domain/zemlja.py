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
            x=random.randint(1, self.sirina - 1),
            y=random.randint(1, self.visina - 1))

    def nastavi_hrano(self):
        self.hrana.x = random.randint(1, self.sirina - 1)
        self.hrana.y = random.randint(1, self.sirina - 1)

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
            return False
    # testiraj postavitve hrane
    def test_nakljucne_postavitve_hrane(self):
        for i in range(10):
            self.zemlja.nastavi_hrano()
            x = self.zemlja.hrana.x
            y = self.zemlja.hrana.y
            self.assertTrue(1 <= x <= self.zemlja.sirina - 1)
            self.assertTrue(1 <= y <= self.zemlja.sirina - 1)
