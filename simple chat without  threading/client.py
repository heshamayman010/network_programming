from socket import *
try:
    host = "127.0.0.1"
    port = 4555

    s = socket(AF_INET, SOCK_STREAM)

    s.connect((host, port))

    while True:
        g = input("give a message to send to ")
        s.send(g.encode("utf-8"))
        k = s.recv(2048)
        print(k.decode("utf-8"))

        if g == "q":
            s.close()
        elif k.decode("utf-8"):
            s.close()
except KeyboardInterrupt:
    print("chat is terminated")
except error as e:
    print(e)
