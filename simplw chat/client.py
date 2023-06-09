import threading
import socket
from socket import *
name = input('Choose an name >>> ')
client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 59000))


def client_receive():
    # forever loop to continue the work
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "name?":
                client.send(name.encode('utf-8'))
            else:
                print(message)
        except error as e:
            print(f'{e}')
            client.close()
            break


def client_send():
    while True:
        message = f'{name}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
