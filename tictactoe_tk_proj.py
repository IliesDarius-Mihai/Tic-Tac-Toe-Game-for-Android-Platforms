# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:07:49 2024

@author: ilies
"""
import tkinter as tk
from tkinter import messagebox
import sys

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        
    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=("Helvetica", 20), width=5, height=2,
                                                command=lambda row=i, col=j: self.button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)
                
        restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        restart_button.grid(row=3, column=0)
        
        exit_button = tk.Button(self.root, text="Exit", command=self.exit_game)
        exit_button.grid(row=3, column=1)
        
    def button_click(self, row, col):
        if self.board[row][col] == "":
            self.buttons[row][col].config(text=self.current_player)
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.restart_game()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.restart_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        
    def check_winner(self, row, col):
        if self.board[row][0] == self.board[row][1] == self.board[row][2] == self.current_player:
            return True
        if self.board[0][col] == self.board[1][col] == self.board[2][col] == self.current_player:
            return True
        if (row == col and self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player) or \
           (row + col == 2 and self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player):
            return True
        return False
    
    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True
    
    def restart_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
                self.board[i][j] = ""
        self.current_player = "X"
        
    def exit_game(self):
        self.root.destroy()
        sys.exit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()

