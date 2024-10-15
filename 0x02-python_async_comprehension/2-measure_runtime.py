#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:59:11 2024.

@author: AM
"""

import asyncio
import time

# Import async_comprehension from the previous task
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel.

    and measure the total runtime.
    """
    start_time: float = time.perf_counter()  # Start the timer

    # Run 4 instances of async_comprehension in parallel using asyncio.gather
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time: float = time.perf_counter()  # End the timer

    total_runtime: float = end_time - start_time  # Calculate total runtime
    return total_runtime


async def main() -> None:
    """Entry Point."""
    print(await measure_runtime())


if __name__ == "__main__":
    asyncio.run(main())
