from socket import AF_INET, SOCK_STREAM, socket
import time

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 20_001))
sock.listen()

while True:
    print("Waiting for new connection...")
    client, addr = sock.accept()
    print("Client connected!")
    curr_time = time.ctime()
    client.send(curr_time.encode('utf-8'))
