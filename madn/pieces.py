class Piece:
    """ Class for pieces moving around the board.

    Attributes:
        color: A float between 0 and 1 representing color
        player_id: An integer representing which player it belongs to
        piece_id: An integer representing which piece of the player it is
        steps: An integer representing how many steps a piece has taken. Gets reset to 0 after capture.
    """
    def __init__(self, player_id, piece_id, color):
        self.color = color
        self.player_id = player_id
        self.piece_id = piece_id
        self.steps = 0

    def __repr__(self):
        return str(self.piece_id)

    def get_position(self, board) -> complex:
        """Returns a position, where a given piece should be drawn"""
        s = board.settings
        index = ((self.player_id + 1) * s.n_tiles + self.steps - 1) % (s.n_players() * s.n_tiles)
        if self.steps == 0:
            return board.tiles[index].pos * (1.25 + self.piece_id / (2*s.n_tiles))
        if 0 < self.steps <= s.n_tiles * s.n_players():
            return board.tiles[index].pos
        else:
            index = self.player_id * s.n_pieces + self.steps - 1
            return board.tiles[index].pos

    def can_move(self, steps, board) -> bool:
        """Returns a Boolean saying whether or not this piece is allowed to move 'steps' tiles forward"""
        s = board.settings
        if self.steps == 0 and steps < 6:  # Can only start given a six
            return False
        if self.steps + steps > s.n_tiles * s.n_players() + s.n_pieces:  # Can't go out of bounds
            return False
        for piece in board.pieces:  # Can't capture own pieces
            if piece.player_id == self.player_id:
                if self.steps + steps == piece.steps and self.steps != 0:
                    return False
                if self.steps + 1 == piece.steps and self.steps == 0:
                    return False
        return True

    def move(self, steps, board):
        """Moves a piece 'steps' places and handles capturing other pieces"""
        if self.steps == 0 and steps == 6:
            self.steps = 1
        else:
            self.steps += steps
        for piece in board.pieces:
            if self.get_position(board) == piece.get_position(board) and self.player_id != piece.player_id:
                piece.steps = 0
