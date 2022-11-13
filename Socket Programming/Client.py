import socket

clientsocket = socket.socket() # create client socket (can mention ipv4/ipv6 and type of network)

clientsocket.connect(('localhost', 44100))

name = input("Enter your name: ")
clientsocket.send(bytes(name, 'utf-8'))

print(clientsocket.recv(1024).decode())
