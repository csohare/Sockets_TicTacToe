import tkinter as tk

class BoardClass():
    def __init__(self):
        self.buttons = [[0 for i in range(3)] for y in range(3)]
        self.gameBoard = None
        self.player1UserName = ''
        self.player2UserName = ''
        self.lastPlayer = ''
        self.totalGames = 0
        self.totalWins = 0
        self.totalTies = 0
        self.totalLosses = 0
        self.turn = True

    def recordGamePlayed(self):
        self.totalGames += 1

    def resetGameBoard(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''

    def isBoardFull(self):
        for i in range(3):
            for y in range(3):
                if self.buttons[i][y]["text"] == '':
                    return False
        return True



    def playMoveOnBoard(self, button):
        if self.lastPlayer == self.player1UserName and button["text"] == '' and self.turn == True:
            button["text"] == 'X'
            self.lastPlayer = self.player2UserName

        elif self.lastPlayer == self.player2UserName and button["text"] == '' and self.turn == True:
            button["text"] == 'O'
            self.lastPlayer = self.player1UserName





    def isGameFinished(self):
        for i in range(3):
            if((self.buttons[i][0]["text"] != '' and self.buttons[i][0]["text"] == self.buttons[i][1]["text"] and self.buttons[i][0]["text"] == self.buttons[i][2]["text"])
            or(self.buttons[0][i]["text"] != '' and self.buttons[0][i]["text"] == self.buttons[1][i]["text"] and self.buttons[0][i]["text"] == self.buttons[2][i]["text"])):
                return True
            if((self.buttons[0][0]["text"] != '' and self.buttons[0][0]["text"] == self.buttons[1][1]["text"] and self.buttons[0][0]["text"] == self.buttons[2][2]["text"])
            or(self.buttons[0][2]["text"] != '' and self.buttons[0][2]["text"] == self.buttons[1][1]["text"] and self.buttons[0][2]["text"] == self.buttons[2][0]["text"])):
                return True
        if self.isBoardFull():
            return True
        return False

        def computeStats(self):
            return self.player1UserName, self.player2UserName, self.lastPlayer, self.totalGames, self.totalWins, self.totalLosses, self.totalTies

        def setBoard(self, board):
            self.gameBoard = board

if __name__ == "__main__":
    testBoard = BoardClass()
    print(testBoard)


