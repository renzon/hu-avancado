import asyncio
from time import time

import aiohttp

from paralelismo_e_concorrencia.flags_serial import (flag_url, generate_countries, save_flag)


async def download(country):
    print('Comecando a executar future')
    async with aiohttp.ClientSession() as session:
        resp = await session.get(flag_url(country))
        if resp.status != 200:
            raise Exception('Flag not found')
        flag_bytes = await resp.read()
        return save_flag(flag_bytes, country)


def download_all_flags():
    futures = [download(country) for country in generate_countries()]
    loop = asyncio.get_event_loop()
    tasks = asyncio.gather(*futures, loop=loop, return_exceptions=True)
    results = loop.run_until_complete(tasks)
    for r in results:
        if isinstance(r, Exception):
            print('Tratamento de Exceção', r)
        else:
            yield r


if __name__ == '__main__':
    elapsed = time()
    for flag in download_all_flags():
        print(flag)

    print(f'Total time: {time()-elapsed}s')

# https://docs.python.org/3/library/asyncio-eventloop.html#id15
