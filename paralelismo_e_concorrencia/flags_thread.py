from threading import Thread
from time import time

from paralelismo_e_concorrencia.flags_serial import (
    FlagNotFound, download_flag, generate_countries, save_flag,
)


def download_and_save(country):
    try:
        image = download_flag(country)
    except FlagNotFound:
        print(f'Flag not found: {country}')
    else:
        path = save_flag(image, country)
        print(path)


def download_all_flags():
    threads = [
        Thread(target=download_and_save, args=[country])
        for country in generate_countries()
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    elapsed = time()
    download_all_flags()
    print(f'Total time: {time()-elapsed}s')
