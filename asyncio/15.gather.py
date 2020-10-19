import asyncio

async def myWorker(number):
    print(number * 2)

async def main():
    print("My Main")

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*[myWorker(i) for i in range(5)]))
except KeyboardInterrupt:
    pass
finally:
    loop.close()