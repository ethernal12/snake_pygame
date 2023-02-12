import unittest
from src.domain.del_kace import DelKace


class Test_del_kace(unittest.TestCase):
    def setUp(self) -> None:
        self.x = 5
        self.y = 3
        self.del_kace = DelKace(self.x, self.y)

    def test___init__(self):
        self.assertEqual(self.del_kace.y, 3)
        self.assertEqual(self.del_kace.x, 5)
        self.assertTrue(isinstance(self.del_kace, DelKace))
