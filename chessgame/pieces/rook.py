from chessgame.piece import Piece


class Rook(Piece):

	def __init__(self, color: bool):
		super().__init__(color)

	def available_moves(self):
		"""

		:return moves: list:
		"""

		moves = []

		# TODO: create the rules for the rook to move
		# TODO: create the rules for the rook to attack

		return moves
