import matplotlib.pyplot as plt

from madn.board import Board
from madn.players import Ai, Human
from madn.settings import Settings


class Game:
    """Class representing 'Mensch ärgere Dich nicht' as a whole

    Attributes:
        board: A Board, responsible for drawing and containing settings and pieces
        cm: A colormap, i.e. a function which given a float between 0 and 1 returns a real color
        turn: An Integer representing how many turns have passed. A turn constitutes of each Player rolling dice
        players: A list of objects of type Player
    """
    def __init__(self, settings=Settings(), ai_cls=Ai, hum_cls=Human, cm=plt.cm.nipy_spectral):
        self.board = Board(settings)
        self.cm = cm
        self.turn = 1
        self.players = []
        for i in range(settings.n_ais):
            self.players.append(ai_cls(i))
        for i in range(settings.n_ais, settings.n_ais + settings.n_humans):
            self.players.append(hum_cls(i))

    def won(self, player) -> bool:
        """Checks whether 'player' won the game"""
        s = self.board.settings
        return all(piece.steps > s.n_players() * s.n_tiles for piece in self.board.pieces if piece.player_id == player.id)

    def process_turn(self):
        """Simulates a single turn of the game.

        The argument is for checking, whether to draw or not.
        Returns a victorious player if there is one or None otherwise
        """
        for i, player in enumerate(self.players):
            if self.board.settings.drawing:
                plt.pause(0.01)
            res = 6
            while res == 6:
                if self.board.settings.drawing:
                    self.board.draw(self.cm)
                res = player.roll_dice()
                if self.board.settings.drawing:
                    plt.title(f"Player {player.id} , Turn {int(self.turn)}, Rolled {res}",
                              c=self.cm(self.board.settings.piece_colors[i]))
                    plt.pause(0.01)
                chosen_piece_index = player.play(res, self.board)
                if chosen_piece_index is not None:
                    piece = self.board.get_piece(player.id, chosen_piece_index)
                    if piece.can_move(res, self.board):
                        piece.move(res, self.board)
                if self.won(player):
                    return player
        self.turn += 1

    def run(self):
        """Main method of the Game. Starts a game and announces a winner at the end of it"""
        input("Press Enter to start")  # Makes the matplotlib window not hide behind terminal
        while True:
            winner = self.process_turn()
            if winner:
                print("This game was won by Player {} on Turn {}".format(winner.id, self.turn))
                break

