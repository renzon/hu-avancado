from threading import Thread
from time import sleep, time


def contador(nome, n):
    # sleep(n/100)
    for i in range(n):
        print(nome, i)


if __name__ == '__main__':
    print('Criando Processos')
    n = 100
    n_processos = 2
    elapsed = time()
    # for i in range(n_processos):
    #     contador(f'Serial {i}:', n)
    serial_elapsed = time() - elapsed
    processos = [
        Thread(target=contador, args=[f'Processo {i}:', n])
        for i in range(n_processos)
    ]

    elapsed = time()
    for p in processos:
        p.start()
    for p in processos:
        p.join()

    print('Serial', serial_elapsed)
    print('Processo', time() - elapsed)
    print('Fim')
