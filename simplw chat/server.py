# creating chat room
import threading
import socket
host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

# then we change the mode of the socket into listening mode
server.listen()
clients = []
names = []


def broadcast(message):
    for client in clients:
        client.send(message)

# then define a function that will handle the conncections of the clients


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:

            # add an excpetion to the remove the clients who left

            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            broadcast(f'{name} has left the chat room!'.encode('utf-8'))
            names.remove(name)
            break
# Main function to receive the clients connection


def receive():
    while True:
        print('Server is running and listening ...')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        client.send('name?'.encode('utf-8'))
        name = client.recv(1024)
        names.append(name)
        clients.append(client)
        print(f'The alias of this client is {name}'.encode('utf-8'))
        broadcast(f'{name} has connected to the chat room'.encode('utf-8'))
        client.send('you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


# the use of main is that to make it only run only when it is the main programme and if it is imported in another prog it wont work
if __name__ == "__main__":
    receive()
