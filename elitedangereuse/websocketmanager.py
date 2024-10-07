import asyncio

from thirdparty import websockets
from elitedangereuse.debug import Debug


class WebsocketManager:
    def __init__(self, elitedangereuse):
        self.elitedangereuse = elitedangereuse
        asyncio.get_event_loop().run_until_complete(self.hello())


    async def hello(self):
        try:
            async with websockets.connect("ws://localhost:8765") as websocket:
                await websocket.send("Hello World!")
                response = await websocket.recv()
                print(f"Received from server: {response}")

        except Exception as e:
            Debug.logger.info(f"Request failure: {str(e)}")
