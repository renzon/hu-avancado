# def count(name: str, n: int, conjunto: list):
#     for i in range(n):
#         s = f'{name}: {i}'
#         conjunto.append(s)
from random import randint
from threading import Thread, current_thread
from time import sleep


class Counter(Thread):
    def __init__(self, lst, n):
        self.n = n
        self.lst = lst
        super().__init__()

    def run(self) -> None:
        for i in range(self.n):
            sleep(randint(1,5)/100)
            self.lst.append(f'{current_thread().getName()}: {i}')


if __name__ == '__main__':
    n = 10
    n_thread = 2
    lst = []
    threads = [Counter(lst, n) for _ in range(n_thread)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    for i in lst:
        print(i)
