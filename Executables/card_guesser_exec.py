import asyncio
import websockets

from Executables import config
from Library.CardGuesser import CardGuesser


async def start():
    uri = "ws://{0}:{1}".format(host,port)
    async with websockets.connect(uri) as websocket:
        card_guesser = CardGuesser(websocket)
        await card_guesser.start_game()

host = config.host
port = config.port

asyncio.get_event_loop().run_until_complete(start())
