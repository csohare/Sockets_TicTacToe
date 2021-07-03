import BoardClass as bC
import tkinter as tk
import socket

serverGUI = tk.Tk()
serverAddress = tk.StringVar(serverGUI)
serverPort = tk.StringVar(serverGUI)
userName = tk.StringVar(serverGUI)
currentPlayer = tk.StringVar(serverGUI)
buttons = [[0 for i in range(3)] for i in range(3)]
playerOne = bC.BoardClass()
data = None

def setupConnection(address, port):
    global conn
    global data
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((address, int(port)))
    server.listen()
    conn, address = server.accept()
    data = conn.recv(1024).decode('utf-8')
    playerOne.setUsername(2, data)
    userEntry()
    playerOne.setButtons(buttons)

def clearCanvas():
    children = serverGUI.winfo_children()
    for child in children:
        child.destroy()
    return

def createGame():
    serverGUI.geometry('363x507')
    clearCanvas()
    player1Label = tk.Label(serverGUI, text = 'Player 1: {}'.format(playerOne.giveUsername(1)), bg = 'blue', fg = 'white')
    player1Label.place(relx = 0, rely = 0.05)
    player2Label = tk.Label(serverGUI, text = 'Player 2: {}'.format(playerOne.giveUsername(2)), bg = 'blue', fg = 'white')
    player2Label.place(relx = 0, rely = 0.1)
    currentTurn = tk.Label(serverGUI, textvariable = currentPlayer, bg = 'blue', fg = 'white')
    currentTurn.place(relx=0, rely = 0.15)
    currentPlayer.set('Current Turn: ' + playerOne.giveUsername(2))
    quit = tk.Button(text='quit', command= lambda: click('Fun Times'))
    quit.place(relx=0, rely=0)
    for i in range(3):
        for y in range(3):
            buttons[i][y] = tk.Button(serverGUI, height = 8, width = 13, text = '')
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
    playerOne.setButtons(buttons)
    playerOne.setLastPlayer()
    playerOne.buttonState(0)
    serverGUI.update()
    data = conn.recv(1024).decode('utf-8')
    if data == 'Fun Times':
        showStats()
    else:
        data = data.split('-')
        row = data[0]
        column = data[1]
        playerOne.playMoveOnBoard(row, column)
        currentPlayer.set('Current Player: ' + playerOne.giveUsername(1))
        playerOne.buttonState(1)
        serverGUI.update()

def showStats():
    clearCanvas()
    player1Name, player2Name, lastPlayer, totalGames, totalWins, totalLosses, totalTies = playerOne.computeStats()
    print(playerOne.computeStats())
    stats = tk.Label(serverGUI, font=('Arial', 20), text='Game Stats', bg='blue', fg='white')
    stats.grid(row=0, sticky='nw')
    player1 = tk.Label(serverGUI, text='Player 1 Name: {}'.format(player1Name), font=('Arial, 15'), bg='blue', fg='white')
    player1.grid(row=1, sticky='w')
    player2 = tk.Label(serverGUI, text='Player 2 Name: {}'.format(player2Name), font=('Arial, 15'), bg='blue', fg='white')
    player2.grid(row=2, sticky='w')
    last = tk.Label(serverGUI, text='Last Player: {}'.format(lastPlayer), font=('Arial, 15'), bg='blue', fg='white')
    last.grid(row=3, sticky='w')
    games = tk.Label(serverGUI, text='Total Games: {}'.format(totalGames), font=('Arial, 15'), bg='blue', fg='white')
    games.grid(row=4, sticky='w')
    wins = tk.Label(serverGUI, text='Total Wins: {}'.format(totalWins), font=('Arial, 15'), bg='blue', fg='white')
    wins.grid(row=5, sticky='w')
    losses = tk.Label(serverGUI, text='Total Losses: {}'.format(totalLosses), font=('Arial, 15'), bg='blue', fg='white')
    losses.grid(row=6, sticky='w')
    ties = tk.Label(serverGUI, text='Total ties: {}'.format(totalTies), font=('Arial, 15'), bg='blue', fg='white')
    ties.grid(row=7, sticky='w')
    conn.close()

def click(button):
    global conn
    if playerOne.lastPlayer == playerOne.giveUsername(2):
        if button == 'Fun Times':
            conn.send(button.encode('utf-8'))
            showStats()
            return
        cord = button.split('-')
        row = int(cord[0])
        column = int(cord[1])
        if buttons[row][column]['text'] == '':
            playerOne.playMoveOnBoard(row, column)
            currentPlayer.set('Current Player: ' + playerOne.giveUsername(2))
            playerOne.buttonState(0)
            serverGUI.update()
            if playerOne.isGameFinished():
                conn.send(button.encode('utf-8'))
                print(playerOne.computeStats())
                serverGUI.update()
                data = conn.recv(1024).decode()
                if data == 'Play Again':
                    createGame()
                else:
                    conn.close()
                    showStats()
                return
            conn.send(button.encode('utf-8'))
            serverGUI.update()
            data = conn.recv(1024).decode('utf-8')
            if data == 'Fun Times':
                showStats()
                return
            playerOne.buttonState(1)
            serverGUI.update()
            data = data.split('-')
            row = int(data[0])
            column = int(data[1])
            playerOne.playMoveOnBoard(row, column)
            currentPlayer.set('Current Player: ' + playerOne.giveUsername(1))
            serverGUI.update()
            if playerOne.isGameFinished():
                serverGUI.update()
                print(playerOne.computeStats())
                data = conn.recv(1024).decode()
                if data == 'Play Again':
                    createGame()
                else:
                    showStats()
                return
    else:
        pass

def sendUsername(username):
    playerOne.setUsername(1, username)
    playerOne.setPlayerName(username)
    conn.send(username.encode('utf-8'))
    createGame()

def userEntry():
    clearCanvas()
    serverGUI.geometry('363x507')
    l1 = tk.Label(serverGUI, text = 'Enter Username :', borderwidth = 4, relief = 'sunken')
    l1.place(relx = 0, rely = 0.45)
    usernameEntry = tk.Entry(serverGUI, textvariable = userName)
    usernameEntry.place(relx = 0.328, rely= 0.45)
    submitName = tk.Button(serverGUI, text = 'Send', command = lambda: sendUsername(userName.get()))
    submitName.place(relx= 0.85 , rely= 0.45, height = 28, width = 55)

def startGUI():
    serverGUI.title("Player1: Two Player Tic-Tac-Toe")
    serverGUI.config(bg = 'blue')
    serverGUI.geometry('500x500')
    serverGUI.resizable(0,0)
    l1 = tk.Label(serverGUI, text="Server Address:", borderwidth = 3, relief = 'sunken')
    l2 = tk.Label(serverGUI, text="Server Port:       ", borderwidth = 3, relief = 'sunken')
    l1.place(relx = 0.2, rely= 0.45)
    l2.place(relx= 0.2, rely = 0.525)
    addressEnrty = tk.Entry(serverGUI, textvariable = serverAddress)
    portEntry = tk.Entry(serverGUI, textvariable = serverPort)
    addressEnrty.place(relx = 0.43, rely = 0.45)
    portEntry.place(relx = 0.43, rely = 0.523)
    submitB = tk.Button(text='Set Up Server',command= lambda: setupConnection(serverAddress.get(), serverPort.get()))
    submitB.place(relx = 0.425, rely = 0.59)
    serverGUI.mainloop()

if __name__ == "__main__":
    startGUI()



