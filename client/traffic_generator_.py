# client/traffic_generator.py

import requests
import time

def run_traffic_generator(server_url, duration_sec):
    start = time.time()
    while time.time() - start < duration_sec:
        try:
            requests.get(server_url)
            print("Traffic sent")
        except Exception as e:
            print(f"Traffic gen error: {e}")
        time.sleep(0.1)

if __name__ == "__main__":
    run_traffic_generator("http://127.0.0.1:8000/ping", 30)