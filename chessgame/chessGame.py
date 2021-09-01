import numpy as np

class Game:

    def __init__(self):
        self.board = np.zeros((8,8))

    def swap(self, loc_a, loc_b):
        if self.board[loc_b[0]][loc_b[1]] != 0:
            return -1
        self.board[loc_a[0]][loc_a[1]], self.board[loc_b[0]][loc_b[1]] = self.board[loc_b[0]][loc_b[1]], self.board[loc_a[0]][loc_a[1]]

    def destroy(self, loc_a, loc_b):
        if self.board[loc_a[0]][loc_a[1]] == 0 or self.board[loc_b[0]][loc_b[1]] == 0:
            return -1
        self.board[loc_a[0]][loc_a[1]], self.board[loc_b[0]][loc_b[1]] = 0, self.board[loc_a[0]][loc_a[1]]

    def set_piece(self, piece, location):
        # TODO: Place the piece on the location in the matrix
        return -1
