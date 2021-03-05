# CLIENT FOR CLIENT-SERVER IRC
"""
CLIENT DESCRIPTION
Client constructs socket and binds it to its IP ADDRESS and PORT
Client inputs userName for IRC (NICK)
Client can join and disconnect to IRC Server
Client receives all broadcasted messages from IRC Server
Client can send message to IRC Server
"""

import socket
import threading

# VARIABLES FOR CLIENT IDENTIFICATION
HOST = socket.gethostname()
PORT = 4200
# Get username for IRC
print("Please enter the user name for this client")
userName = input()

print(f"\nyour userName is {userName}")

# CREATE SOCKET AND CONNECT IT TO THE IRC SERVER
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print(f"\nA socket has been created and connected to the IRC Server")


def receive_message():
    while True:
        message = s.recv(5000).decode("ascii")
        if message == "Please send your nickname for the IRC":
            s.send(userName.encode("ascii"))
            print(f"\nYour nickname {userName} has been registered with IRC\nYou are now welcome to chat")
        else:
            print(message)


def send_message():
    while True:
        message = userName + ": " + input()
        s.send(message.encode("ascii"))


# CREATE 2 THREADS, FOR MULTI-TASKING: 1 FOR SENDING MESSAGES AND 1 FOR RECEIVING MESSAGES
receive_message_thread = threading.Thread(target=receive_message)
send_message_thread = threading.Thread(target=send_message)

# RUN BOTH THREADS
print(f"\nNow running both threads {userName}")
receive_message_thread.start()
send_message_thread.start()
