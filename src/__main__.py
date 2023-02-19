import sys
import os

# adding directory to python path!
sys.path.append(os.getcwd())
import pygame

from app.GUI import GUI

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
app.init()

while not app.konec():
    app.draw()
    app.input()


