import threading
from concurrent.futures import ThreadPoolExecutor

def worker(n):
    print('Thread {n} is working')


with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(worker,i) for i in range(10)]

# thread = threading.Thread(target=worker)
# thread.start()
# thread.join()
