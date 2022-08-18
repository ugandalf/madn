import matplotlib.pyplot as plt
import numpy as np

from madn.pieces import Piece


class Tile:
    """ Class representing a space that can be occupied by a piece

    Attributes:
        pos: A complex number representing coordinates. Used for drawing.
        color: A float between 0 and 1 representing color
    """
    def __init__(self, pos: complex, color: float = 1.0):
        self.pos = pos
        self.color = color

class Board:
    """ Class representing a board.

    Attributes:
        settings: An instance of Settings. Contains general information about the game like number of players
        pieces: A list of objects of type Piece.
        tiles: A list of objects of type Tile.
    """
    def __init__(self, settings):
        self.settings = settings
        self.pieces = []
        self.tiles = []
        # Points on the unit circle for each player
        points = np.exp(np.arange(1, settings.n_players() + 2) * np.pi * 2j / settings.n_players())
        # Piece generation
        for i in range(settings.n_players()):
            for j in range(settings.n_pieces):
                self.pieces.append(Piece(player_id=i, piece_id=j,
                                         color=settings.piece_colors[i]))
        # Outer tiles - spaces commonly available
        for i in range(settings.n_players()):
            outer = np.linspace(points[i], points[i + 1], settings.n_tiles + 1)[1:]
            for j in outer:
                self.tiles.append(Tile(j))
        # Inner tiles - finish line
        for i in range(settings.n_players()):
            inner = np.linspace(0.8*points[i+1], 0.4*points[i+1], settings.n_pieces)
            for j in inner:
                self.tiles.append(Tile(j, settings.piece_colors[i]))
        # And lastly we set matplotlib in interactive mode, so we won't have to close the window between moves
        if settings.drawing:
            plt.ion()

    def get_piece(self, player_id, piece_id) -> Piece:
        """ Returns a piece with given parameters. See: madn.piece.Piece """
        return self.pieces[self.settings.n_pieces * player_id + piece_id]

    def draw(self, cmap=plt.cm.nipy_spectral):
        """ Draws the whole board. Optionally can get a different colormap, but the default one is nice enough """
        plt.gca().cla()
        plt.grid()
        plt.gca().set_axis_off()
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)
        self.draw_tiles(cmap)
        self.draw_pieces(cmap)

    def draw_tiles(self, cmap=plt.cm.nipy_spectral):
        """ Draws tiles on the screen"""
        colors = np.array([tile.color for tile in self.tiles])
        plt.scatter([tile.pos.real for tile in self.tiles],
                    [tile.pos.imag for tile in self.tiles],
                    marker=self.settings.tile_shape,
                    s=100,
                    facecolors='none',
                    edgecolors=cmap(colors))

    def draw_pieces(self, cmap=plt.cm.nipy_spectral):
        """ Draws pieces on the screen"""
        positions = [piece.get_position(self) for piece in self.pieces]
        xs = [pos.real for pos in positions]
        ys = [pos.imag for pos in positions]
        plt.scatter(xs, ys,
                    marker=self.settings.piece_shape,
                    s=50,
                    c=[cmap(piece.color) for piece in self.pieces])
        for i in range(len(self.pieces)):
            plt.annotate(self.pieces[i].piece_id, (xs[i], ys[i]), alpha=0.7)

