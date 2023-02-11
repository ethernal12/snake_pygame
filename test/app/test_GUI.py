import unittest
from src.app.GUI import GUI


class Test_GUI(unittest.TestCase):
    def setUp(self) -> None:
        self.width = 400
        self.height = 400
        self.GUI = GUI(self.width, self.height)

    def test_init(self):
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

