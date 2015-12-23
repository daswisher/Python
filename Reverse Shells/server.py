import socket
import sys

# Create socket for computer to connect to
def socket_create():
	try:
		global host
		global port
		global s
		host = ''
		port = 1234
		s = socket.socket()
	except socket.error as msg: # Saves error into variable msg
		print("Socket creation error: " + str(msg))


