import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('', 20_001)

sock.bind(address)
sock.listen(1)

try:
    client_socket, address = sock.accept()
    print(f"Got new connection from {address}")
    while True:
        msg = client_socket.recv(2)
        if msg:
            print("Received:", len(msg), "bytes")
            client_socket.send(msg)
        else:
            time.sleep(.1)
except KeyboardInterrupt as done:
    print("Exiting...")
except Exception as e:
    print(e)
finally:
    print("Clean up")
    sock.close()
