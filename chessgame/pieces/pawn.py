from chessgame.piece import Piece


class Pawn(Piece):

	def __init__(self, color: bool):
		super().__init__(color)

	def available_moves(self):
		"""

		:return moves: list:
		"""

		moves = []

		# TODO: create the rules for the pawn to move
		# TODO: create the rules for the pawn to attack

		return moves
