import socket
import tkinter as tk
import BoardClass as bC

clientGUI = tk.Tk()
serverAddress = tk.StringVar(clientGUI)
serverPort = tk.StringVar(clientGUI)
userName = tk.StringVar(clientGUI)
currentPlayer = tk.StringVar(clientGUI)
buttons = [[0 for i in range(3)] for y in range(3)]
playerTwo = bC.BoardClass()
data = None
flag = 0

def connectToServer(address, port):
    address = socket.gethostbyname(address)
    global clientSocket
    global data
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        clientSocket.connect((address, int(port)))
    except:
        retryUI = tk.Tk()
        clientGUI.withdraw()
        retryUI.title('Try Again?')
        l1 = tk.Label(retryUI, text= 'Connection Failed')
        l1.pack(side = 'top')
        retryUI.config(bg='blue')
        yButton = tk.Button(retryUI, text='Retry Connection?', command= lambda: [clientGUI.deiconify(), retryUI.destroy()])
        yButton.pack(side= 'left')
        nButton = tk.Button(retryUI, text= 'Close Game',command = lambda: [clientGUI.destroy(), retryUI.destroy()])
        nButton.pack(side = 'left')
        retryUI.mainloop()
    userEntry()

def replayGUI():
    global replay
    global flag
    if flag == 0:
        replay = tk.Tk()
        replay.config(bg = 'blue')
        replay.resizable(0, 0)
        replay.title('')
        l1 = tk.Label(replay, text= 'Game Over')
        l1.pack(side = 'top')
        quit = tk.Button(replay, text = 'Quit   ', command = lambda: gameOver('Fun Times'))
        quit.pack(side = 'left')
        playAgain= tk.Button(replay, text = 'Play Again', command = lambda: gameOver('Play Again'))
        playAgain.pack(side = 'right')
        flag = 1
        replay.mainloop()
    else:
        replay.deiconify()

def gameOver(choice):
    if choice == 'Fun Times':
        clientSocket.send(choice.encode('utf-8'))
        showStats()
        replay.destroy()
    else:
        clientSocket.send(choice.encode('utf-8'))
        replay.withdraw()
        createGame()

def showStats():
    clearCanvas()
    player1Name, player2Name, lastPlayer, totalGames, totalWins, totalLosses, totalTies = playerTwo.computeStats()
    print(playerTwo.computeStats())
    stats = tk.Label(clientGUI, font=('Arial', 20), text='Game Stats', bg='blue', fg='white')
    stats.grid(row=0, sticky='nw')
    player1 = tk.Label(clientGUI, text='Player 1 Name: {}'.format(player1Name), font=('Arial, 15'), bg='blue', fg='white')
    player1.grid(row=1, sticky='w')
    player2 = tk.Label(clientGUI, text='Player 2 Name: {}'.format(player2Name), font=('Arial, 15'), bg='blue', fg='white')
    player2.grid(row=2, sticky='w')
    last = tk.Label(clientGUI, text='Last Player: {}'.format(lastPlayer), font=('Arial, 15'), bg='blue', fg='white')
    last.grid(row=3, sticky='w')
    games = tk.Label(clientGUI, text='Total Games: {}'.format(totalGames), font=('Arial, 15'), bg='blue', fg='white')
    games.grid(row=4, sticky='w')
    wins = tk.Label(clientGUI, text='Total Wins: {}'.format(totalWins), font=('Arial, 15'), bg='blue', fg='white')
    wins.grid(row=5, sticky='w')
    losses = tk.Label(clientGUI, text='Total Losses: {}'.format(totalLosses), font=('Arial, 15'), bg='blue', fg='white')
    losses.grid(row=6, sticky='w')
    ties = tk.Label(clientGUI, text='Total Ties: {}'.format(totalTies), font=('Arial, 15'), bg='blue', fg='white')
    ties.grid(row=7, sticky='w')
    clientSocket.close()

