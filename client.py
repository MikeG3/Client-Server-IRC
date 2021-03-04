# Echo client program
# Copied from https://www.youtube.com/watch?v=Lbfe3-v7yE0

import socket

PORT = 4200

# Get username for IRC
print("Please enter the user name for this client")
userName = input()

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server, with host-IP at Port 4200
sock.connect((socket.gethostname(), PORT))

# Receive and print message (max size)
message = sock.recv(512)
print(message.decode("utf-8"))

