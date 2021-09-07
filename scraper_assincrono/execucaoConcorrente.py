## modelo retirado conforme aula online
## https://github.com/dunossauro
## vamos trabalhar assincrono com e processamento concorrente
import asyncio
from os.path import exists
from os import makedirs
from shutil import rmtree
from urllib.parse import urljoin
from aiohttp import ClientSession
from requests import get
from aiofiles import open as aopen


## estamos definindo no path uma pasta para download das imagens
path = 'downloads'
base_url = 'https://pokeapi.co/api/v2/' # endereço base da API
pokemons = get(urljoin(base_url, 'pokemon/?limit=100')).json()['results'] #limitando a 100 imagens


# verifica se a pasta downloads já existe
if exists(path):
    rmtree(path)
makedirs(path)

async def write_file(session, url, name):
    async with session.get(url) as response:
        print("Utilizando asyncio >> requisitando api do Pokemon limitado a 100 páginas /n")
        print(f'baixando {name} : {url[-6:-3]}')
        async with aopen(f'{path}/{name}.jpg', 'wb') as f:
            content = await response.content.read()
            await f.write(content)


async def fetch(sem, session, url, name):
    async with sem:
        async with session.get(url) as response:
            result = await response.json()
            sprite_url = result['sprites']['front_default']
            await write_file(session, sprite_url, name)


async def main():
    tasks = []
    sem = asyncio.Semaphore(100)

    async with ClientSession() as session:
        print("Iniciando a execução concorrente \n \n")
        for pokemon in pokemons:
            url = pokemon['url']
            name = pokemon['name']
            print(name, url)
            task = asyncio.ensure_future(fetch(sem, session, url, name))
            tasks.append(task)
        responses = asyncio.gather(*tasks)
        await responses


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(main())
loop.run_until_complete(future)
