def print_board(board):
    """Function to print the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, mark):
    """Function to check if a player has won."""
    # Check rows, columns, andhhjjk diagonals for a win
    for row in board:
        if row.count(mark) == 3:
            return True
    for col in range(3):
        if board[0][col] == mark and board[1][col] == mark and board[2][col] == mark:
            return True
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    return False

def check_draw(board):
    """Function to check if the game is a draw."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize a 3x3 board
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    
    while True:
        print_board(board)
        
        # Get player input
        try:
            row = int(input(f"Player {current_player}, enter the row (1-3): ")) - 1
            col = int(input(f"Player {current_player}, enter the column (1-3): ")) - 1
        except ValueError:
            print("Invalid input. Please enter numbers between 1 and 3.")
            continue

        # Check if the input is valid
        if row not in range(3) or col not in range(3):
            print("Invalid move. Please enter numbers between 1 and 3.")
            continue
        if board[row][col] != " ":
            print("That spot is already taken. Try again.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check for a win or draw
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
tic_tac_toe()
