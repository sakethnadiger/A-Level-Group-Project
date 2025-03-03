# the purpose of this script is to create a class that can connect the client to the server and take client messages to send to the server.
# This is basically like the waiter at a restaurant.
import socket



class Network:
    def __init__(self):
        # ensures that the network connects to the right server socket and port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname(socket.gethostname())
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        # upon initialisation, attempt to connect to the server and print when connected.
        print(self.id)

    def connect(self):
        try:
            # attempts to connect the client to the server
            self.client.connect(self.addr)
            # return the "Connected" message we have set the server to send once a connection has been made.
            return self.client.recv(2048).decode()
        except:
            print("error: not able to connect the network to the server")

    def send(self, data):
        try:
            # when this function is run, it will send the data in the parameter and return the message that the server gives back.
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

n = Network()
# sending these two messages and printing the returned response. in this test, we have set up the server to send back the same messages it recieves, so we should just get the same message back.
print(n.send("Hello"))
print(n.send("Working"))

while True:
    newmessage = (n.send(input("Send message: ")))