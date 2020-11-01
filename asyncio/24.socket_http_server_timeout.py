"""
the server should timeout an idle connection, that is wait a certain length of time
for the client to do something and then close the connection if it doesn’t
"""

import asyncio

TIMEOUT = 1  # Second

class TimeoutServer(asyncio.Protocol):
    def __init__(self):
        loop = asyncio.get_running_loop()
        self.timeout_handle = loop.call_later(
            TIMEOUT, self._timeout,
        )

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        self.timeout_handle.cancel()

    def _timeout(self):
        self.transport.close()
