import sys
import signal

# Initialize global variables
total_file_size = 0
status_codes_count = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0

def print_statistics():
    """Prints total file size and status codes count in ascending order."""
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_codes_count):
        if status_codes_count[status_code] > 0:
            print(f"{status_code}: {status_codes_count[status_code]}")

def handle_interrupt(sig, frame):
    """Handles the keyboard interrupt (CTRL + C)."""
    print_statistics()
    sys.exit(0)

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line_count += 1

        # Parse the line format <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
        parts = line.split()
        if len(parts) >= 7 and parts[-2].isdigit() and parts[-1].isdigit():
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update total file size
            total_file_size += file_size

            # Update the status code count if it's a known status code
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except Exception as e:
    sys.stderr.write(f"Error: {e}\n")

if __name__ == '__main__':
    print_statistics()
