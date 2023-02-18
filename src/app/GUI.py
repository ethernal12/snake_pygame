import sys
from dataclasses import dataclass

import pygame
from src.app._app import App
from src.domain.zemlja import Zemlja
from typing import Optional


@dataclass
class GUI(App):
    width: int
    height: int
    zemlja = None
    tocke: int = 0
    dx: int = 0
    dy: int = 0
    windowSurface: Optional[pygame.Surface] = None

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
        pygame.draw.rect(surface=self.windowSurface, color=(0, 0, 0), rect=(
            self.zemlja.snake.x * self.dx, self.zemlja.snake.y * self.dy,
            (20),
            (20)))
        # nariši hrano
        pygame.draw.rect(surface=self.windowSurface, color=(0, 255, 0), rect=(
            self.zemlja.hrana.x * self.dx, self.zemlja.hrana.y * self.dy,
            (20),
            (20)))
        # nariši del_kače
        for i, d in enumerate(self.zemlja.snake.deli):
            pygame.draw.rect(surface=self.windowSurface, color=(0, 0, 0), rect=(
                d.x * self.dx, d.y * self.dy,
                (20),
                (20)))

    def new_game(self):
        self.zemlja = Zemlja(
            sirina=20,
            visina=20
        )

    def input(self):
        self.messages(self.zemlja.tocke, 'Points:', 0, 0)
        self.zemlja.snake.premikanje()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.zemlja.snake.smer_premika(-1, 0)
                elif event.key == pygame.K_d:
                    self.zemlja.snake.smer_premika(1, 0)
                elif event.key == pygame.K_w:
                    self.zemlja.snake.smer_premika(0, -1)
                elif event.key == pygame.K_s:
                    self.zemlja.snake.smer_premika(0, 1)
                elif event.key == pygame.K_q:
                    sys.exit()

    def messages(self, text, title, poistionX, positionY):
        # Nastavi font
        font = pygame.font.Font('freesansbold.ttf', 30)
        # Ustvari text podlago
        text_podlaga = font.render(f'{title} {str(text)}', True, (0, 0, 0))
        # Nariši text na canvas
        self.windowSurface.blit(text_podlaga, (poistionX, positionY))
        pygame.display.update()
