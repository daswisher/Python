import socket
import threading
import sys
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_addresses = []

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
		s.bind((host, port))
		s.listen(5) # 5 is the number of bad connections it'll receive before it'll start refusing connections
	except socket.error as msg:
		print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
		time.sleep(5)
		socket_bind()

# Accept connections form clients and save to list
def accept_connections():
	for c in all_connections:
		c.close()
	del all_connections[:]
	del all_addresses[:]
	while 1:
		try:
			conn, address = s.accept()
			conn.setblocking(1) #No timeout
			all_connections.append(conn)
			all_addresses.append(address)
			print("\nConnection has been established: " + address[0])
		except:
			print("Error accepting connections")

