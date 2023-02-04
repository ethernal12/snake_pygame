import unittest

from src.domain.hrana import Hrana
from src.domain.zemlja import Zemlja


class Test_Hrana(unittest.TestCase):

    def setUp(self) -> None:
        self.hrana_x = 5
        self.hrana_y = 2
        self.hrana = Hrana(x=self.hrana_x, y=self.hrana_y)
        self.zemlja = Zemlja(10, 10)

    def test___init__(self):
        self.assertTrue(self.hrana.x, self.hrana_x)
        self.assertEqual(self.hrana.y, self.hrana_y)

    def test_nakljucne_postavitve_hrane(self):
        for i in range(10):
            self.zemlja.nastavi_hrano()
            x = self.zemlja.hrana.x
            y = self.zemlja.hrana.y
            self.assertTrue(1 <= x <= self.zemlja.sirina - 1)
            self.assertTrue(1 <= y <= self.zemlja.sirina - 1)
