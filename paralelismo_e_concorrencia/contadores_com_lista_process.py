# def count(name: str, n: int, lst: list):
#     for i in range(n):
#         s = f'{name}: {i}'
#         lst.append(s)
from multiprocessing import Manager, Process, current_process
from random import randint
from time import sleep


def count(lst: list, n: int) -> None:
    for i in range(n):
        sleep(randint(1, 5) / 100)
        lst.append(f'{current_process().name}: {i}')


if __name__ == '__main__':
    n = 10
    n_process = 2
    manager = Manager()
    lst = manager.list()
    processes = [Process(target=count, args=[lst, n]) for _ in range(n_process)]

    for t in processes:
        t.start()
    for t in processes:
        t.join()
    for i in lst:
        print(i)
