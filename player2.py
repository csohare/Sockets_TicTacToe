import socket
import tkinter as tk
import BoardClass as BC




clientGUI = tk.Tk()
serverAddress = tk.StringVar(clientGUI)
serverPort = tk.StringVar(clientGUI)
buttons = [[0 for i in range(3)] for y in range(3)]



def connectToServer(address, port):
    address = socket.gethostbyname(address)
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        clientSocket.connect((address, int(port)))
        #clientSocket.send(b'testing')
        #clientSocket.recv(1024)
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


#def createButtons():



def setupGUI():
    clientGUI.title("Client: Two Player Tic-Tac-Toe")
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
    setupGUI()