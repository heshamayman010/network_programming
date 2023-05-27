from socket import *
try:
    s = socket(AF_INET, SOCK_STREAM)

    host = "127.0.0.1"
    port = 4555

    s.bind((host, port))
    s.listen(6)
    client, addr = s.accept()
    print("accepted the connection from ", addr[0])
    print("you have established a connection")
    while True:
        x = client.recv(2048)
        print(x.decode("utf-8"))
        y = input("give a message to send")
        client.send(y.encode("utf-8"))

        if x.decode("utf-8") == "q":
            s.close()
        elif y == "q":
            s.close()

except error as i:
    print(i)
except KeyboardInterrupt:
    print("chat is terminated")
