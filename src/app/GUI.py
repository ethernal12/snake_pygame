import sys
from dataclasses import dataclass

import pygame

from src.app._app import App
from src.domain.del_kace import DelKace
from src.domain.hrana import Hrana
from src.domain.snake import Snake
from src.domain.zemlja import Zemlja


@dataclass
class GUI(App):
    width: int
    height: int
    zemlja = None

    def __post_init__(self):
        pygame.init()
        self.windowSurface = pygame.display.set_mode((self.width, self.height), 0, 32)

    def draw_game(self):

        pygame.display.set_caption("Snake Game")
        # zapolni display z barvo, bela
        self.windowSurface.fill((255, 255, 255))
        dx = self.width / 10
        dy = self.height / 10
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
            print(d.x, 'del_kače x', i)
            print(d.y, 'del_kače y', i)
            pygame.draw.rect(self.windowSurface, (0, 0, 0), (
                d.x * dx, d.y * dy,
                (20),
                (20)))

    def end_game_conditions(self):
        dx = self.width / 10
        dy = self.height / 10

        self.del_kace = DelKace(dx, dy)
        if self.zemlja.snake.x == self.zemlja.hrana.x and self.zemlja.snake.y == self.zemlja.hrana.y:
            # nariši del kače
            self.zemlja.snake.dodaj_del_kace()
            self.zemlja.nastavi_hrano()

    def new_game(self):
        self.zemlja = Zemlja(
            sirina=10,
            visina=10
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


if __name__ == '__main__':
    app = GUI(600, 600)
    running = True
    app.new_game()
    # Create a clock object
    clock = pygame.time.Clock()
    while running:
        app.draw_game()
        app.input()
        pygame.display.update()
        app.end_game_conditions()
        clock.tick(2)
