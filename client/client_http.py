# client/client_http.py
import requests
import time
from datetime import datetime
from metrics import calculate_latency
from logger import log_metrics

SERVER_URL = 'http://<YOUR_SERVER_IP>:8000/ping'

while True:
    start = time.time()
    try:
        r = requests.get(SERVER_URL, timeout=5)
        r.raise_for_status()
        server_timestamp = r.json()['server_timestamp']
        latency_ms = calculate_latency(start, time.time())
        log_metrics('http', latency_ms)
        print(f"[HTTP] Latency: {latency_ms:.2f} ms")
    except Exception as e:
        print(f"Request failed: {e}")
    time.sleep(1)