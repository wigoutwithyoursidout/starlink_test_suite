import subprocess
import json
from logger import Logger

def run_iperf(server_ip, reverse=False):
    cmd = ["iperf3", "-c", server_ip, "-J"]  # -J = JSON output
    if reverse:
        cmd.append("-R")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"iperf3 failed: {result.stderr}")
        return None
    return json.loads(result.stdout)

def run_throughput_test(server_ip):
    logger = Logger()

    # 1. Upload test
    upload_data = run_iperf(server_ip)
    if upload_data:
        upload_bps = upload_data["end"]["sum_sent"]["bits_per_second"]
        logger.log("throughput_upload_bps", upload_bps)

    # 2. Download test
    download_data = run_iperf(server_ip, reverse=True)
    if download_data:
        download_bps = download_data["end"]["sum_received"]["bits_per_second"]
        logger.log("throughput_download_bps", download_bps)

if __name__ == "__main__":
    run_throughput_test("YOUR_SERVER_IP")