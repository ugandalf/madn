import unittest
from madn import Player, Ai


class PlayerTest(unittest.TestCase):
    def test_cant_Player(self):
        with self.assertRaises(TypeError):
            self.assertRaises(Player(0))  # because abstract class

    def test_roll(self):
        p = Ai(0)
        for _ in range(100):
            self.assertIn(p.roll_dice(), range(1, 7))


if __name__ == '__main__':
    unittest.main()
