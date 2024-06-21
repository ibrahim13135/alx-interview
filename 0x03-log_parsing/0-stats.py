#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics:
- Total file size
- Number of lines by status code
"""
import sys

def print_stats(total_size, status_counts):
    """
    Print the computed statistics
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
        except (ValueError, IndexError):
            continue

        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise

print_stats(total_size, status_counts)
