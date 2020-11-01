"""
asyncio有两种high level的socket服务器写法，第二种是声明一种协议asyncio.Protocol。
"""
import asyncio

class EchoProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        self.transport.write(data)
        print(data)

async def main(host, port):
    loop = asyncio.get_running_loop()
    server = await loop.create_server(EchoProtocol, host, port)
    await server.serve_forever()

asyncio.run(main('127.0.0.1', 4002))
