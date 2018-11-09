from dis import dis
from functools import partial
from time import time


def hello() -> str:
    'Retorna hello'
    # for i in range(10):
    #     print(i)
    return 'Hello'


print(dir(hello))
print(hello.__doc__)
hello.foo = 'blah'
print(hello.foo)
print(help(hello))
print(hello.__code__.co_code)
print(dis(hello.__code__.co_code))

ola = hello

# hello = 1

print(ola())
print(ola.__name__)


def medidor_de_tempo(fcn, *args, **kwargs):
    inicio = time()
    for _ in range(10):
        print(fcn(*args, **kwargs))
    return (time() - inicio) / 10


print(medidor_de_tempo(hello))

hello2 = (lambda nome: f'Olá {nome}')

hello3 = partial(hello2, 'Renzo')

print(medidor_de_tempo(hello3))
print(medidor_de_tempo(hello3))
print(medidor_de_tempo(hello3))
print(medidor_de_tempo(hello3))
print(medidor_de_tempo(hello3))
print(medidor_de_tempo(hello3))


def n_execucao(n=3):
    def f():
        nonlocal n
        n = n+ 1

    print(n)
    f()
    print(n)

    return f


f_global = n_execucao()
print(f_global())
print(f_global.__closure__)