def createGame():
    clearCanvas()
    clientGUI.geometry('363x507')
    player1Label = tk.Label(clientGUI, text='Player 1: {}'.format(playerTwo.giveUsername(1)), bg='blue', fg='white')
    player1Label.place(relx=0, rely=0.05)
    player2Label = tk.Label(clientGUI, text='Player 2: {}'.format(playerTwo.giveUsername(2)), bg='blue', fg='white')
    player2Label.place(relx=0, rely=0.1)
    currentTurn = tk.Label(clientGUI, textvariable=currentPlayer, bg='blue', fg='white')
    currentTurn.place(relx=0, rely=0.15)
    currentPlayer.set('Current Turn: ' + playerTwo.giveUsername(2))
    quit = tk.Button(text = 'quit' , command = lambda: click('Fun Times'))
    quit.place(relx = 0, rely = 0)
    for i in range(3):
        for y in range(3):
            buttons[i][y] = tk.Button(clientGUI, height = 8, width = 13, text = '')
            if i == 0:
                buttons[i][y].grid(row = i, column = y, pady = (110, 0))
            else:
                buttons[i][y].grid(row = i, column = y)
    buttons[0][0].config(command=lambda: click('0-0'))
    buttons[0][1].config(command=lambda: click('0-1'))
    buttons[0][2].config(command=lambda: click('0-2'))
    buttons[1][0].config(command=lambda: click('1-0'))
    buttons[1][1].config(command=lambda: click('1-1'))
    buttons[1][2].config(command=lambda: click('1-2'))
    buttons[2][0].config(command=lambda: click('2-0'))
    buttons[2][1].config(command=lambda: click('2-1'))
    buttons[2][2].config(command=lambda: click('2-2'))
    playerTwo.setButtons(buttons)
    playerTwo.setLastPlayer()

def click(button):
    if playerTwo.giveLastPlayer() == playerTwo.giveUsername(1):
        if button == 'Fun Times':
            clientSocket.send(button.encode('utf-8'))
            showStats()
            return
        cord = button.split('-')
        playedrow = int(cord[0])
        playedcolumn = int(cord[1])
        if buttons[playedrow][playedcolumn]['text'] == '':
            playerTwo.playMoveOnBoard(playedrow, playedcolumn)
            currentPlayer.set('Current Turn: ' + playerTwo.giveUsername(1))
            playerTwo.buttonState(0)
            clientGUI.update()
            if playerTwo.isGameFinished():
                clientSocket.send(button.encode('utf-8'))
                replayGUI()
                return
            clientSocket.send(button.encode('utf-8'))
            data = clientSocket.recv(1024).decode('utf-8')
            if data == 'Fun Times':
                showStats()
                return
            playerTwo.buttonState(1)
            data = data.split('-')
            recvrow = data[0]
            recvcolumn = data[1]
            playerTwo.playMoveOnBoard(recvrow, recvcolumn)
            currentPlayer.set('Current Turn: ' + playerTwo.giveUsername(2))
            if playerTwo.isGameFinished():
                clientGUI.update()
                replayGUI()
                return
    else:
        pass

def clearCanvas():
    children = clientGUI.winfo_children()
    for child in children:
        child.destroy()
    return

def sendUsername(name):
    global data
    playerTwo.setPlayerName(name)
    playerTwo.setUsername(2, name)
    clientSocket.send(name.encode('utf-8'))
    data = clientSocket.recv(1024).decode('utf-8')
    playerTwo.setUsername(1, data)
    clearCanvas()
    createGame()

def userEntry():
    clearCanvas()
    clientGUI.geometry('363x507')
    l1 = tk.Label(clientGUI, text = 'Enter Username :', borderwidth = 4, relief = 'sunken')
    l1.place(relx = 0, rely = 0.45)
    usernameEntry = tk.Entry(clientGUI, textvariable = userName)
    usernameEntry.place(relx = 0.328, rely= 0.45)
    submitName = tk.Button(clientGUI, text = 'Send', command = lambda: sendUsername(userName.get()))
    submitName.place(relx= 0.85 , rely= 0.45, height = 28, width = 55)

def startGUI():
    clientGUI.title("Player 2: Two Player Tic-Tac-Toe")
    clientGUI.config(bg = 'blue')
    clientGUI.geometry('500x500')
    clientGUI.resizable(0,0)
    l1 = tk.Label(clientGUI, text="HostName/IP    ", borderwidth = 3, relief = 'sunken')
    l2 = tk.Label(clientGUI, text="Server Port       ", borderwidth = 3, relief = 'sunken')
    l1.place(relx = 0.2, rely= 0.45)
    l2.place(relx= 0.2, rely = 0.525)
    addressEnrty = tk.Entry(clientGUI, textvariable = serverAddress)
    portEntry = tk.Entry(clientGUI, textvariable = serverPort)
    addressEnrty.place(relx = 0.43, rely = 0.45)
    portEntry.place(relx = 0.43, rely = 0.523)
    submitB = tk.Button(text='Confirm Port and Address', command= lambda: connectToServer(serverAddress.get(), serverPort.get()))
    submitB.place(relx = 0.355, rely = 0.59)
    clientGUI.mainloop()

if __name__ == "__main__":
    startGUI()