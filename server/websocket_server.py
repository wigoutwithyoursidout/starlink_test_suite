# server/websocket_server.py
import asyncio
import websockets
from datetime import datetime

async def handler(websocket, path):
    while True:
        msg = {
            'server_timestamp': datetime.utcnow().isoformat() + 'Z'
        }
        await websocket.send(str(msg))
        await asyncio.sleep(1)  # send every 1 sec

start_server = websockets.serve(handler, '0.0.0.0', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()