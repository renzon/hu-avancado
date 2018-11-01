"""
>>> dict(contagem('banana').items())
{'b': 1, 'a': 3, 'n': 2}
>>> dict(contagem('maça').items())
{'m': 1, 'a': 2, 'ç': 1}
"""


def contagem(caracteres: str):
    resultado = {}
    for c in caracteres:
        resultado[c] = caracteres.count(c)
    return resultado
