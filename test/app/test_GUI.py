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
