from environment import read_setup

class Communication:
    """
    Keeps connections to all known servers
    """
    def __init__(self, setup_filename="setup.cfg"):
        servers = read_setup(setup_filename)


    def request_vote(self):
        pass
