import unittest

from src.domain.snake import Snake
from src.domain.zemlja import Zemlja
from src.app.GUI import GUI


class Test_Snake(unittest.TestCase):
    def init_snake(self, x: int, y: int, dx: int, dy: int):
        return Snake(x=x, y=y, dx=dx, dy=dy)

    def setUp(self) -> None:
        self.snake_x = 5
        self.snake_y = 2
        self.snake_dx = 1
        self.snake_dy = 1
        self.snake = self.init_snake(x=self.snake_x, y=self.snake_y, dx=self.snake_dx, dy=self.snake_dy)
        self.zemlja = Zemlja(10, 10)
        self.GUI = GUI(400, 400, 0)

    def test___init__(self):
        self.assertEqual(self.snake.x, self.snake_x)
        self.assertEqual(self.snake.y, self.snake_y)

    def test_premik_glave(self):
        for i in range(5):
            # pozitivna sprememba
            self.snake = self.init_snake(x=self.snake_x, y=self.snake_y, dx=self.snake_dx, dy=self.snake_dy)
            x = self.snake.x
            y = self.snake.y
            self.snake.smer_premika(dx=self.snake_dx, dy=self.snake_dy)
            self.snake.premikanje()
            x_nova = self.snake.x
            y_nova = self.snake.y
            self.assertTrue(x < x_nova)
            self.assertTrue(y < y_nova)
            # negativna sprememba
            self.snake = self.init_snake(x=self.snake_x, y=self.snake_y, dx=self.snake_dx, dy=self.snake_dy)
            x = self.snake.x
            y = self.snake.y
            self.snake.smer_premika(dx=- self.snake_dx, dy=- self.snake_dy)
            self.snake.premikanje()
            x_nova = self.snake.x
            y_nova = self.snake.y
            self.assertTrue(x > x_nova)
            self.assertTrue(y > y_nova)

    def test_premik_telesa_kače(self):
        # dodaj N * kos kace
        for _ in range(2):
            self.snake.dodaj_del_kace()
        self.snake.smer_premika(self.snake_dx, 0)
        # premakni kačo dokler ni premaknjen ves del kače
        for i in range(2):
            self.snake.premikanje()
            for j in range(len(self.snake.deli)):
                print(self.snake.deli[j].x)
                if i > 0:
                    if j == 0:
                        self.assertEqual(self.snake.deli[j].x, self.snake.x - 1)
                    elif j > 0:
                        self.assertEqual(self.snake.deli[j].x, self.snake.deli[j - 1].x - 1)

    def test_smpremembe_smeri(self):
        self.init_snake(x=self.snake_x, y=self.snake_y, dx=self.snake_dx, dy=self.snake_dy)
        y = self.snake.y
        self.snake.premikanje()
        self.assertTrue(self.snake.y > y)
        x = self.snake.x
        self.snake.smer_premika(1, 0)
        self.snake.premikanje()
        self.assertTrue(self.snake.x > x)

    def test_pobiranje_hrane(self):
        self.assertEqual(len(self.zemlja.snake.deli), 0)
        self.zemlja.hrana.x = 10
        self.zemlja.hrana.y = 10
        self.zemlja.snake.x = 10
        self.zemlja.snake.y = 10
        int = self.zemlja.dodaj_del_kace_in_nastavi_hrano()
        self.assertEqual(len(self.zemlja.snake.deli), 1)
        self.assertEqual(int, 1)
