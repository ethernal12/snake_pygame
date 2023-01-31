import sys
from dataclasses import dataclass

import pygame

from src.app._app import App
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

        # zapolni display z barvo, bela
        self.windowSurface.fill((255, 255, 255))
        dx = self.width / 10
        dy = self.height / 10
        # nariši kačo
        pygame.draw.rect(self.windowSurface, (0, 0, 0), (
            self.zemlja.snake.x * dx, self.zemlja.snake.y * dy,
            (20),
            (20)))

    def end_game_conditions(self):
        pass

    def new_game(self):
        self.zemlja = Zemlja(
            sirina=10,
            visina=10
        )

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pygame.display.update()
                    self.zemlja.snake.premik(-1, 0)
                elif event.key == pygame.K_d:
                    self.zemlja.snake.premik(1, 0)
                elif event.key == pygame.K_w:
                    self.zemlja.snake.premik(0, -1)
                elif event.key == pygame.K_s:
                    self.zemlja.snake.premik(0, 1)
                elif event.key == pygame.q_q:
                    sys.exit()



if __name__ == '__main__':
    app = GUI(400, 400)
    running = True
    app.new_game()
    while running:
        app.draw_game()
        app.input()
        pygame.display.update()
