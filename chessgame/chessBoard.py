import numpy as np

from chessgame.pieces.pawn import Pawn


class Board:

    def __init__(self):
        pass

    def create_board(self):
        # TODO: create a 8x8 matrix with zeros

        self.game_matrix = np.zeros([8, 8], int)

        pass

    def add_pieces(self):
        pawn = Pawn(True)

        pass