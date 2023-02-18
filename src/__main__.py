import logging
import sys

import pygame

from src.app.GUI import GUI


# from autologging import TRACE

# logging.basicConfig(level=TRACE, stream=sys.stdout,
#                     format="%(asctime)s.%(msecs)04d ┃ %(filename)+20s ┃ %(funcName)-30s ┃ %(levelname)+8s ┃ %(message)s")
#
# log = logging.getLogger(__name__)
# log.debug("To je debug %s", '123')
# log.info("To je info %s", '123')
# log.warning("To je warning %s", '123')
# log.error("To je debugwa%s", '123')

app = GUI(600, 600)
app.new_game()
running = True
clock = pygame.time.Clock()
while running:
    app.draw_game()
    app.input()
    pygame.display.update()
    app.zemlja.dodaj_del_kace_in_nastavi_hrano()
    clock.tick(5)
    if not app.zemlja.konec():
        running = False
