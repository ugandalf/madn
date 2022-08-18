"""
A module implementing a game 'Mensch ärgere Dich nicht' for any number of players > 2.

'Mensch ärgere Dich nicht' is a turn-based board game.
Each player has pieces of the same color and the goal of the game is to move each piece around the board and land it
on a tile with a matching color. In each turn a player rolls a dice. If the player rolls a 6,
he gets to bring a piece on the board. Rolling a 6 also gives him additional turn.
If he rolls a different number, he can move one of his pieces on the board.
If the piece lands on a place already occupied by another, that other piece gets captured and returns off the board.

To play either run the game from your own python script e.g.:

    from madn import Game, Settings
    s = Settings(n_ais = 4, n_humans = 1)
    game = Game(s)
    game.run()

Or use one with default settings:

    $ python main.py
    $ python main_ai_only.py

To exit use Ctrl + C then Enter

Game tested on Windows 10
"""

from .game import Game
from .settings import Settings
from .players import Player, Ai, Human
from .board import Tile, Board
from .pieces import Piece
