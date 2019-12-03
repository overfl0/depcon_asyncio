from time import time

from without_asyncio import main
from with_asyncio import main_asyncio

if __name__ == '__main__':
    start = time()
    print('started without asyncio...')
    main()
    print(f'finished in {time() - start} s')

    start = time()
    print('started with asyncio...')
    main_asyncio()
    print(f'finished in {time() - start} s')
