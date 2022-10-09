import socket
import time
import pickle

address = 'localhost', 20_001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

msg = pickle.dumps(("add", 12, 3, {}))

send_bytes = s.send(msg)
print(f"{send_bytes} byte(s) sent")
print("Waiting for response...")

response = s.recv(1024)
while not response:
    time.sleep(0.1)
    response = s.recv(1024)

print(f"Received {len(response)} byte(s)")
result = pickle.loads(response)
print(result)

s.close()
