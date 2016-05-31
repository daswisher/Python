#!/usr/bin/env python

import socket

MAX_BUFFER = 1024

myClientSocket = socket.socket()

localHost = socket.gethostname()

localPort = 5555

myClientSocket.connect((localHost, localPort))

msg = myClientSocket.recv(MAX_BUFFER)
print msg

myClientSocket.close()
