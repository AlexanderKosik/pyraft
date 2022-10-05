import socketserver
import socket
import threading
import time

class HeartbeatRequestHandler(socketserver.BaseRequestHandler):
    def handle(self, *args):
        print("New client connected")
        try:
            while True:
                heartbeat = b'heartbeat... '
                self.request.send(heartbeat)
                time.sleep(1)
        except BrokenPipeError:
            print("Client disconnected")


class Server(socketserver.ForkingTCPServer):
    def __init__(self, address, requestHandler):
        socketserver.ForkingTCPServer.__init__(self, address, requestHandler)
        self.allow_reuse_address = True


addresses = [
        ('localhost', 20_001), 
        ('localhost', 20_002), 
        ]


servers = {}
for ip, port in addresses:
    t = threading.Thread(target=Server((ip, port), HeartbeatRequestHandler).serve_forever)
    t.start()
    servers[(ip, port)] = t
    print(f"Server loop running on port {port}")
# todo: cleanup and close threads on ctrl+c
