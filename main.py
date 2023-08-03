# Tic Tac Toe

# Create the game board as a 3x3 list of lists
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

# Function to print the game board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to handle player moves
def make_move(board, player):
    while True:
        row = int(input('Enter the row (0-2): '))
        col = int(input('Enter the column (0-2): '))
        if row < 0 or row > 2 or col < 0 or col > 2:
            print('Invalid move. Try again.')
        elif board[row][col] != '':
            print('That square is already occupied. Try again.')
        else:
            board[row][col] = player
            break

# Function to check for a win
def check_win(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if [board[0][col], board[1][col], board[2][col]].count(player) == 3:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check for a tie
def check_tie(board):
    for row in board:
        if '' in row:
            return False
    return True

# Main game loop
current_player = 'X'
while True:
    print_board(board)
    print(f"Player {current_player}'s turn:")
    make_move(board, current_player)

    if check_win(board, current_player):
        print_board(board)
        print(f"Player {current_player} wins!")
        break
    elif check_tie(board):
        print_board(board)
        print("It's a tie!")
        break

    # Switch to the other player
    current_player = 'O' if current_player == 'X' else 'X'