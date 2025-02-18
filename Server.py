# THIS SCRIPT ALWAYS HAS TO BE RUNNING FROM THE MACHINE WHERE THE IP ADDRESS IS FROM.

import socket
from _thread import *
import sys

server = "192.168.1.151"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is the type of IP I'm using. SOCK_STREAM reprisents how the server stream comes in.

try:
    s.bind((server, port)) # Attempts to bind the server to the IP.
except socket.error as e:
    str(e)

s.listen(2) # Opens up the port so you can connect to it. Parameter is how many connections, leaving empty allows infinite.
print("Waiting for a connection, Server Started.")

def read_pos(str): # Reads the position sent as a string, splits it into two and changes them into a tupple.
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


pos = [(0,0),(100,100)] # Holds positions of players.

def threaded_client(conn, player): #Stands for connection. A thread starts a new process, it runs in the background as process 2 while process 1 is still running so the program doesn't have to wait. Means you can accept multiple connections at the same time.
    conn.send(str.encode(make_pos(pos[player]))) # Converts position into string, sends it to player and convert it to a position so it can be applied.
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode()) # Trying to recieve data from the connection. Parameter is in bits.
            pos[player] = data 

            if not data:
                print("Disconnected.") # If we try recieve data from client and get nothing, we break to avoid infinite loops.
                break
            else:
                if player == 1: # If we're player 1, we send player 0's position.
                    reply = pos[0]
                else: # If we're player 0, we send player 1's position.
                    reply = pos[1] 

                print("Recieved ", data)
                print("Sending: ", reply)
            
            conn.sendall(str.encode(make_pos(reply))) # Sends information over the server as a bytes object. Encoded.
        except:
            break

    print("Lost connection.")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept() # Accepts any incoming connection, stores connection and address in conn and addr
    print("Connected to", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1