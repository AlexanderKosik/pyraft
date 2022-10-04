from environment import read_setup
import asyncio

async def client_connected_cb(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    client = writer.get_extra_info('peername')
    print(f'New client {client} connected')


async def new_server(address: str, port: int):
    server =  await asyncio.start_server(client_connected_cb, address, port)
    ip, port = server.sockets[0].getsockname()
    print(f'Listening on {ip}:{port}. Hit Ctrl+C to stop')
    await server.serve_forever()

try:
    asyncio.run(new_server('localhost', 5555))
except KeyboardInterrupt:
    print("\nShutdown server...")

class Communication:
    """
    Keeps connections to all known servers
    """
    port_base = 5555
    def __init__(self, setup_filename="setup.cfg"):
        try:
            asyncio.run(new_server('localhost', port_base))
            port_base += 1
        except KeyboardInterrupt:
            print("\nShutdown server...")
        # servers = read_setup(setup_filename)


    def request_vote(self):
        pass

c = Communication()
c_2 = Communication()
