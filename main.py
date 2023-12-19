import tkinter as tk
from tkinter import messagebox

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '':
            return True

    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return True

    if board[0][0] == board[1][1] == board[2][2] != '' or board[0][2] == board[1][1] == board[2][0] != '':
        return True

    return False

def on_click(row, col):
    global current_player, game_over

    if buttons[row][col]['text'] == '' and not game_over:
        buttons[row][col]['text'] = current_player

        board[row][col] = current_player

        if check_winner(board):
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            game_over = True
        else:
            if all([cell != '' for row in board for cell in row]):
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'

def reset_game():
    global current_player, game_over

    current_player = 'X'
    game_over = False

    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ''
            board[i][j] = ''

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

current_player = 'X'
game_over = False

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='', font=('Arial', 20), width=5, height=2,
                                   command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j)

reset_button = tk.Button(root, text='Reset', font=('Arial', 12), command=reset_game)
reset_button.grid(row=3, columnspan=3)

root.mainloop()
