import logging
import unittest

from src.domain.del_kace import DelKace
from src.domain.hrana import Hrana
from src.domain.snake import Snake
from src.domain.zemlja import Zemlja


class Test_Zemlja(unittest.TestCase):

    def setUp(self) -> None:
        self.sirina = 10
        self.visina = 10
        self.zemlja = Zemlja(self.sirina, self.visina)

    def test___init__(self):
        for _ in range(100):
            # testiranje začetnega stanja
            self.zemlja = Zemlja(self.sirina, self.visina)
            self.assertEqual(self.zemlja.visina, self.visina)
            self.assertEqual(self.zemlja.sirina, self.sirina)
            self.assertEqual(self.zemlja.tocke, 0)

            self.assertTrue(isinstance(self.zemlja.snake, Snake))
            self.assertTrue(isinstance(self.zemlja.hrana, Hrana))
            self.assertTrue(0 <= self.zemlja.snake.x <= self.sirina)
            self.assertTrue(0 <= self.zemlja.snake.y <= self.visina)
            self.assertTrue(0 <= self.zemlja.hrana.x <= self.sirina)
            self.assertTrue(0 <= self.zemlja.hrana.y <= self.visina)

    def test_nastavi_hrano(self):
        self.assertTrue(0 <= self.zemlja.hrana.x <= self.zemlja.sirina)
        self.assertTrue(0 <= self.zemlja.hrana.y <= self.zemlja.visina)

        for _ in range(10):
            self.zemlja.nastavi_hrano()
            self.assertTrue(0 <= self.zemlja.hrana.x <= self.zemlja.sirina)
            self.assertTrue(0 <= self.zemlja.hrana.y <= self.zemlja.visina)

    def test_konec_(self):
        # testiraj če se glava dotika dela kače z enim delom

        self.zemlja.snake.deli = [DelKace(self.zemlja.snake.x, self.zemlja.snake.y)]
        self.assertEqual(self.zemlja.konec(), False)
        # testiraj če se glava dotika dela kače z dvemi deli

        self.zemlja.snake.deli = [DelKace(self.zemlja.snake.x, self.zemlja.snake.y),
                                  DelKace(self.zemlja.snake.x, self.zemlja.snake.y)]
        self.assertEqual(self.zemlja.konec(), True)

        # ustvari in  testiraj kombinacije pozicije kače izven obsega zemlje
        x, y = self.sirina + 1, 5
        self.zemlja.snake.x, self.zemlja.snake.y = x, y
        self.assertEqual(self.zemlja.konec(), True)
        x, y = - 1, 5
        self.zemlja.snake.x, self.zemlja.snake.y = x, y
        self.assertEqual(self.zemlja.konec(), True)
        x, y = 5, self.visina + 1
        self.zemlja.snake.x, self.zemlja.snake.y = x, y
        self.assertEqual(self.zemlja.konec(), True)
        x, y = 5, - 1
        self.zemlja.snake.x, self.zemlja.snake.y = x, y
        self.assertEqual(self.zemlja.konec(), True)
        # ustvari in  testiraj  kombinacije pozicije kače znotraj obsega zemlje
        x, y = self.sirina - 1, 5
        self.zemlja.snake.x, self.zemlja.snake.y = x, y
        self.assertEqual(self.zemlja.konec(), False)
        x, y = 1, 5
        self.zemlja.snake.x, self.zemlja.snake.y = x, y
        self.assertEqual(self.zemlja.konec(), False)
        x, y = 5, self.visina - 1
        self.zemlja.snake.x, self.zemlja.snake.y = x, y
        self.assertEqual(self.zemlja.konec(), False)
        x, y = 5, 1
        self.zemlja.snake.x, self.zemlja.snake.y = x, y
        self.assertEqual(self.zemlja.konec(), False)
        # ustvari in  testiraj  pozcijo kače na robovih
        x, y = 0, 0
        self.zemlja.snake.x, self.zemlja.snake.y = x, y
        self.assertEqual(self.zemlja.konec(), False)
        x, y = 0, self.visina
        self.zemlja.snake.x, self.zemlja.snake.y = x, y
        self.assertEqual(self.zemlja.konec(), False)
        x, y = self.sirina, 0
        self.zemlja.snake.x, self.zemlja.snake.y = x, y
        self.assertEqual(self.zemlja.konec(), False)
        x, y = self.sirina, self.visina
        self.zemlja.snake.x, self.zemlja.snake.y = x, y
        self.assertEqual(self.zemlja.konec(), False)

    def test_premakni(self):
        # začetna vrednost
        self.assertEqual(self.zemlja.snake.deli, [])
        self.assertEqual(self.zemlja.tocke, 0)
        # efekt
        self.zemlja.snake.x = self.zemlja.hrana.x
        self.zemlja.snake.y = self.zemlja.hrana.y
        self.zemlja.premakni()
        self.assertEqual(self.zemlja.tocke, 1)
        # končna vrednost
        self.assertEqual(len(self.zemlja.snake.deli), 1)
        # reset vrednosti
        self.zemlja.snake.deli = []
        self.zemlja.tocke = 0
        # efekt
        self.zemlja.snake.x = self.zemlja.hrana.x
        self.zemlja.snake.y = self.zemlja.hrana.y - 1
        self.zemlja.premakni()
        self.assertEqual(self.zemlja.snake.deli, [])
        self.assertEqual(self.zemlja.tocke, 0)
