from chessgame.piece import Piece


class Queen(Piece):

	def __init__(self, color: bool):
		super().__init__(color)

	def available_moves(self):
		"""

		:return moves: list:
		"""

		moves = []

		# TODO: create the rules for the queen to move
		# TODO: create the rules for the queen to attack

		return moves
