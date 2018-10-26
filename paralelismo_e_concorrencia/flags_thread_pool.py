from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor
from time import time

from paralelismo_e_concorrencia.flags_serial import (
    FlagNotFound, download_flag, generate_countries, save_flag,
)


def download_and_save(country):
    try:
        image = download_flag(country)
    except FlagNotFound:
        return f'Flag not found: {country}'
    else:
        path = save_flag(image, country)
        return path


def download_all_flags():
    with ProcessPoolExecutor() as executor:
        yield from executor.map(download_and_save, generate_countries(), chunksize=4)


if __name__ == '__main__':
    elapsed = time()
    for result in download_all_flags():
        print(result)
    print(f'Total time: {time()-elapsed}s')
