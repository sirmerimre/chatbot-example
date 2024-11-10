# rate_limiter.py
import time
from collections import defaultdict

# In-memory storage to track request timestamps per IP
request_timestamps = defaultdict(list)

def rate_limiter(ip_address, max_requests, time_window):
    """
    Checks if the IP address has exceeded the allowed request limit within the time window.
    Returns True if the request is allowed, False if rate-limited.
    """
    current_time = time.time()

    # Get the list of timestamps for the given IP address
    timestamps = request_timestamps[ip_address]

    # Remove timestamps outside the time window
    request_timestamps[ip_address] = [t for t in timestamps if t > current_time - time_window]

    # If the number of requests exceeds the limit, deny the request
    if len(request_timestamps[ip_address]) >= max_requests:
        return False

    # Otherwise, add the current timestamp and allow the request
    request_timestamps[ip_address].append(current_time)
    return True
