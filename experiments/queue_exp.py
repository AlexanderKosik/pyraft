from queue import Queue
import threading
import random
import time

q = Queue()

def produce():
    while True:
        random_number = random.randint(0, 99)
        q.put(random_number)
        print(f"{threading.current_thread().name}: add {random_number} to queue")
        time.sleep(random.random())

    

def consume():
    while True:
        while q.empty() is False:
            number = q.get()
            print(f"{threading.current_thread().name}: consuming {number} from queue")
        time.sleep(5)

threading.Thread(target=produce).start()
threading.Thread(target=produce).start()
threading.Thread(target=produce).start()

threading.Thread(target=consume).start()

