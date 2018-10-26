from multiprocessing import JoinableQueue, current_process
from multiprocessing.context import Process


def produce(q: JoinableQueue, n: int):
    for i in range(n):
        q.put(f'{current_process().name}: {i}')


def consume(q: JoinableQueue):
    while True:
        i = q.get()
        print(f'{current_process().name} - {i}')
        q.task_done()


if __name__ == '__main__':
    n_producers = 2
    n_consumers = 1
    n_tasks = 100
    q = JoinableQueue()
    producers = [Process(target=produce, args=[q, n_tasks]) for _ in range(n_producers)]
    consumers = [Process(target=consume, args=[q]) for _ in range(n_consumers)]

    for p in producers:
        p.start()
    for p in consumers:
        p.start()
    for p in producers:
        p.join()
    q.join()
    for p in consumers:
        p.terminate()
