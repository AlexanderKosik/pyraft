# reads setup.cfg and instanciates server
from server import Server
from environment import read_setup


servers = read_setup("setup.cfg")
for server_id, (_, _) in enumerate(servers):
    s = Server(server_id)
    
    
