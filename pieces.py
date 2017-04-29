
#------------------------!!------------------classes for all pieces--------------------!!------------------#
ABBRIVIATIONS = {
	'R': 'Rook'
	'N': 'Knight'
	'B': 'Bishop'
	'Q': 'Queen'
	'K': 'King'
	'P': 'Pawn'
}


class Piece(object):
	""" Parent Class for all the chess pieces """
	__slots__ = ('abbriviation', 'color', 'location')

	def __init__(self, color, abbriviation, location):
		if color == 'white':
			self.abbriviation = self.abbriviation.upper()
			self.location = location
		elif color == 'black':
			self.abbriviation = self.abbriviation.lower()
			self.location = location

		try:
			self.color = color
		
		except:
			pass

	def move_is_legal(self, move, board):
		"""
		Test whether a move is legal in the current game state.

		Parameters
		----------
		move : (int, int)
			A corrdinate pair (row, column) indicating the next position for
			the active player on the board.

		Returns
		----------
		bool
			Returns True if the move is lega, False otherwise
		"""
		row, col = move
		return 0 <= row < board.height and \
			   0 <= col < board.width and \
			   board.__board_state__[row][col] == board.BLANK

	# keep a reference to the board
	def get_location(self):
		return self.location

	def get_legal_moves(self):
		"""
		Return the list of all legal moves for
		"""

	def apply_move(self, move, board):
		"""
		Move the active player to a specified location.

		Parameters
		----------
		move : (int, int)
			A coordinate par(row, column) indicating the next position for
			the active player on the board.

		Returns
		----------
		None
		"""
		temp_row, temp_col = self.location
		board.__board_state__[row][col] = self.abbriviation
		self.location = move
		board.__board_state__[temp_row][temp_col] = board.BLANK
		

class King(piece):

	def get_legal_moves(self):
		"""
		Return the list of all legal moves for
		"""

class Queen(piece):

	def get_legal_moves(self):
		"""
		Return the list of all legal moves for
		"""

class Rook(piece):

	def get_legal_moves(self):
		"""
		Return the list of all legal moves for
		"""

class Bishop(piece):
	abbriviation = 'b'
	def get_legal_moves(self, board):
		"""
		Return the list of all legal moves for
		"""

class Knight(piece):
	abbriviation = 'n'

	def get_legal_moves(self, board):
		"""
		Return the list of all legal moves for
		"""
		position = self.position
		color = self.color
		possible_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

		for x, y in possible_moves:
			destination = (position[0] + x, position[1] + y)
			if destination not in board.occupied(color):
				legal_moves.append(destination)

		return legal_moves

class Pawn(piece):
	abbriviation = 'p'
	def get_legal_moves(self, board):
		"""
		Return the list of all legal moves for
		"""
		position = self.position
		if self.color == 'white':
			home_row, direction, enemy = 1, 1, 'black'
		else:
			home_row, direction, enemy = 6, -1, 'white'

		legal_moves = []

		# Moving
		forward = (position[0] + direction, position[1])
		if forward in board.get_blank_space() and self.move_is_legal(forward, board):
			legal_moves.append(forward)
			if position[0] == homerow:
				# Allow to forward 2 steps if at starting position
				double_forward = (forward[0] + direction, forward[1])
				if double_forward in board.get_blank_space() and self.move_is_legal(forward, board):
					legal_moves.append(double_forward)

		# Attack
		for i in (-1, 1):
			attack = (position[0] + direction, position[1] + i)
			if attack not in board.get_blank_space() and self.move_is_legal(attach, board) and board.occupied(enemy):
				legal_moves.append(attach)

		# TODO: En passant
		return legal_moves





