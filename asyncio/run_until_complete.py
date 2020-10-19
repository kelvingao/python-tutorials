import asyncio
import time

# 定义一个协程
async def myWork():
    print("Starting Work")
    time.sleep(5)
    print("Finishing Work")


# 快速启动一个简单的事件循环，运行直至协程结束
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(myWork())
finally:
    loop.close()