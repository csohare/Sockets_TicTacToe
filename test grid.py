import tkinter as tk
serverGUI = tk.TK()
serverGUI.title("Server: Two Player Tic-Tac-Toe")
serverGUI.config(bg = 'blue')
serverGUI.geometry('500x500')
serverGUI.resizable(0,0)

def createGrid():
    for i in range(3):
        for y in range(3):
            buttons[i][y] = tk.Button(serverGUI, height = 15, width = 10, text = '', command = lambda: player1.playMoveOnBoard(buttons[i][y]))
            buttons[i][y].grid(row = i, column = y)
    return