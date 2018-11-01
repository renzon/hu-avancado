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


async def download_all_flags():
    futures = [download(country) for country in generate_countries()]
    r = await asyncio.wait(futures)
    print(r)
    return 'Final'


if __name__ == '__main__':
    elapsed = time()
    future = download_all_flags()
    asyncio.run(future)
    print(f'Total time: {time()-elapsed}s')
