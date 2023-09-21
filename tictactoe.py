import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.ai_player = 'O'
        self.create_widgets()
        self.reset_board()

    def create_widgets(self):
        self.buttons = [[tk.Button(self.master, text=' ', font=('Arial', 60), width=3, height=1, command=lambda row=row, col=col: self.button_click(row, col)) for col in range(3)] for row in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].grid(row=row, column=col)
        self.reset_button = tk.Button(self.master, text='Reset', font=('Arial', 20), width=6, command=self.reset_board)
        self.reset_button.grid(row=3, column=1)

    def reset_board(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.update_board()

    def update_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=self.board[row][col])

    def button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.update_board()
            if self.check_win(self.current_player):
                messagebox.showinfo('Game Over', f'{self.current_player} wins!')
                self.reset_board()
            elif self.check_tie():
                messagebox.showinfo('Game Over', 'Tie game!')
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.current_player == self.ai_player:
                    self.ai_move()

    def check_win(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def ai_move(self):
        best_score = float('-inf')
        best_move = None
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    self.board[row][col] = self.ai_player
                    score = self.minimax(False)
                    self.board[row][col] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        self.board[best_move[0]][best_move[1]] = self.ai_player
        self.update_board()
        if self.check_win(self.ai_player):
            messagebox.showinfo('Game Over', f'{self.ai_player} wins!')
            self.reset_board()
        elif self.check_tie():
            messagebox.showinfo('Game Over', 'Tie game!')
            self.reset_board()
        else:
            self.current_player = 'X'

    def minimax(self, is_maximizing):
        if self.check_win(self.ai_player):
            return 1
        elif self.check_win('X'):
            return -1
        elif self.check_tie():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == ' ':
                        self.board[row][col] = self.ai_player
                        score = self.minimax(False)
                        self.board[row][col] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == ' ':
                        self.board[row][col] = 'X'
                        score = self.minimax(True)
                        self.board[row][col] = ' '
                        best_score = min(score, best_score)
            return best_score

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
