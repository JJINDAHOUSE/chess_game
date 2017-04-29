'''
This file contains the `Board` class, which implements the rules for the 
chess game.
'''

from copy import deepcopy
from copy import copy

class Board(object):
	"""
	Implement a model for the chess game

	"""
	BLANK = 0
	NOT_MOVED = None

	def __init__(self, player_1, player_2, width=8, height=8):
		self.width = width
		self.height = height
		self.move_count = 0
		self.__player_1__ = player_1
		self.__player_2__ = player_2
		self.__active_player__ = player_1
		self.__inactive_player__ = player_2
		self.__board_state__ = [[Board.BLANK for i in range(width)] for j in range(height)]
		self.__last_player_move__ = {palyer_1: Board.NOT_MOVED, player_2: Board.NOT_MOVED}
		self.__player_symbols__ = {Board.BLANK: Board.BLANK, player_1: 1, player_2: 2}

	@property
	def active_player(self):
		"""
		The object registered as the player holding initiative in the 
		current game state.
		"""
		return self.__active_player__

	@property
	def inactive_player(self):
		"""
		The object registered as the player in waiting for the current
		game state.
		"""
		return self.__inactive_player__

	def get_opponent(self, player):
		"""
		Return the opponent of the supplied player.


		Parameters
		-----------
		player: object
			An object registered as a player in the current game. Raises an
			error if the supplied object is not registered as a player in
			this game.

		Returns
		-----------
		object
			The opponent of the input player object.
		"""
		if player == self.__active_player__:
			return self.__inactive_player__
		elif player ==self.__inactive_player__:
			return self.__active_player__
		raise RuntimeError("`player` must be an object registered as a player in the current game.")

	def copy(self):
		""" Return a deep copy of the current board. """
		new_board = Board(self.__player_1__, self.__player_2__, width=self.width, height=self.height)
		new_board.move_count = self.move_count
		new_board.__active_player__ = self.__active_player__
		new_board.inactive_player = self.__inactive_player__
		new_board.last_player_move = copy(self.__last_player_move__)
		new_board.__player_symbols__ = copy(self.__player_symbols__)
		new_board.__board_state__ = deepcopy(self.__board_state__)
		return new_board

	def get_blank_spaces(self):
		"""
		Return a list of the locations that are still available on the board.
		"""
		return [(i, j) for j in range(self.width) for i in range(self.height)
			if self.__board_state__[i][j] == Board.BLANK]

	def apply_move(self, move):
		"""
		Move the active player to a specified location.

		Parameters
		----------
		move : (int, int)
			A coordinate pair (row, column) indicating the next position for 
			the active player on the board.

		Returns
		----------
		None
		"""
		row, col = move
		self.__last_player_move__[self.active_player] = move
		self.__board_state__[row][col] = self.__player_symbols__[self.active_player]
		self.__active_player__, self.__inactive_player__ = self.__inactive_player__, self.__active_player__
		self.move_count += 1

	def is_winner(self, player):
		""" Test whether the specified player has won the game. """

	def is_loser(self, player):
		""" Test whether the specified player has lost the game. """


