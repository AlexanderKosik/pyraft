import socketserver
import socket
import threading

class NewClientRequestHandler(socketserver.BaseRequestHandler):
    def handle(self, *args):
        print("New client connected")
        while True:
            msg = self.request.recv(1024)
            print("Got:", msg)

class Server(socketserver.ForkingTCPServer):
    def __init__(self, address, requestHandler):
        super().__init__(address, requestHandler)
        self.allow_reuse_address = True


addresses = [
        ('localhost', 20_001), 
        ('localhost', 20_002), 
        ]

for ip, port in addresses:
    threading.Thread(target=Server((ip, port), NewClientRequestHandler).serve_forever).start()
    # t.setDaemon(True)
    print(f"Server loop running in port {port}")


# todo: store threads in data structure

# todo: cleanup and close threads on ctrl+c
