import tkinter as tk
from tkinter import messagebox
import random

# Function to handle a player's move
def on_click(row, col):
    global current_player, game_over
    if buttons[row][col]["text"] == "" and not game_over:
        buttons[row][col]["text"] = current_player
        board[row][col] = current_player
        if check_win(current_player):
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins! jitis hai jitis")
            game_over = True
        elif check_draw():
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"
            if current_player == "O":
                computer_move()

# Function to handle the computer's move
def computer_move():
    global current_player, game_over
    if not game_over:
        empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            buttons[row][col]["text"] = current_player
            board[row][col] = current_player
            if check_win(current_player):
                messagebox.showinfo("Tic-Tac-Toe", "Computer le jityo ta !")
                game_over = True
            elif check_draw():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                game_over = True
            else:
                current_player = "X"

# Function to check if the current player has won
def check_win(player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Function to check if the game is a draw
def check_draw():
    for row in board:
        if "" in row:
            return False
    return True

# Function to reset the game
def reset_game():
    global current_player, game_over, board
    current_player = "X"
    game_over = False
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize the game variables
current_player = "X"
game_over = False
board = [["" for _ in range(3)] for _ in range(3)]

# Create the 3x3 grid of buttons
buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=('Arial', 20), width=5, height=2,
                                      command=lambda row=row, col=col: on_click(row, col))
        buttons[row][col].grid(row=row, column=col)

# Add a reset button
reset_button = tk.Button(root, text="Reset", font=('Arial', 15), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

# Start the Tkinter main loop
root.mainloop()
