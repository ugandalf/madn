# Possible improvement: Settings as a Singleton class

class Settings:
    """ A class used for storing initial settings for the game

    Attributes:
        drawing: A boolean, whether to draw the board or not
        n_humans: An integer count of human players
        n_ais: An integer count of computer players
        n_pieces: An integer count of pieces per player
        n_tiles: An integer count of tiles between the starting places of the players
        tile_shape: A string representing a shape of each tile drawn on the board. By default, it's a square
        piece_shape: A string representing a shape of each piece drawn on the board. By default it's a circle
        piece_colors: A list of floats between 0 and 1 representing each player's color.
    """
    def __init__(self, drawing=True, n_humans=1, n_ais=3, n_pieces=4,
                 n_tiles=10, tile_shape="s", piece_shape="o",
                 piece_colors=None):
        self.drawing = drawing
        self.n_humans = n_humans
        self.n_ais = n_ais
        self.n_pieces = n_pieces
        self.n_tiles = n_tiles
        self.tile_shape = tile_shape
        self.piece_shape = piece_shape
        self.piece_colors = piece_colors

        if not piece_colors:
            self.piece_colors = [i / (n_humans + n_ais) for i in range(n_humans + n_ais)]
        elif len(piece_colors) != n_humans + n_ais:
            raise ValueError("Wrong amount of colours for a given amount of players")

        if n_humans + n_ais <= 2:
            raise ValueError("Not enough players (Minimum number is 3)")
        if n_tiles < 1:
            raise ValueError("Not enough tiles")
        if n_pieces < 1:
            raise ValueError("Not enough pieces per player")

    def n_players(self) -> int:
        """ A helper function. Returns a number of players in total"""
        return self.n_ais + self.n_humans

