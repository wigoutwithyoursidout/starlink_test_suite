# client/metrics.py
def calculate_latency(start_time, end_time):
    """Returns latency in ms"""
    return (end_time - start_time) * 1000

# Add jitter, throughput calc if needed