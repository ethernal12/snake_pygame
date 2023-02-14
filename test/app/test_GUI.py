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
        pygame.event.Event(pygame.KEYDOWN, key=pygame.K_e),
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

        # pokličemo funkcijo input()

        # testiranje premika s tipko a - levo
        event.key = pygame.K_a
        pygame.event.get = MagicMock(return_value=[event])
        self.GUI.zemlja.snake.dx = 0
        self.GUI.zemlja.snake.dy = 0
        self.assertEqual(self.GUI.zemlja.snake.dx, 0)
        self.assertEqual(self.GUI.zemlja.snake.dy, 0)

        self.GUI.input()
        self.assertEqual(self.GUI.zemlja.snake.dx, -1)
        self.assertEqual(self.GUI.zemlja.snake.dy, 0)

        # testiranje premika s tipko d - desno
        self.GUI.zemlja.snake.dx = 0
        self.GUI.zemlja.snake.dy = 0
        self.assertEqual(self.GUI.zemlja.snake.dx, 0)
        self.assertEqual(self.GUI.zemlja.snake.dy, 0)

        self.assertEqual(self.GUI.zemlja.snake.dx, 0)
        self.assertEqual(self.GUI.zemlja.snake.dy, 0)
        event.key = pygame.K_d
        pygame.event.get = MagicMock(return_value=[event])
        self.GUI.input()

        self.assertEqual(self.GUI.zemlja.snake.dx, 1)
        self.assertEqual(self.GUI.zemlja.snake.dy, 0)

        # testiranje premika s tipko w - gor
        self.GUI.zemlja.snake.dx = 0
        self.GUI.zemlja.snake.dy = 0
        self.assertEqual(self.GUI.zemlja.snake.dx, 0)
        self.assertEqual(self.GUI.zemlja.snake.dy, 0)

        self.assertEqual(self.GUI.zemlja.snake.dx, 0)
        self.assertEqual(self.GUI.zemlja.snake.dy, 0)
        event.key = pygame.K_w
        pygame.event.get = MagicMock(return_value=[event])
        self.GUI.input()

        self.assertEqual(self.GUI.zemlja.snake.dx, 0)
        self.assertEqual(self.GUI.zemlja.snake.dy, -1)

        # testiranje premika s tipko s - dol
        self.GUI.zemlja.snake.dx = 0
        self.GUI.zemlja.snake.dy = 0
        self.assertEqual(self.GUI.zemlja.snake.dx, 0)
        self.assertEqual(self.GUI.zemlja.snake.dy, 0)

        self.assertEqual(self.GUI.zemlja.snake.dx, 0)
        self.assertEqual(self.GUI.zemlja.snake.dy, 0)
        event.key = pygame.K_s
        pygame.event.get = MagicMock(return_value=[event])
        self.GUI.input()

        self.assertEqual(self.GUI.zemlja.snake.dx, 0)
        self.assertEqual(self.GUI.zemlja.snake.dy, 1)

        # testiranje izhoda ob pritisku tipke q
        with patch('sys.exit') as mock_sys_exit:
            event.key = pygame.K_q
            pygame.event.get = MagicMock(return_value=[event])

            self.GUI.input()

            mock_sys_exit.assert_called_once()



