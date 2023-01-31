import unittest

from src.domain.hrana import Hrana
from src.domain.snake import Snake


class Test_Snake(unittest.TestCase):
    def init_snake(self, x: int, y: int):
        return Snake(x=x, y=y, velikost=self.snake_velikost)

    def setUp(self) -> None:
        self.snake_x = 5
        self.snake_y = 2
        self.snake_velikost = 0
        self.snake_dx = 2
        self.snake_dy = 1
        self.snake = self.init_snake(x=self.snake_x, y=self.snake_y)

    def test___init__(self):
        self.assertEqual(self.snake.x, self.snake_x)
        self.assertEqual(self.snake.y, self.snake_y)
        self.assertEqual(self.snake.velikost, self.snake_velikost)

    def test_postavitev(self):
        for i in range(5):
            # pozitivna sprememba
            self.snake = self.init_snake(x=self.snake_x, y=self.snake_y)
            x = self.snake.x
            y = self.snake.y
            self.snake.premik(dx=self.snake_dx, dy=self.snake_dy)
            x_nova = self.snake.x
            y_nova = self.snake.y
            self.assertTrue(x < x_nova)
            self.assertTrue(y < y_nova)
            # negativna sprememba
            self.snake = self.init_snake(x=self.snake_x, y=self.snake_y)
            x = self.snake.x
            y = self.snake.y
            self.snake.premik(dx=- self.snake_dx, dy=- self.snake_dy)
            x_nova = self.snake.x
            y_nova = self.snake.y
            self.assertTrue(x > x_nova)
            self.assertTrue(y > y_nova)
    def test_premik(self):
