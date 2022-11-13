import socket

serversocket = socket.socket() #create a socket
print('Socket Created') #print socket created when socket is created

serversocket.bind(('localhost', 44100)) # bind socket to port number

serversocket.listen(3) # wait for 3 clients to connect
print('Waiting for the connections')

while True:
    clientsocket, clientaddress = serversocket.accept()
    name = clientsocket.recv(1024).decode()
    print('Connected with', clientaddress, name)
    clientsocket.send(bytes("Welcome to Socket Programming!", 'utf-8')) # have to send as bytes not str
    clientsocket.close()


