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
    current_time: int = None

    def __post_init__(self):
        pygame.init()
        self.windowSurface = pygame.display.set_mode((self.width, self.height), 0, 32)

    def draw_game(self):
        pygame.display.set_caption("Snake Game")
        self.current_time = time.strftime("%S")
        # zapolni display z barvo, bela
        self.windowSurface.fill((255, 255, 100))
        dx = self.width / 20
        dy = self.height / 20
        # nariši kačo
        pygame.draw.rect(self.windowSurface, (0, 0, 0), (
            self.zemlja.snake.x * dx, self.zemlja.snake.y * dy,
            (20),
            (20)))
        # nariši hrano
        pygame.draw.rect(self.windowSurface, (0, 255, 0), (
            self.zemlja.hrana.x * dx, self.zemlja.hrana.y * dy,
            (20),
            (20)))
        # nariši del_kače
        for i, d in enumerate(self.zemlja.snake.deli):
            pygame.draw.rect(self.windowSurface, (0, 0, 0), (
                d.x * dx, d.y * dy,
                (20),
                (20)))

    def end_game_conditions(self):

        #messages(self.windowSurface, self.current_time, 'Time: ', 200, 0)
        messages(self.windowSurface, self.tocke, 'Points: ', 0, 0)
        for i, d in enumerate(self.zemlja.snake.deli):
            # če se glava kače dotakne sama sebe
            if d.x == self.zemlja.snake.x and d.y == self.zemlja.snake.y:
                sys.exit()
        # če kača pobere hrano
        if self.zemlja.snake.x == self.zemlja.hrana.x and self.zemlja.snake.y == self.zemlja.hrana.y:
            self.tocke += 1
            self.zemlja.snake.dodaj_del_kace()
            self.zemlja.nastavi_hrano()

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
