from chessgame.piece import Piece


class King(Piece):

    def __init__(self, color: bool):
        super().__init__(color)

    def available_moves(self):
        """

        :return moves: list:
        """

        moves = []

        # TODO: create the rules for the king to move
        # TODO: create the rules for the king to attack

        return moves

