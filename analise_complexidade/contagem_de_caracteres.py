"""
>>> dict(contagem('banana').items())
{'b': 1, 'a': 3, 'n': 2}
>>> dict(contagem('maça').items())
{'m': 1, 'a': 2, 'ç': 1}
"""
from bisect import bisect_right
from collections import Counter


def contagem(caracteres: str):
    return Counter(caracteres)


if __name__ == '__main__':
    lst = [1, 1] + list(range(2, 100))
    print(bisect_right(lst, 1))
