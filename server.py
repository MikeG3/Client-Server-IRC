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
# LIST OF RESERVED COMMANDS THAT ARE NOT STRING LITERLAS FOR MESSAGES
CLOSE = "#CLOSE"

# CONSTRUCT SOCKET BINDED TO SERVER ADDRESS AND PORT, FOR 12 SERVICABLE CLIENTS
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(12)
print(f"Server is actively listening to at port: {PORT}")


# VALIDATE USERNAME
def valid_user_name(name):
    if name in nick:
        return False
    return True


# RELAY MESSAGES TO ALL CLIENTS
def relay_message(message):
    for clients in client:
        # SEND MESSAGE TO ALL CLIENTS
        clients.send(message)


# RECEIVE MESSAGES
def receive_message(sender):
    while True:
        msg = sender.recv(5000).decode("ascii")
        # CHECK IF COMMAND
        if msg != CLOSE:
            relay_message(msg.encode("ascii"))
        else:
            disconnect(sender)


# CLOSE CLIENT CONNECTION
def disconnect(close_requester):
    # remove user name and nick from lists
    # code here
    # disconnect
    close_requester.close()
    # close thread
    print(f"{close_requester} disconnected from the server")


# IRC MAIN PROGRAM LOOP
print("SERVER FOR IRC IS NOW ACTIVE\n")
while True:
    # ACCEPT NEW CLIENTS AND INCOMING DATA
    user, address = s.accept()
    print(f'Connected to {address}\n')
    # SAVE USER AS CONNECTED CLIENT
    client.append(user)
    print("\nClient has been appended")
    # REQUEST NICK
    user.send("Please send your nickname for the IRC".encode("ascii"))
    user_name = user.recv(100).decode("ascii")
    if valid_user_name(user_name):
        nick.append(user_name)
        # ANNOUNCE NEW USER IN CHAT ROOM
        user.send("Welcome to IRC default Chat Room".encode("ascii"))
        relay_message(f"\n{user_name} has joined the IRC".encode("ascii"))
        # CREATE THREAD FOR EACH CLIENT IN ORDER TO HANDLE MULTIPLE CLIENTS
        client_thread = threading.Thread(target=receive_message, args=(user,))
        client_thread.start()
    else:
        user.send("The user name that you entered is already in use\n".encode("ascii"))
        user.send("Please try a different username".encode("ascii"))
        # DISCONNECT FROM SERVER
