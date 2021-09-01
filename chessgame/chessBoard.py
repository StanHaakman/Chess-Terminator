import numpy as np

from chessgame.pieces.pawn import Pawn


class Board:

    def __init__(self):
        pass

    def create_board(self):
        # TODO: create a 8x8 matrix with zeros

        self.game_matrix = np.zeros([8, 8], object)

        pass

    def add_pieces(self):
        pawn = Pawn(True)

        for x in range(0, 2):
            for i in range(0, 8):
                self.game_matrix[1 if x == 0 else 6][i] = Pawn(False if x == 0 else True)

        pass
