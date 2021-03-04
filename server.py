# Echo server program
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

HOST = ""
PORT = 4200

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(12)

conn, address = s.accept()
with conn:
    print('Connected by', address)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)

"""
while True:
    clientsocket: socket
    clientsocket, address = s.accept()
    print(f"Connected to {socket.gethostname()}")
    clientsocket.send(bytes(f"Server response: You are now connected to {HOST}", "utf-8"))
"""
