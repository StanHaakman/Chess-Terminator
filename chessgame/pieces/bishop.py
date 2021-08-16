from chessgame.piece import Piece


class Bishop(Piece):

    def __init__(self, color: bool):
        super().__init__(color)

    def available_moves(self):
        """

        :return moves: list:
        """

        moves = []

        # TODO: create the rules for the bishop to move
        # TODO: create the rules for the bishop to attack

        return moves
