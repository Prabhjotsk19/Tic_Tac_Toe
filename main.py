# ------ GLOBAL VARIABLE -------


# game board
board = ["-", "-", "-",
		 "-", "-", "-",
		 "-", "-", "-"]


# if game still going
game_still_going = True


# to display board
def display_board():
	print(board[0] + "|" + board[1] + "|" + board[2])
	print(board[3] + "|" + board[4] + "|" + board[5])
	print (board[6] + "|" + board[7] + "|" + board[8])


def play_game():

	# Display Initial Board
	display_board()

	while game_still_going:

		handle_turn()

		check_if_game_over()

		flip_player()


def handle_turn():
	position = input("Choose a position from 1-9: ")
	position = int(position) - 1

	board[position] ="X"
	display_board()


def check_if_game_over():
	check_if_win()
	check_if_tie()


def check_if_win():
	# check rows
	# check columns
	# check diagonals
	return 


def check_if_tie():
	return


def flip_player():
	return

	


play_game()







# board 
# display  board
# play game
# handle turn 
# check win
	# check rows
	# check columns
	# check display
# check tie
# flip player
#