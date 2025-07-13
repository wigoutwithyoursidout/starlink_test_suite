# client/traffic_generator.py
import requests

def generate_load(server_url, duration_sec=30):
    """Sends multiple concurrent requests for a set time"""
    import time
    start = time.time()
    while time.time() - start < duration_sec:
        try:
            r = requests.get(server_url)
        except Exception as e:
            print(f"Load request failed: {e}")

if __name__ == '__main__':
    generate_load('http://<YOUR_SERVER_IP>:8000/ping')