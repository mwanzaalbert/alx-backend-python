#!/usr/bin/env python3
"""
Measure the total execution time for wait_n(n, max_delay).

Returns average time per coroutine.
"""
import time
import asyncio

# Import wait_n from the previous file
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay).

    Returns average time per coroutine.
    """
    start_time = time.perf_counter()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Run wait_n with asyncio
    end_time = time.perf_counter()  # Record the end time

    total_time = end_time - start_time  # Calculate total elapsed time
    return total_time / n  # Return the average time per coroutine


if __name__ == "__main__":
    n = 5
    max_delay = 9

    print(measure_time(n, max_delay))
