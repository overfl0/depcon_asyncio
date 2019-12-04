import asyncio
import aiohttp

from common import links_wl


async def count_words(text):
    wordcount = {}
    for word in text.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1


async def download_file(link):
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resp:
            data = await resp.text()
            asyncio.create_task(count_words(data))


async def foo():
    await asyncio.gather(*(download_file(link) for link in links_wl))


def main_asyncio():
    asyncio.run(foo())
