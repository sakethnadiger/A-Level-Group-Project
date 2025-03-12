# check the online example 1 folder for an explanation of this kind of code
import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.173"
        # self.server = socket.gethostbyname(socket.gethostname())
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()

    # def getPos(self):
    #     return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
            # print("error: not able to connect the network to the server")

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

# n = Network()
# print(n.send("Hello"))
# print(n.send("Working"))

# for i in range(10, 20):
#     print(n.send(str(i)))