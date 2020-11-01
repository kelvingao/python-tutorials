"""
In the initial echo server example we had await writer.drain() as this paused the coroutine from writing more data to the socket
till the client had caught up, it drained the socket. This is useful as until the client catches up the data will be stored in memory,
hence a malicious client can make many requests for a lot of data, refuse to receive the data, and allow the server to exhaust its memory.

This is really all there is with respect to asyncio to build an ASGI server. To continue you’ll need to add pipelining,
ASGI constructs, the request-body, and streaming as completed in the Hypercorn h11.py file.
See also the h2, and wsproto libraries for the HTTP/2 and Websocket equivalents of h11.
"""

import asyncio

class FlowControlServer(asyncio.Protocol):
    def __init__(self):
        self._can_write = asyncio.Event()
        self._can_write.set()

    def pause_writing(self) -> None:
        # 当传输超过了警戒线的时候，会被调用
        self._can_write.clear()

    def resume_writing(self) -> None:
        # 传输掉入警戒线以下的时候，会被调用
        self._can_write.set()

    async def drain(self) -> None:
        await self._can_write.wait()
