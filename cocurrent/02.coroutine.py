import asyncio
import time

async def foo():
    print('42')
    # time.sleep(1)
    await asyncio.sleep(1)
    print('1337')

async def main():
    await asyncio.gather(*[foo() for i in range(5)])

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print('Total Time: ' + str(end - start) + 's.')
