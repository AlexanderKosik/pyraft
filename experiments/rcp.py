from typing import Tuple
import time
import pickle
import socket


class RCPServer:
    def __init__(self, address: Tuple):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(address)
        self.sock.listen(1)
        self.funcs = {}

    def register_function(self, func):
        self.funcs[func.__name__] = func

    def start(self):
        self.serve_forever()

    def serve_forever(self):
        while True:
            print("Waiting for connection...")
            try:
                client_sock, address = self.sock.accept()
                print("New client connected:", address)
                while True:
                    msg = client_sock.recv(1024)
                    if msg:
                        func, *args, kwargs = pickle.loads(msg)
                        result = self.funcs[func](*args, **kwargs)
                        client_sock.send(pickle.dumps(result))
                        client_sock.close()
                        break
                    else:
                        time.sleep(0.1)
            except KeyError:
                msg = pickle.dumps(Exception("Method not available"))
                client_sock.send(msg)
            except Exception as e:
                msg = pickle.dumps(e)
                self.socket.send(msg)

    def close(self):
        self.sock.close()


def add(x, y):
    return x+y

def sub(x, y):
    return x-y

try:
    s = RCPServer(('', 20_001))
    s.register_function(add)
    s.register_function(sub)

    s.serve_forever()
except KeyboardInterrupt:
    s.close()
    print("Goodbye!")

