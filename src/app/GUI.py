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
    clock = pygame.time.Clock()
    # Nastavi font
    font = None
    velikost_kvadrata = 20

    def __post_init__(self):
        pygame.init()
        self.windowSurface = pygame.display.set_mode((self.width, self.height), 0, 32)
        self.font = pygame.font.Font('freesansbold.ttf', 30)

    def draw(self):
        pygame.display.set_caption("Snake Game")
        # zapolni display z barvo, bela
        self.windowSurface.fill((255, 255, 100))
        self._messages(self.zemlja.tocke, 'Points:', 0, 0)
        self.dx = self.width // self.velikost_kvadrata
        self.dy = self.height // self.velikost_kvadrata
        # nariši kačo
        pygame.draw.rect(surface=self.windowSurface, color=(0, 0, 0), rect=(
            self.zemlja.snake.x * self.dx, self.zemlja.snake.y * self.dy,
            self.velikost_kvadrata,
            self.velikost_kvadrata))
        # nariši hrano
        pygame.draw.rect(surface=self.windowSurface, color=(0, 255, 0), rect=(
            self.zemlja.hrana.x * self.dx, self.zemlja.hrana.y * self.dy,
            self.velikost_kvadrata,
            self.velikost_kvadrata))
        # nariši del_kače
        for i, d in enumerate(self.zemlja.snake.deli):
            pygame.draw.rect(surface=self.windowSurface, color=(0, 0, 0), rect=(
                d.x * self.dx, d.y * self.dy,
                self.velikost_kvadrata,
                self.velikost_kvadrata))
        pygame.display.update()

    # TODO: POGRUNTAJ IZRAČUN ZA ŠI. IN VI.
    def init(self):
        self.zemlja = Zemlja(
            sirina=20,
            visina=20
        )

    def konec(self):
        return self.zemlja.konec()

    def input(self):
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
        self.zemlja.premakni()
        self.clock.tick(7)

    def _messages(self, text, title, poistionX, positionY):
        # Ustvari text podlago
        text_podlaga = self.font.render(f'{title} {str(text)}', True, (0, 0, 0))
        # Nariši text na canvas
        self.windowSurface.blit(text_podlaga, (poistionX, positionY))
