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

# Bind socket ot port and wait for connection from client
def socket_bind():
	try:
		global host
		global port
		global s
		print("Binding socket to port: " + str(port))
		s.bind((host, port))
		s.listen(5) # 5 is the number of bad connections it'll receive before it'll start refusing connections
	except socket.error as msg:
		print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
		socket_bind()

# Establish connection with client from listening socket
def socket_accept():
	conn, address = s.accept() # s.accept() accepts new connections
	print("Connection has been established | " + "IP " +  address[0] + " | Port " + str(address[1]))
	send_commands(conn)
	conn.close()
