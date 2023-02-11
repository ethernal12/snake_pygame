import logging
import unittest

from src.domain.hrana import Hrana
from src.domain.snake import Snake
from src.domain.zemlja import Zemlja


class Test_Zemlja(unittest.TestCase):

    def setUp(self) -> None:
        self.sirina = 10
        self.visina = 10
        self.zemlja = Zemlja(self.sirina, self.visina, )

    def test___init__(self):
        for _ in range(100):
            self.zemlja = Zemlja(self.sirina, self.visina)
            self.assertEqual(self.zemlja.visina, self.visina)
            self.assertEqual(self.zemlja.sirina, self.sirina)
            self.assertTrue(isinstance(self.zemlja.snake, Snake))
            self.assertTrue(isinstance(self.zemlja.hrana, Hrana))
            self.assertTrue(0 <= self.zemlja.snake.x <= self.sirina)
            self.assertTrue(0 <= self.zemlja.snake.y <= self.visina)
            self.assertTrue(0 <= self.zemlja.hrana.x <= self.sirina)
            self.assertTrue(0 <= self.zemlja.hrana.y <= self.visina)

    def test_konec_igre(self):
        self.zemlja.snake.x = self.zemlja.sirina - 1
        self.zemlja.snake.y = self.zemlja.visina - 1
        self.assertEqual(self.zemlja.konec(), True)
        self.zemlja.snake.x = self.zemlja.sirina + 1
        self.zemlja.snake.y = self.zemlja.visina + 1
        self.assertEqual(self.zemlja.konec(), False)

    def test_nastavi_hrano(self):
        for _ in range(100):
            self.zemlja.nastavi_hrano()
            self.assertTrue(0 <= self.zemlja.hrana.x <= self.zemlja.sirina)
            self.assertTrue(0 <= self.zemlja.hrana.y <= self.zemlja.visina)
