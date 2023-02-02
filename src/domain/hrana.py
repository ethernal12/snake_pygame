from dataclasses import dataclass

from autologging import traced
import random


@dataclass
@traced
class Hrana:
    x: int
    y: int

