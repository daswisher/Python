#!/usr/bin/env python

import socket

myServerSocket = socket.socket()

localHost = socket.gethostname()

localPort = 5555

myServerSocket.bind((localHost, localPort))

myServerSocket.listen(1)

print "Waiting for connection request ..."

conn, clientInfo = myServerSocket.accept()

print "Connection received from:", clientInfo

conn.send("Connection confirmed: IP: " + clientInfo[0] + " Port: " +str(clientInfo[1]))
