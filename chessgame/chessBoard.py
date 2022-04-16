import numpy as np

from chessgame.pieces.pawn import Pawn
from chessgame.pieces.rook import Rook
from chessgame.pieces.knight import Knight
from chessgame.pieces.bishop import Bishop
from chessgame.pieces.queen import Queen
from chessgame.pieces.king import King


class Board:

    def __init__(self):
        pass

    def create_board(self):
        self.game_matrix = np.zeros([8, 8], object)

    def add_pieces(self):
        first_row_black  = [Rook(False), Knight(False), Bishop(False), Queen(False), King(False), Bishop(False), Knight(False), Rook(False)]
        second_row_black = [Pawn(False) for _ in range(8)]
        
        second_row_white = [Pawn(True) for _ in range(8)]
        first_row_white  = [Rook(True), Knight(True), Bishop(True), Queen(True), King(True), Bishop(True), Knight(True), Rook(True)]

        
        self.game_matrix[0] = first_row_black
        self.game_matrix[1] = second_row_black
        self.game_matrix[6] = second_row_white
        self.game_matrix[7] = first_row_white
