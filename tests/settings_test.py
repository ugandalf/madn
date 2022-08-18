import unittest
from madn import Settings
from random import randint

class SettingsTest(unittest.TestCase):
    def test_default(self):
        Settings()

    def test_invalid_players(self):
        with self.assertRaises(ValueError):
            Settings(n_humans=0, n_ais=0)
        with self.assertRaises(ValueError):
            Settings(n_humans=1, n_ais=0)
        with self.assertRaises(ValueError):
            Settings(n_humans=0, n_ais=1)

    def test_invalid_tiles(self):
        with self.assertRaises(ValueError):
            Settings(n_tiles=0)

    def test_invalid_pieces(self):
        with self.assertRaises(ValueError):
            Settings(n_pieces=0)
        with self.assertRaises(ValueError):
            Settings(n_pieces=-1)

    def test_colors(self):
        with self.assertRaises(ValueError):
            Settings(n_ais=2, n_humans=1, piece_colors=["r", "g"])  # not enough colors

        with self.assertRaises(ValueError):
            Settings(n_ais=2, n_humans=1, piece_colors=["r", "g", "r", "g"])  # too many colors

    def test_helper(self):
        for _ in range(100):
            n1 = randint(2, 20)
            n2 = randint(1, 7)
            s = Settings(n_humans=n1, n_ais=n2)
            self.assertEqual(s.n_humans + s.n_ais, s.n_players())


if __name__ == '__main__':
    unittest.main()
