import tkinter as tk
import socket


class ClientGUI:
    def __init__(self, master):
        self.master = master
        master.title("Client GUI")

        # Create widgets
        self.label = tk.Label(master, text="Enter message:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Send", command=self.send_message)
        self.button.pack()

    def send_message(self):
        message = self.entry.get()
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect(('127.0.0.1', 7070))
        clientsocket.send(bytes(message, 'UTF-8'))
        print("the message has been sent")
        clientsocket.close()


root = tk.Tk()
client_gui = ClientGUI(root)
root.mainloop()
