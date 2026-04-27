# 15.1
import multiprocessing
import random
import time
from datetime import datetime

def worker():
    wait_time = random.random()   # random float between 0 and 1
    time.sleep(wait_time)
    print("Process finished at:", datetime.now().time())

if __name__ == "__main__":
    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=worker)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes completed.")