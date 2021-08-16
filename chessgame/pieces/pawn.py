from chessgame.piece import Piece


class Pawn(Piece):

	def __init__(self, color: bool):
		super().__init__(color)
