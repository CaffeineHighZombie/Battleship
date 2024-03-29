from random import randint

board = []	# empty board list
board_size = 5	# battleship board is created as 5x5 matrix, change this for different board size

for x in range(board_size):	
    board.append(["O"] * board_size)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# debug code
# print ship_row
# print ship_col

for turn in range(0,4):	# change this for number turns user can take to guess. Intiallized to 4.
    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        print (turn + 1)
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        
        if turn == 3:
            print "Game Over"
        
        print (turn + 1)
        print_board(board)
