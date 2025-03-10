# check the online example 1 folder for an explanation of this kind of code

import socket
from _thread import *
import sys

# find the IP address of the server by taking the computer that the server runs on and open cmd > type "ipconfig" > copy the IPV4 Address.
server = "10.2.64.51"  # the ip address goes here
#server = socket.gethostbyname(socket.gethostname())
port = 5555



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print("error occurred when binding the port to the socket")
    str(e)


s.listen()
print("Waiting for a connection, Server Started")

currentmsg = [".","."]

def threaded_client(conn, user):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        # try:
            data = conn.recv(2048)
            currentmsg[user] = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", currentmsg[user])
                if user == 0:
                    reply = currentmsg[1]
                    print("Sending : ", reply)
                else:
                    reply = currentmsg[0]
                    print("Sending : ", reply)
            print(currentmsg)
            conn.sendall(str.encode(reply))
        # except:
        #     print("error occured in threaded_client function, while sending and recieving messages to and from client.")
        #     break

    print("Lost connection")
    conn.close()

userID = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, userID))
    userID += 1