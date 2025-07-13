# logger.py
import csv  # For writing CSV rows
import uuid  # For generating unique session IDs
import os  # For checking if the CSV already exists
from datetime import datetime  # For timestamps
from zoneinfo import ZoneInfo

class Logger:
    def __init__(self, filepath='../results/metrics.csv'):
        # Filepath to store logs
        self.filepath = filepath

        # Generate a unique session ID for this test run
        self.session_id = str(uuid.uuid4())

        # If the file does not exist, write the CSV header
        file_exists = os.path.isfile(self.filepath)
        if not file_exists:
            with open(self.filepath, 'w', newline='') as f:
                writer = csv.DictWriter(
                    f, fieldnames=['timestamp', 'session_id', 'test_type',
                                   'latency_ms', 'iperf3_output'])
                writer.writeheader()

    def log(self, data: dict):
        """Add a row to the CSV with timestamp, session ID, and test data"""
        data_out = {
            'timestamp': datetime.now(ZoneInfo("Australia/Sydney")).isoformat(),
            'session_id': self.session_id,
            **data  # Add the test data keys (latency or throughput)
        }
        # Write the row to the CSV file
        with open(self.filepath, 'a', newline='') as f:
            writer = csv.DictWriter(
                f, fieldnames=['timestamp', 'session_id', 'test_type',
                               'latency_ms', 'iperf3_output'])
            writer.writerow(data_out)