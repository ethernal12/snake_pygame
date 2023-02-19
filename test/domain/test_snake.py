import unittest

from src.domain.del_kace import DelKace
from src.domain.snake import Snake


class Test_Snake(unittest.TestCase):
    def init_snake(self, x: int, y: int, dx: int, dy: int):
        return Snake(x=x, y=y, dx=dx, dy=dy)

    def setUp(self) -> None:
        self.snake_x = 5
        self.snake_y = 2
        self.snake_dx = 1
        self.snake_dy = 1
        self.snake = self.init_snake(x=self.snake_x, y=self.snake_y, dx=self.snake_dx, dy=self.snake_dy)

    def test___init__(self):
        self.assertEqual(self.snake.x, self.snake_x)
        self.assertEqual(self.snake.y, self.snake_y)
        self.assertEqual(self.snake.dx, self.snake_dx)
        self.assertEqual(self.snake.dy, self.snake_dy)
        self.assertEqual(self.snake.deli, [])

    # ali funkcija ustvari efekt, če ga treba efetkt testirati
    # ali funkcija vrača rezultat, če ga, treba rezultat testirati
    def test_smer_premika(self):
        # testiranje začetnega stanja
        self.assertEqual(self.snake.dx, self.snake_dx)
        self.assertEqual(self.snake.dy, self.snake_dy)
        dx_novi = 2
        dy_novi = 3
        self.assertNotEqual(self.snake_dx, dx_novi)
        self.assertNotEqual(self.snake_dy, dy_novi)
        # povzročimo efekt
        self.snake.smer_premika(dx=dx_novi, dy=dy_novi)
        # testiranje novega stanja
        self.assertEqual(self.snake.dx, dx_novi)
        self.assertEqual(self.snake.dy, dy_novi)

    def test_premikanje_brez_delov(self):
        # začetno stanje
        self.assertEqual(self.snake.deli, [])
        self.assertEqual(self.snake.x, self.snake_x)
        self.assertEqual(self.snake.y, self.snake_y)
        stari_x = self.snake.x
        stari_y = self.snake.y
        self.snake.dx = 3
        self.snake.dy = 5

        # efekt
        self.snake.premikanje()

        # končno stanje
        self.assertEqual(self.snake.x, stari_x + self.snake.dx)
        self.assertEqual(self.snake.y, stari_y + self.snake.dy)
        self.assertEqual(self.snake.deli, [])

    def test_premikanje_z_deli(self):
        # začetno stanje
        self.assertEqual(self.snake.deli, [])
        stari_x = self.snake.x
        stari_y = self.snake.y
        self.snake.deli = [
            DelKace(x=self.snake.x + 1, y=self.snake.y),
            DelKace(x=self.snake.x + 1, y=self.snake.y + 1),
            DelKace(x=self.snake.x + 2, y=self.snake.y + 1),
        ]

        # efekt
        self.snake.premikanje()

        # končno stanje
        self.assertEqual(self.snake.deli[0].x, stari_x)
        self.assertEqual(self.snake.deli[0].y, stari_y)

        self.assertEqual(self.snake.deli[1].x, stari_x + 1)
        self.assertEqual(self.snake.deli[1].y, stari_y)

        self.assertEqual(self.snake.deli[2].x, stari_x + 1)
        self.assertEqual(self.snake.deli[2].y, stari_y + 1)

    def test_dodaj_del_kace_brez_delov(self):
        self.assertEqual(self.snake.deli, [])

        self.snake.dodaj_del_kace()

        self.assertEqual(self.snake.deli, [DelKace(x=self.snake.x, y=self.snake.y)])

    def test_dodaj_del_kace_z_deli(self):
        self.snake.deli = [
            DelKace(x=self.snake.x + 1, y=self.snake.y),
            DelKace(x=self.snake.x + 1, y=self.snake.y + 1),
            DelKace(x=self.snake.x + 2, y=self.snake.y + 1),

        ]
        self.snake.dodaj_del_kace()
        self.assertEqual(self.snake.deli, [
            DelKace(x=self.snake.x + 1, y=self.snake.y),
            DelKace(x=self.snake.x + 1, y=self.snake.y + 1),
            DelKace(x=self.snake.x + 2, y=self.snake.y + 1),
            DelKace(x=self.snake.x + 2, y=self.snake.y + 1)
        ])


