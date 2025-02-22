import socket

# Creating a class to be reused in the future

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1" # This is this server address, not the client, it will stay the same.
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr) # This will try to connect to the server.
            return self.client.recv(2048).decode() # Recieves 2048 bits from the server and decodes it.
        except:
            pass
    
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

# n = Network() # Testing variable.
# print(n.send("Hello"))
# print(n.send("Working"))