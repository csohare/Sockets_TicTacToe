import BoardClass as BC
import tkinter as tk
import socket



#Making the GUI
serverGUI = tk.Tk()
serverAddress = tk.StringVar(serverGUI)
serverPort = tk.StringVar(serverGUI)
buttons = [[0 for i in range(3)] for i in range(3)]
player1 = BC.BoardClass()


def setupConnection(address, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((address, int(port)))
    server.listen()
    conn, address = server.accept()
    print('connected')
    clearCanvas()
    createGrid()

    #data = conn.recv(1024)
    #print(data.decode('utf-8'))

def clearCanvas():
    children = serverGUI.winfo_children()
    for child in children:
        child.destroy()
    return

def createGrid():
    for i in range(3):
        for y in range(3):
            buttons[i][y] = tk.Button(serverGUI, height = 15, width = 10, text = '', command = lambda: player1.playMoveOnBoard(buttons[i][y]))
            buttons[i][y].grid(row = i, column = y)
    return



def setupGUI():
    serverGUI.title("Server: Two Player Tic-Tac-Toe")
    serverGUI.config(bg = 'blue')
    serverGUI.geometry('500x500')
    serverGUI.resizable(0,0)
    l1 = tk.Label(serverGUI, text="Server Address", borderwidth = 3, relief = 'sunken')
    l2 = tk.Label(serverGUI, text="Server Port       ", borderwidth = 3, relief = 'sunken')
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
    setupGUI()



