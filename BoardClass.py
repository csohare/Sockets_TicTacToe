class BoardClass:
    def __init__(self):
        self.buttons = ''
        self.gameBoard = None
        self.player1UserName = 'player1'
        self.player2UserName = 'player2'
        self.lastPlayer = ''
        self.totalGames = 0
        self.totalWins = 0
        self.totalTies = 0
        self.totalLosses = 0
        self.playCount = 0
        self.userName = ''

    def recordGamePlayed(self):
        self.totalGames += 1

    def resetGameBoard(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''

    def isBoardFull(self):
        if self.playCount == 9:
            return True
        return False

    def returnBoard(self):
        return self.buttons

    def playMoveOnBoard(self, row, column):
        #if self.lastPlayer == self.player1UserName and button["text"] == '' and self.turn == True:
        row = int(row)
        column = int(column)
        if self.lastPlayer == self.player1UserName and self.buttons[row][column]['text'] == '':
            self.buttons[row][column]["text"] = 'X'
            #self.buttons[row][column]['state'] = 'disabled'
            self.playCount += 1
            self.lastPlayer = self.player2UserName

        elif self.lastPlayer == self.player2UserName and self.buttons[row][column]['text'] == '':
            self.buttons[row][column]["text"] = 'O'
            #self.buttons[row][column]['state'] = 'disabled'
            self.playCount += 1
            self.lastPlayer = self.player1UserName




    def isGameFinished(self):
        for i in range(3):
            if(self.buttons[i][0]["text"] != '' and self.buttons[i][0]["text"] == self.buttons[i][1]["text"] and self.buttons[i][0]["text"] == self.buttons[i][2]["text"]):
                if self.lastPlayer == self.userName:
                    self.buttons[i][0].config(highlightbackground = 'green')
                    self.buttons[i][1].config(highlightbackground = 'green')
                    self.buttons[i][2].config(highlightbackground = 'green')
                    self.totalWins += 1
                    self.recordGamePlayed()
                    self.playCount = 0

                else:
                    self.buttons[i][0].config(highlightbackground='red')
                    self.buttons[i][1].config(highlightbackground='red')
                    self.buttons[i][2].config(highlightbackground='red')
                    self.totalLosses += 1
                    self.recordGamePlayed()
                    self.playCount = 0
                self.buttonState(0)
                return True
            elif(self.buttons[0][i]["text"] != '' and self.buttons[0][i]["text"] == self.buttons[1][i]["text"] and self.buttons[0][i]["text"] == self.buttons[2][i]["text"]):
                if self.lastPlayer == self.userName:
                    self.buttons[0][i].config(highlightbackground = 'green')
                    self.buttons[1][i].config(highlightbackground = 'green')
                    self.buttons[2][i].config(highlightbackground = 'green')
                    self.totalWins += 1
                    self.recordGamePlayed()
                    self.playCount = 0
                else:
                    self.buttons[0][i].config(highlightbackground='red')
                    self.buttons[1][i].config(highlightbackground='red')
                    self.buttons[2][i].config(highlightbackground='red')
                    self.totalLosses += 1
                    self.recordGamePlayed()
                    self.playCount = 0
                self.buttonState(0)
                return True
            elif(self.buttons[0][0]["text"] != '' and self.buttons[0][0]["text"] == self.buttons[1][1]["text"] and self.buttons[0][0]["text"] == self.buttons[2][2]["text"]):
                if self.lastPlayer == self.userName:
                    self.buttons[0][0].config(highlightbackground = 'green')
                    self.buttons[1][1].config(highlightbackground = 'green')
                    self.buttons[2][2].config(highlightbackground = 'green')
                    self.totalWins += 1
                    self.recordGamePlayed()
                    self.playCount = 0
                else:
                    self.buttons[0][0].config(highlightbackground='red')
                    self.buttons[1][1].config(highlightbackground='red')
                    self.buttons[2][2].config(highlightbackground='red')
                    self.totalLosses += 1
                    self.recordGamePlayed()
                    self.playCount = 0
                self.buttonState(0)
                return True
            elif(self.buttons[0][2]["text"] != '' and self.buttons[0][2]["text"] == self.buttons[1][1]["text"] and self.buttons[0][2]["text"] == self.buttons[2][0]["text"]):
                if self.lastPlayer == self.userName:
                    self.buttons[0][2].config(highlightbackground = 'green')
                    self.buttons[1][1].config(highlightbackground = 'green')
                    self.buttons[2][0].config(highlightbackground = 'green')
                    self.totalWins += 1
                    self.recordGamePlayed()
                    self.playCount = 0
                else:
                    self.buttons[0][2].config(highlightbackground='red')
                    self.buttons[1][1].config(highlightbackground='red')
                    self.buttons[2][0].config(highlightbackground='red')
                    self.totalLosses += 1
                    self.recordGamePlayed()
                    self.playCount = 0
                self.buttonState(0)
                return True
            elif self.isBoardFull():
                self.totalTies += 1
                self.recordGamePlayed()
                self.playCount = 0
                self.buttonState(0)
                return True
        return False

    def computeStats(self):
        return self.player1UserName, self.player2UserName, self.lastPlayer, self.totalGames, self.totalWins, self.totalLosses, self.totalTies

    def setBoard(self, board):
        self.gameBoard = board

    def setButtons(self, buttonArray):
        self.buttons = buttonArray

    def setUsername(self, playerNum, name):
        if playerNum == 1:
            self.player1UserName = name
        else:
            self.player2UserName = name
        self.lastPlayer = self.player1UserName

    def giveUsername(self, playerNum):
        if playerNum == 1:
            return self.player1UserName
        else:
            return self.player2UserName

    def setPlayerName(self, name):
        self.userName = name

    def setLastPlayer(self):
        self.lastPlayer = self.player1UserName

    def giveLastPlayer(self):
        return self.lastPlayer

    def buttonState(self, state):
        if state == 0:
            for row in self.buttons:
                for button in row:
                    button.config(state = 'disabled')
        elif state == 1 :
            for row in self.buttons:
                for button in row:
                    button.config(state = 'normal')


if __name__ == "__main__":
    testBoard = BoardClass()
    print(testBoard.computeStats())




