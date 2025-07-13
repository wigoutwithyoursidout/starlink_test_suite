# client/test_throughput.py

import subprocess
import json
import os
from datetime import datetime
from logger import Logger

def run_iperf(server_ip, reverse=False):
    """
    Run an iperf3 throughput test.
    If reverse=True, runs in reverse mode to test download.
    Returns JSON output as a Python dict.
    """
    cmd = ["iperf3", "-c", server_ip, "-J"]  # -c = client mode, -J = JSON output
    if reverse:
        cmd.append("-R")  # Reverse mode: server sends to client (download)

    # Run the iperf3 command and capture its output
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"iperf3 failed: {result.stderr}")
        return None

    # Parse the JSON output string into a Python dict
    return json.loads(result.stdout)

def save_json(data, direction):
    """
    Save the full iperf3 JSON result to a timestamped file.
    This keeps raw interval data separate from summary CSV logs.
    """
    # Format timestamp for filename
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    # Make sure the directory exists
    os.makedirs("../results/iperf3", exist_ok=True)

    # Create filename with test direction (upload or download)
    filename = f"../results/iperf3/iperf3_{direction}_{timestamp}.json"

    # Write JSON data to file
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"[+] Saved iperf3 {direction} data to {filename}")

def run_throughput_test(server_ip):
    """
    Run both upload and download throughput tests.
    Log summary results to CSV and save raw JSON.
    """
    logger = Logger()

    # ----------- Upload Test -----------
    upload_data = run_iperf(server_ip)
    if upload_data:
        # Extract upload bits per second from JSON
        upload_bps = upload_data["end"]["sum_sent"]["bits_per_second"]

        # Log summary to CSV
        logger.log({
            "test_type": "throughput_upload",
            "throughput_bps": upload_bps
        })

        # Save full JSON output
        save_json(upload_data, direction="upload")

    # ----------- Download Test -----------
    download_data = run_iperf(server_ip, reverse=True)
    if download_data:
        # Extract download bits per second from JSON
        download_bps = download_data["end"]["sum_received"]["bits_per_second"]

        # Log summary to CSV
        logger.log({
            "test_type": "throughput_download",
            "throughput_bps": download_bps
        })

        # Save full JSON output
        save_json(download_data, direction="download")

if __name__ == "__main__":
    # Replace YOUR_SERVER_IP with your actual server IP or use argparse
    run_throughput_test("YOUR_SERVER_IP")
