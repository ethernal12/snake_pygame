import unittest

import pygame

from src.app.GUI import GUI
from unittest.mock import MagicMock, patch


class Test_GUI(unittest.TestCase):
    def setUp(self) -> None:
        self.width = 400
        self.height = 400
        self.GUI = GUI(self.width, self.height)
        self.zemlja = MagicMock()
        self.snake = MagicMock()
        self.zemlja.snake = self.snake

    @patch('pygame.event.get', return_value=[
        pygame.event.Event(pygame.KEYDOWN, key=pygame.K_w),
        pygame.event.Event(pygame.KEYDOWN, key=pygame.K_d),
        pygame.event.Event(pygame.KEYDOWN, key=pygame.K_s),
        pygame.event.Event(pygame.KEYDOWN, key=pygame.K_q),
    ])
    def test_init(self, mock_event_get):
        self.assertTrue(isinstance(self.GUI, GUI))
        self.assertEqual(self.GUI.width, self.width)
        self.assertEqual(self.GUI.height, self.height)
        self.assertEqual(self.GUI.tocke, 0)
        self.assertEqual(self.GUI.dx, 0)
        self.assertEqual(self.GUI.dx, 0)
        self.assertTrue(isinstance(self.GUI.windowSurface, pygame.Surface))

    def test_end_game_conditions(self):
        pass

    def snake_reset(self):
        self.GUI.zemlja.snake.x = 10
        self.GUI.zemlja.snake.y = 10
        self.GUI.zemlja.snake.dx = 0
        self.GUI.zemlja.snake.dy = 0

    def test_new_game(self):
        # začetno stanje
        self.assertEqual(self.GUI.zemlja, None)
        # efekt
        self.GUI.new_game()
        # test spremembe
        self.assertEqual(self.GUI.zemlja.sirina, 20)
        self.assertEqual(self.GUI.zemlja.visina, 20)

    def test_draw_game(self):
        self.GUI.new_game()
        self.GUI.draw_game()
        self.assertEqual(self.GUI.dx, self.GUI.width / self.GUI.dx)
        self.assertEqual(self.GUI.dy, self.GUI.height / self.GUI.dx)

    def test_input(self):
        # kličemo funkcijo da se ustvari objekt zemlja in tako snake objekt
        self.GUI.new_game()

        # zmokamo event
        event = MagicMock()
        event.type = pygame.KEYDOWN

        # testiranje premika s tipko a - levo
        event.key = pygame.K_a
        pygame.event.get = MagicMock(return_value=[event])
        self.snake_reset()
        self.assertEqual(self.GUI.zemlja.snake.dx, 0)
        self.assertEqual(self.GUI.zemlja.snake.dy, 0)
        self.assertEqual(self.GUI.zemlja.snake.x, 10)
        self.assertEqual(self.GUI.zemlja.snake.y, 10)

        # test spremembe smeri
        self.GUI.input()
        self.assertEqual(self.GUI.zemlja.snake.dx, -1)
        self.assertEqual(self.GUI.zemlja.snake.dy, 0)

        # test premikanja
        self.GUI.input()
        self.assertEqual(self.GUI.zemlja.snake.x, 9)
        self.assertEqual(self.GUI.zemlja.snake.y, 10)

        # testiranje premika s tipko d - desno
        self.snake_reset()
        self.assertEqual(self.GUI.zemlja.snake.dx, 0)
        self.assertEqual(self.GUI.zemlja.snake.dy, 0)
        self.assertEqual(self.GUI.zemlja.snake.x, 10)
        self.assertEqual(self.GUI.zemlja.snake.y, 10)

        event.key = pygame.K_d
        pygame.event.get = MagicMock(return_value=[event])

        self.GUI.input()
        # test spremembe smeri
        self.assertEqual(self.GUI.zemlja.snake.dx, 1)
        self.assertEqual(self.GUI.zemlja.snake.dy, 0)

        # test premikanja
        self.GUI.input()
        self.assertEqual(self.GUI.zemlja.snake.x, 11)
        self.assertEqual(self.GUI.zemlja.snake.y, 10)

        # testiranje premika s tipko w - gor

        self.snake_reset()
        self.assertEqual(self.GUI.zemlja.snake.dx, 0)
        self.assertEqual(self.GUI.zemlja.snake.dy, 0)
        self.assertEqual(self.GUI.zemlja.snake.x, 10)
        self.assertEqual(self.GUI.zemlja.snake.y, 10)

        event.key = pygame.K_w
        pygame.event.get = MagicMock(return_value=[event])

        self.GUI.input()
        # test spremembe smeri
        self.assertEqual(self.GUI.zemlja.snake.dx, 0)
        self.assertEqual(self.GUI.zemlja.snake.dy, -1)

        # test premikanja
        self.GUI.input()
        self.assertEqual(self.GUI.zemlja.snake.x, 10)
        self.assertEqual(self.GUI.zemlja.snake.y, 9)

        # testiranje premika s tipko s - dol
        self.snake_reset()
        self.assertEqual(self.GUI.zemlja.snake.dx, 0)
        self.assertEqual(self.GUI.zemlja.snake.dy, 0)
        self.assertEqual(self.GUI.zemlja.snake.x, 10)
        self.assertEqual(self.GUI.zemlja.snake.y, 10)

        event.key = pygame.K_s
        pygame.event.get = MagicMock(return_value=[event])

        self.GUI.input()
        # test spremembe smeri
        self.assertEqual(self.GUI.zemlja.snake.dx, 0)
        self.assertEqual(self.GUI.zemlja.snake.dy, 1)

        # test premikanja
        self.GUI.input()
        self.assertEqual(self.GUI.zemlja.snake.x, 10)
        self.assertEqual(self.GUI.zemlja.snake.y, 11)

        # testiranje izhoda ob pritisku tipke q
        with patch('sys.exit') as mock_sys_exit:
            event.key = pygame.K_q
            pygame.event.get = MagicMock(return_value=[event])

            self.GUI.input()

            mock_sys_exit.assert_called_once()
