from communication import Communication

class Server:
    def __init__(self, server_id):
        self.current_term = 0
        self.voted_for = None
        self.log = []
        self.server_id = server_id
        # self.commit_index = 0
        # self.last_applied = 0

        self.communication = Communication()
        print(f"Server {self.server_id} up and runnig")

