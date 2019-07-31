# =========== Tic Tac Toe Game With Python ==========
# created in july,
# learning open source contribution

# ------------ Global Variables -----------

# Will hold the Game board data
board = [
         "-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"
         ]

# Let us know if the game is still going
game_still_going = True

# Tells us  Who win? Or Tie?
winner = None

# Tell us Who's turn is this (X goes first)
current_player = "X"


# Play a game of Tic Tac Toe
def play_game():

    # Display Initial Board
    display_board()

    # Loop until the game stops (winner or tie)
    while game_still_going:

        # Handle a single turn of arbitrary player
        handle_turn(current_player)

        # Check if game has ended
        check_if_game_over()

        # Flip to other player
        flip_player()

    # Since the game is over, print winner or tie
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner is None:
        print("Tie.")


# Display game board to screen
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# Handle a single turn for an arbitrary player
def handle_turn(player):

    # Get position from player
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:

        # Whatever the user inputs, make sure it is a valid input, the spot is open
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        # Get correct index in your board
        position = int(position) - 1

        # Then also make sure that spot is available on the board
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    # Put the game piece on the board
    board[position] = player

    # Show the game board at current state
    display_board()


# Check if the game is over
def check_if_game_over():
    check_for_winner()
    check_if_tie()


# Check to see if somebody has won
def check_for_winner():
    # set up global variables
    global winner
    # Check if there was a winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# Check the rows for win
def check_rows():
    # set up local variables
    global game_still_going
    #  check if any of the row have all the same values (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    # Or return None if there was no winner
    else:
        return None


# Check the columns for win
def check_columns():
    # set up local variables
    global game_still_going
    # check if any of the column have all the same values (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


# Check the diagonals for win
def check_diagonals():
    # set up local variables
    global game_still_going
    # check if any of the diagonal have all the same values (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # If any diagonal does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


# Check if there was a tie
def check_if_tie():
    # global variable
    global game_still_going
    # If game board is full
    if "-" not in board:
        game_still_going = False
    # Else there is not tie
    else:
        return False


# Flip the player from X to O, or O to X
def flip_player():
    # Global variables we need
    global current_player
    # If current player is X then changed it to O
    if current_player == "X":
        current_player = "O"
    # If current player is O then changed it to X
    elif current_player == "O":
        current_player = "X"
    return


# ----------------- Start Execution -------------------
# Play a game of Tic Tac Toe
play_game()


# ------------------ Game logic as under :-> ----------------
# board
# display  board
# play game
# handle turn :
# -> check win
# -> check rows
# -> check columns
# check display
# check tie
# flip player
