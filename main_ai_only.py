from madn import Game, Settings

s = Settings(n_ais=5, n_humans=0, n_pieces=3, n_tiles=7, tile_shape="p", piece_shape="*")
Game(s).run()