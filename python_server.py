#!/usr/bin/python           # This is server.py file                                                                                                                                                                           

import socket               # Import socket module
import thread
import time

def on_new_client(clientsocket,addr):
    while True:
        # msg = clientsocket.recv(1024)
        #do some checks and if msg == someWeirdSignal: break:
        # print addr, ' >> ', msg
        # msg = raw_input('SERVER >> ')
        msg = 'hello world\n'
        clientsocket.send(msg)
        time.sleep(1)
    clientsocket.close()

s = socket.socket()         # Create a socket object
host = '0.0.0.0' 
port = 50000                # Reserve a port for your service.

print 'Server started!'
print (host + ',' + port.__str__() + 'Waiting for clients...')
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.

while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   thread.start_new_thread(on_new_client,(c,addr))
s.close()
