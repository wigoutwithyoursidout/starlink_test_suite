# client/network_tools.py
import subprocess

def run_ping(host='8.8.8.8', count=10):
    cmd = ['ping', '-n', str(count), host]  # Windows syntax
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)

def run_iperf3(server_ip='127.0.0.1'):
    cmd = ['iperf3', '-c', server_ip]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)

if __name__ == '__main__':
    run_ping('google.com')
    run_iperf3('<YOUR_IPERF3_SERVER>')