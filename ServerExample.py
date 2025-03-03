# the server is like the bridge between the clients. It is the thing that takes the requests of the clients and sends them to each other.

# in our actual project, this would be a separate machine from the users, that constantly has this script running, basically like how a minecraft server works or a cloud server in the random place in the ocean.

# in the server we have to set up sockets to allow for connections to come into the server from the clients on a certain port.
# a wifi basically has various ports for different purposes eg. port 80 is for HTTP requests. A lot of ports are unused, like 5555, which is the one we will use.

import socket
from _thread import *
import sys

# STEP 1:   CREATING THE PORT
# find the IP address of the server by taking the computer that the server runs on and open cmd > type "ipconfig" > copy the IPV4 Address. 
server = socket.gethostbyname(socket.gethostname()) # the ip address goes here
port = 5555



# STEP 2:   SETTING UP THE SOCKET
# AF_INET is the type of socket that has to be used with IPv4, the ip were using. SOCK_STREAM might be how the messages are sent in the server idrk.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# STEP 3:   BINDING THE PORT TO THE SOCKET
# we use a try except if the port we chose (5555) happens to be used for something on the network.
try:
    s.bind((server, port))
except socket.error as e:
    print("error occurred when binding the port to the socket")
    str(e)


# STEP 4:   OPENING THE PORT FOR A CLIENT TO CONNECT
# the parameter 2 ensures that we only have 2 clients connected in order to do a 1v1.
s.listen(2)
print("Waiting for a connection, Server Started")



def threaded_client(conn):
    # STEP 7:   RECIEVE AND SEND INFORMATION TO AND FROM THE CONNECTED CLIENT
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            # recieve a message from the client. 2048 represents a 10-bit message. BINARY REFERENCE
            # if there are errors in this stage, they might be fixed by increasing the number 2048, eg. multiplying by 8.
            data = conn.recv(2048)
            # decode the 10-bit message using utf-8 into a string for us to handle
            reply = data.decode("utf-8")

            if not data:
                # if we try to get data from the client and nothing comes back, we're probably disconnected.
                print("Disconnected")
                break
            else:
                # printing the message we recieved from the client
                print("Received: ", reply)
                print("Sending : ", reply)
            # sending a message back to the clients. sendall refers to sending all of the message. in this example we send the exact same message back as a test.
            conn.sendall(str.encode(reply))
        except:
            print("error occured in threaded_client function, while sending and recieving messages to and from client.")
            break

    print("Lost connection")
    conn.close()

# STEP 5:   SEARCHING FOR CONNECTIONS
# we remain in a while loop to constantly check for client connections
while True:
    conn, addr = s.accept() # accept an incoming connection. store the object representing the client connected in conn and the ip address of the client in addr.
    print("Connected to:", addr)
    # STEP 6:   START A THREAD FOR THE CONNECTED CLIENT
    # the thing is, we want to run the code for the connected client, but we also want to search for the other client at the same time.
    # we can use threading to do both like miles morales in spider verse.
    # so then we start a new thread which runs our "threaded_client" function, the stuff we want to run when a client is connected, while also still running this while loop to search for any more connections.
    start_new_thread(threaded_client, (conn,))
    
