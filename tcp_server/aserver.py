import asyncio

HEARTBEAT_INTERVAL_SEC = 1.0

async def heartbeat(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    client = writer.get_extra_info('peername')
    print(f'New client {client} connected')

    while True:
        writer.write(b'Heartbeat... ')
        await writer.drain()
        await asyncio.sleep(HEARTBEAT_INTERVAL_SEC)


async def new_server(address: str, port: int):
    server =  await asyncio.start_server(heartbeat, address, port)
    #server.sockets[0].
    ip, port = server.sockets[0].getsockname()
    print(f'Listening on {ip}:{port}. Hit Ctrl+C to stop')
    await server.serve_forever()

try:
    asyncio.run(new_server('localhost', 5555))
except KeyboardInterrupt:
    print("\nShutdown server...")
