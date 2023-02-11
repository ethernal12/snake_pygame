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

    def test_funkcije_draw_game(self):
        self.GUI.new_game()
        self.GUI.draw_game()
        self.assertEqual(self.GUI.dx, self.GUI.width / self.GUI.dx)
        self.assertEqual(self.GUI.dy, self.GUI.height / self.GUI.dx)

    def test_funkionalnosti_inputov(self):
        # kličemo funkcijo da se ustvari objekt zemlja in tako snake objekt
        self.GUI.new_game()
        # zmokamo funkcije
        self.GUI.zemlja.snake.smer_premika = MagicMock()
        self.GUI.zemlja.snake.premikanje = MagicMock()

        # zmokamo event
        event = MagicMock()
        event.type = pygame.KEYDOWN
        event.key = pygame.K_e
        # pokličemo funkcijo input()

        self.GUI.input(event)

        self.zemlja.snake.premikanje.assert_called_once()
        self.zemlja.snake.smer_premika.assert_called_once()
