import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 1111))
inpt = input()
clientsocket.send(bytes(inpt, 'UTF-8'))
print("the message has been sent")
