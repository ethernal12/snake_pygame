import sys
from dataclasses import dataclass

import pygame
import time
from src.app._app import App
from src.domain.zemlja import Zemlja
from src.app.GUItext import messages


@dataclass
class GUI(App):
    width: int
    height: int
    zemlja = None
    tocke: int = 0
    dx: int = 0
    dy: int = 0

    def __post_init__(self):
        pygame.init()
        self.windowSurface = pygame.display.set_mode((self.width, self.height), 0, 32)

    def draw_game(self):
        pygame.display.set_caption("Snake Game")
        # zapolni display z barvo, bela
        self.windowSurface.fill((255, 255, 100))
        self.dx = self.width / 20
        self.dy = self.height / 20
        # nariši kačo
        pygame.draw.rect(self.windowSurface, (0, 0, 0), (
            self.zemlja.snake.x * self.dx, self.zemlja.snake.y * self.dy,
            (20),
            (20)))
        # nariši hrano
        pygame.draw.rect(self.windowSurface, (0, 255, 0), (
            self.zemlja.hrana.x * self.dx, self.zemlja.hrana.y * self.dy,
            (20),
            (20)))
        # nariši del_kače
        for i, d in enumerate(self.zemlja.snake.deli):
            pygame.draw.rect(self.windowSurface, (0, 0, 0), (
                d.x * self.dx, d.y * self.dy,
                (20),
                (20)))

    def end_game_conditions(self):

        messages(self.windowSurface, self.tocke, 'Points: ', 0, 0)
        for i, d in enumerate(self.zemlja.snake.deli):
            # če se glava kače dotakne sama sebe
            if d.x == self.zemlja.snake.x and d.y == self.zemlja.snake.y:
                sys.exit()

    def poberi_hrano(self):
        # če kača pobere hrano
        int = self.zemlja.dodaj_del_kace_in_nastavi_hrano()
        self.tocke += int

    def new_game(self):
        self.zemlja = Zemlja(
            sirina=20,
            visina=20
        )

    def input(self):
        self.zemlja.snake.premikanje()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    self.zemlja.snake.smer_premika(0, 1)
                elif event.key == pygame.K_a:
                    self.zemlja.snake.smer_premika(-1, 0)
                elif event.key == pygame.K_d:
                    self.zemlja.snake.smer_premika(1, 0)
                elif event.key == pygame.K_w:
                    self.zemlja.snake.smer_premika(0, -1)
                elif event.key == pygame.K_s:
                    self.zemlja.snake.smer_premika(0, 1)
                elif event.key == pygame.q_q:
                    sys.exit()
