# SERVER FOR CLIENT-SERVER IRC
"""
SERVER DESCRIPTION
Server will construcr a socket and bind its IP ADDRESS and PORT to it
Server listens to responses at the socket
Server will allow clients to join its general channel
    Nickname required to enter and allow for message transfer
Server Accepts and broadcasts messages
Server handles disconnections from clients
"""

import socket
import threading

# FIXED HOST ADDRESS AND PORT
HOST = ""
PORT = 4200
# LIST OF CLIENT AND NICK'S
client = []
nick = []

# CONSTRUCT SOCKET BINDED TO SERVER ADDRESS AND PORT, FOR 12 SERVICABLE CLIENTS
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(12)


# RELAY MESSAGES TO ALL CLIENTS
def relay_message(message):
    for clients in client:
        clients.send(message)


# RECEIVE MESSAGES
def receive_message():
    while True:
        msg = client.recv(5000)
        relay_message(msg)


print("SERVER FOR IRC IS NOW ACTIVE\n")

# IRC MAIN PROGRAM LOOP
while True:
    # ACCEPT NEW CLIENTS AND INCOMING DATA
    user, address = s.accept()
    print(f'Connected to {user} at {address}')
    data = user.recv(1024)
    # SAVE USER AS CONNECTED CLIENT
    client.append(user)
    # REQUEST NICK
    user.send("Please send your nickname for the IRC")
    user_name = client.recv(100).encode("ascii")
    nick.append(user_name)
    # ANNOUNCE NEW USER IN CHAT ROOM
    client.send("Welcome to IRC default Chat Room")
    relay_message(f"{user_name} has joined the IRC")
    # CREATE THREAD FOR EACH CLIENT IN ORDER TO HANDLE MULTIPLE CLIENTS
    threading.Thread(target=handle, args=(user,))

