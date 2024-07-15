#!/usr/bin/python3

import socket
from pwn import xor

def server_connect(server):
	try:
		sock = socket.socket()
		sock.connect((server))
		server_msg = sock.recv(2046).decode()
		print('SUCCESS')
		print('\n',server_msg)

		xor_op(sock, server_msg)
	except socket.error as err:
		print(f'Failed to connect: Error {err}')
		main()

def xor_op(sock, server_msg):
	enc_hash = server_msg.split(':')
	enc_hash = enc_hash[1].strip()
	enc_hash = bytes.fromhex(enc_hash)

	key1 = xor(enc_hash[:4], b'THM{')
	key2 = xor(enc_hash[-1:], b'}')
	full_key = (key1.decode()+key2.decode())
	enc_key = full_key.encode()
	result = xor(enc_hash, enc_key)
	print(f'The decoded input is: {result.decode()}\nKey: {full_key}')
	key_send = full_key + '\n'
	sock.recv(1024)
	sock.sendall(key_send.encode())
	print(sock.recv(1024).decode())
	

def main():
	target = input('Enter target: ')
	port = int(input('Enter port: '))
	server = (target,port)
	print(f'Attempting to connect to server...\n')
	server_connect(server)
	
main()
