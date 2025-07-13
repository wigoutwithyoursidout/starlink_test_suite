# client/test_latency.py
import requests
import time
from logger import Logger

def run_http_ping(server_url, count=10):
    """Send HTTP GET requests to the /ping endpoint and measure latency."""
    logger = Logger()
    
    for i in range(count):
        try:
            start_time = time.time()
            response = requests.get(f"{server_url}", timeout=5)
            end_time = time.time()

            if response.status_code == 200:
                round_trip_ms = (end_time - start_time) * 1000
                data = response.json()
                server_timestamp = data.get('server_timestamp')

                print(f"Ping {i+1}: {round_trip_ms:.2f} ms | server_timestamp: {server_timestamp}")
                logger.log("http_latency_ms", round_trip_ms)
            else:
                print(f"Ping {i+1}: HTTP {response.status_code}")

        except requests.RequestException as e:
            print(f"Ping {i+1}: Request failed - {e}")

        # Add 5-second delay before the next request
        if i < count - 1:
            time.sleep(5)

if __name__ == "__main__":
    # Example: http://127.0.0.1:8000 if running locally
    run_http_ping("http://127.0.0.1:8000/ping", count=10)