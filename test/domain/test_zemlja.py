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
            # testiranje začetnega stanja
            self.zemlja = Zemlja(self.sirina, self.visina)
            self.assertEqual(self.zemlja.visina, self.visina)
            self.assertEqual(self.zemlja.sirina, self.sirina)
            # novo stanje
            stara_sirina = self.zemlja.sirina
            stara_visina = self.zemlja.visina
            self.zemlja.sirina = 9
            self.zemlja.visina = 8
            self.assertNotEqual(stara_sirina, self.zemlja.sirina)
            self.assertNotEqual(stara_visina, self.zemlja.visina)

            self.assertEqual(self.zemlja.visina, self.visina)
            self.assertEqual(self.zemlja.sirina, self.sirina)

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
        self.zemlja.snake.x = self.zemlja.sirina - 1
        self.zemlja.snake.y = self.zemlja.visina - 1
        self.assertEqual(self.zemlja.konec(), True)
        self.zemlja.snake.x = self.zemlja.sirina + 1
        self.zemlja.snake.y = self.zemlja.visina + 1
        self.assertEqual(self.zemlja.konec(), False)

    def test_dodaj_del_kace_in_nastavi_hrano(self):
        # testiranje return vrednosti
        self.zemlja.snake.x = self.zemlja.hrana.x
        self.zemlja.snake.y = self.zemlja.hrana.y
        self.assertEqual(self.zemlja.dodaj_del_kace_in_nastavi_hrano(), 1)
        self.zemlja.hrana.y = 5
        self.assertEqual(self.zemlja.dodaj_del_kace_in_nastavi_hrano(), 0)
        # testiranje efekta dodajanja dela kače
        # začetno stanje
        self.zemlja.snake.deli = []
        self.assertEqual(self.zemlja.snake.deli, [])
        self.zemlja.snake.x = self.zemlja.hrana.x
        self.zemlja.snake.y = self.zemlja.hrana.y
        # efekt
        self.zemlja.dodaj_del_kace_in_nastavi_hrano()
        self.assertNotEqual(self.zemlja.snake.deli, [])
        # testiranje efekta nastavljanja hrane
        self.zemlja.snake.x = self.zemlja.hrana.x
        self.zemlja.snake.y = self.zemlja.hrana.y
        # začetno stanje
        stara_vrednost_hrane_x = self.zemlja.hrana.x
        stara_vrednost_hrane_y = self.zemlja.hrana.y
        # efekt
        self.zemlja.dodaj_del_kace_in_nastavi_hrano()
        self.assertNotEqual(stara_vrednost_hrane_x, self.zemlja.hrana.x)
        self.assertNotEqual(stara_vrednost_hrane_y, self.zemlja.hrana.y)



