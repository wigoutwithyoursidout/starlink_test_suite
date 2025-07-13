# client/client_ws.py
import asyncio
import websockets
import time
from metrics import calculate_latency
from logger import log_metrics

SERVER_URI = 'ws://<YOUR_SERVER_IP>:8765'

async def listen():
    async with websockets.connect(SERVER_URI) as websocket:
        while True:
            start = time.time()
            msg = await websocket.recv()
            latency_ms = calculate_latency(start, time.time())
            log_metrics('ws', latency_ms)
            print(f"[WS] Latency: {latency_ms:.2f} ms")

asyncio.run(listen())