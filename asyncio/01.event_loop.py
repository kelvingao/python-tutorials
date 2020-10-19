import asyncio

# 定义一个协程，以便将来调用
async def myCoroutine():
    print('My Coroutine')


# 快速启动一个简单的事件循环，运行直至协程结束
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(myCoroutine())
finally:
    loop.close()