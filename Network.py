# the purpose of this script is to create a class that can connect the client to the server and take client requests to send to the server.
# This is basically like the waiter at a restaurant.
import socket



class Network:
    def __init__(self):
        # ensures that the network connects to the right class
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname(socket.gethostname())
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

n = Network()
print(n.send("Hello"))
print(n.send("Working"))

while True:
    newmessage = (n.send(input("Send message: ")))