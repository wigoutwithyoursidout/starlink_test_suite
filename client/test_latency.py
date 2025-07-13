# client/test_latency.py
import subprocess
import re
from logger import Logger

def run_ping(server_ip, count=10):
    """Run a simple ping test"""
    cmd = ["ping", "-c", str(count), server_ip]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Ping failed: {result.stderr}")
        return None
    return result.stdout

def parse_and_log_ping_output(ping_output, logger):
    """
    Extracts and logs latency for each individual ping.
    Example line: 64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=14.2 ms
    """
    for line in ping_output.splitlines():
        match = re.search(r'time=([\d\.]+) ms', line)
        if match:
            latency_ms = float(match.group(1))
            logger.log("latency_ms", latency_ms)

def run_latency_test(server_ip, count=10):
    logger = Logger()
    ping_output = run_ping(server_ip, count)
    if ping_output:
        parse_and_log_ping_output(ping_output, logger)

if __name__ == "__main__":
    run_latency_test("YOUR_SERVER_IP", count=10)