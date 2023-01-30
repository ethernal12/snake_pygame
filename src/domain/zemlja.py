import logging
import random
import trace
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
        self.snake = Snake(x=self.sirina / 2, y=self.sirina / 2, velikost=0)
        self.hrana = Hrana(
            x=random.randint(0, self.sirina),
            y=random.randint(0, self.visina))
