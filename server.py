# Echo server program
# Copied https://www.youtube.com/watch?v=Lbfe3-v7yE0

import socket

HOST = "Server X"
PORT = 4200

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), PORT))
sock.listen(12)

while True:
    clientsocket: socket
    clientsocket, address = sock.accept()
    print(f"Connected to {socket.gethostname()}")
    clientsocket.send(bytes(f"Server response: You are now connected to {HOST}", "utf-8"))

