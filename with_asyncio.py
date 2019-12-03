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
    for link in links_wl:
        asyncio.create_task(download_file(link))


def main_asyncio():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(foo())
