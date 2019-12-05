import asyncio


async def foo():
    while True:
        await asyncio.sleep(2)
        print('foo')


async def bar():
    while True:
        await asyncio.sleep(3)
        print('bar')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(foo())
    loop.create_task(bar())
    loop.run_forever()
