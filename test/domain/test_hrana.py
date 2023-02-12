import unittest

from src.domain.hrana import Hrana
from src.domain.zemlja import Zemlja


class Test_Hrana(unittest.TestCase):

    def setUp(self) -> None:
        self.hrana_x = 5
        self.hrana_y = 2
        self.hrana = Hrana(x=self.hrana_x, y=self.hrana_y)

    def test___init__(self):
        self.assertTrue(self.hrana.x, self.hrana_x)
        self.assertEqual(self.hrana.y, self.hrana_y)


