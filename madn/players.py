import abc
from random import randint, sample

from madn.board import Board

class Player(abc.ABC):
    """
    A mix-in class representing a Player.
    Subclasses must override a method named 'play'.

    Attributes:
        id: An Integer identifying a player; used in some calculations, should be number of players created.
            id assignment isn't handled in class, because it caused problems in unittests.
    """
    def __init__(self, id):
        self.id = id

    def roll_dice(self) -> int:
        """ Used for getting a result of a dice roll. Could potentially be overriden for cheating"""
        res = randint(1, 6)
        print(f"Player {self.id} rolled {res}")
        return res

    def can_move(self, steps, board: Board):
        """ Return a list of pieces which can move by a given number steps (when the current player is playing)"""
        res = []
        for piece in board.pieces:
            if piece.player_id == self.id:
                if piece.can_move(steps, board):
                    res.append(piece)
        return res

    @abc.abstractmethod
    def play(self, steps, board: Board):
        """ Abstract method determining a strategy of which piece to move. Must return a list of piece_ids"""
        pass


class Ai(Player):
    """ A sample implementation of an AI-Player. Makes a random legal move"""
    def play(self, steps, board):
        print(f"Player {self.id} to move")
        available = self.can_move(steps, board)
        if len(available) > 0:
            return sample(available, 1)[0].piece_id

class Human(Player):
    """ A sample implementation of a Human-Player. Takes input from terminal"""
    def play(self, steps, board):
        print(f"Player {self.id} to move")
        available = self.can_move(steps, board)
        if len(available) == 0:
            print("No pieces available - skip")
        if len(available) == 1:
            input(f"Press Enter to move your only available piece ({available[0]})")
            return available[0].piece_id
        if len(available) > 0:
            res = None
            while not isinstance(res, int):
                print(f"(Pieces available: {available})")
                try:
                    res = int(input("Move piece number: "))
                except ValueError:
                    continue
            return res
