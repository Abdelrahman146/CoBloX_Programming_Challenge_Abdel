import asyncio
import websockets

from Executables import config
from Library.CardPicker import CardPicker


async def start(websocket, path):
    card_picker = CardPicker(websocket)
    await card_picker.start_game()

host = config.host
port = config.port
start_server = websockets.serve(start, host, port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
