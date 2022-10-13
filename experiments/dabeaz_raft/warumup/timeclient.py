from socket import socket, AF_INET, SOCK_STREAM

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 20_001))
msg = sock.recv(1024)
print("Got", msg)
