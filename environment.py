from typing import List, Tuple

def read_setup(filename: str) -> List[Tuple[str, int]]:
    servers = []
    with open(filename) as f:
        for line in f:
            if line.startswith("#"):
                continue

            ip, port = line.split()
            servers.append((ip, int(port)))

    return servers

