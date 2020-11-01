"""
asyncio有两种high level的服务器写法，一种是基于回调，另外一种是基于stream，但是后者性能更低。
我们先介绍一种流的方式，我们会使用python3.7的serve_forever特性。
"""
import asyncio

async def echo_server(reader, writer):
    while True:
        data = await reader.read(100)  # 每次读取的最大字节
        if not data:
            break
        writer.write(data)
        await writer.drain()  # 流控制
        print(data)
    writer.close()

async def main(host, port):
    server = await asyncio.start_server(echo_server, host, port)
    await server.serve_forever()

asyncio.run(main('127.0.0.1', 4002))
