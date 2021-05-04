import concurrent.futures
import time
import uuid
import datetime


def task():
    time.sleep(1)
    return uuid.uuid4().hex


print(datetime.datetime.now())

queue = []
with concurrent.futures.ThreadPoolExecutor(max_workers=2_000) as pool:
    for i in range(20_000):
        queue.append(
            pool.submit(task)
        )

    concurrent.futures.wait(queue)

    for i in queue:
        print(i.result())

print(datetime.datetime.now())