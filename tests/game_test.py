import unittest
from madn import Game, Settings

class GameTest(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Settings(drawing=False, n_ais=3, n_humans=0)
        self.g = Game(self.s)

    def test_no_win(self):
        for player in self.g.players:
            self.assertFalse(self.g.won(player))

    def test_turns(self):
        self.assertEqual(self.g.turn, 1)
        self.g.process_turn()
        self.assertEqual(self.g.turn, 2)
        self.g.process_turn()
        self.assertEqual(self.g.turn, 3)


if __name__ == '__main__':
    unittest.main()
