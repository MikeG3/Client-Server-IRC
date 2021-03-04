# Echo client program
"""
CLIENT DESCRIPTION
Client constructs socket and binds it to its IP ADDRESS and PORT
Client inputs userName for IRC (NICK)
Client can join and disconnect to IRC Server
Client receives all broadcasted messages from IRC Server
Client can send message to IRC Server
"""

import socket
HOST = socket.gethostname()
PORT = 4200

# Get username for IRC
print("Please enter the user name for this client")
userName = input()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))


"""
# Create socket
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server, with host-IP at Port 4200
a.connect((socket.gethostname(), PORT))

# Receive and print message (max size)
message = a.recv(512)
print(message.decode("utf-8"))
"""

