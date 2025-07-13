# client/traffic_generator_.py

import requests
import time
from logger import Logger

def run_traffic_generator(server_url, duration_sec):
    """
    Send continuous HTTP GET requests to the /ping endpoint for a given duration.
    Measure and log round-trip latency for each request.
    """
    logger = Logger()

    start = time.time()
    count = 0

    while time.time() - start < duration_sec:
        count += 1
        try:
            req_start = time.time()
            response = requests.get(server_url, timeout=5)
            req_end = time.time()

            round_trip_ms = (req_end - req_start) * 1000

            if response.status_code == 200:
                data = response.json()
                server_timestamp = data.get('server_timestamp')

                print(f"Request {count}: {round_trip_ms:.2f} ms | server_timestamp: {server_timestamp}")
                logger.log("http_latency_ms", round_trip_ms)
            else:
                print(f"Request {count}: HTTP {response.status_code}")

        except requests.RequestException as e:
            print(f"Request {count}: Request failed - {e}")

        # Small delay to control request rate (optional)
        time.sleep(0.1)

if __name__ == "__main__":
    run_traffic_generator("http://127.0.0.1:8000/ping", duration_sec=30)