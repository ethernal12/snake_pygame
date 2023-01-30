from dataclasses import dataclass

from autologging import traced


@dataclass
@traced
class Hrana:
    x: int
    y: int
