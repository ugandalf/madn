import unittest
from madn import Game, Board, Settings


class BoardTest(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Settings(drawing=False, n_ais=6, n_humans=0, n_pieces=10)
        self.g = Game(self.s)
        self.b = self.g.board

    def test_getting_pieces(self):
        for i in range(6):
            self.assertEqual(self.b.get_piece(player_id=i, piece_id=0).player_id, i)
        for j in range(10):
            self.assertEqual(self.b.get_piece(player_id=0, piece_id=j).piece_id, j)

    def test_invalid_pieces(self):
        with self.assertRaises(IndexError):
            self.b.get_piece(player_id=100, piece_id=0)
        with self.assertRaises(IndexError):
            self.b.get_piece(player_id=0, piece_id=100)


if __name__ == '__main__':
    unittest.main()
