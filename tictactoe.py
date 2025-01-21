import random

# Function to print the game board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check for a winner
def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

# Function to check if the board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Function for AI's move (Random move for simplicity)
def ai_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

# Main game function
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"  # Player is X, AI is O
    ai = "O"  # AI's symbol
    
    while True:
        print_board(board)
        
        # Player's turn
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        
        if board[row][col] != " ":
            print("Cell already taken! Try again.")
            continue
        
        board[row][col] = player
        
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # AI's turn
        print("AI's turn...")
        ai_row, ai_col = ai_move(board)
        board[ai_row][ai_col] = ai
        
        if check_winner(board):
            print_board(board)
            print(f"Player {ai} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

# Start the game
tic_tac_toe()
