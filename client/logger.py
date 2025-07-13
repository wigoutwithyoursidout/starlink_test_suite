# client/logger.py
import csv
from datetime import datetime
import os

RESULTS_FILE = 'results/metrics.csv'

# Ensure results folder exists
os.makedirs('results', exist_ok=True)

def log_metrics(method, latency):
    file_exists = os.path.isfile(RESULTS_FILE)
    with open(RESULTS_FILE, mode='a', newline='') as csvfile:
        fieldnames = ['timestamp', 'method', 'latency_ms']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'method': method,
            'latency_ms': round(latency, 2)
        })