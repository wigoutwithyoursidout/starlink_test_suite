# runner.py

import argparse
from client.test_latency import run_latency_test
from client.test_throughput import run_throughput_test
from client.traffic_generator_ import run_traffic_generator

    # python runner.py --test latency --server 10.0.2.15 --duration 30
    # python runner.py --test throughput --server 10.0.2.15
    # python runner.py --test traffic --server http://10.0.2.15:8000 --duration 30

def main():
    parser = argparse.ArgumentParser(description="Starlink Test Suite Runner")
    parser.add_argument("--test", required=True, choices=['latency', 'throughput', 'traffic'],
                        help="Which test to run")
    parser.add_argument("--server", required=True,
                        help="Server URL")
    parser.add_argument("--duration", type=int, default=30,
                        help="Duration in seconds")

    args = parser.parse_args()

    if args.test == "latency":
        run_latency_test(args.server, args.duration)
    elif args.test == "throughput":
        run_throughput_test(args.server, args.duration)
    elif args.test == "traffic":
        run_traffic_generator(args.server, args.duration)

if __name__ == "__main__":
    main()