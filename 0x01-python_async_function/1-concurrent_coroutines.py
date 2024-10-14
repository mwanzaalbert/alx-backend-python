#!/usr/bin/env python3
"""
Spawn wait_random n times with the specified max_delay.

Return the list of delays in ascending order.
"""
import asyncio
from typing import List

# Import the wait_random function
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Return the list of delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        # Insert the delay in the correct order
        if not delays or delay >= delays[-1]:
            delays.append(delay)
        else:
            for i, d in enumerate(delays):
                if delay < d:
                    delays.insert(i, delay)
                    break
    return delays


async def wait_n2(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Return the list of delays in ascending order.
    """
    # Create a list of tasks to run concurrently
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Gather all results concurrently
    delays = await asyncio.gather(*tasks)

    # Return the delays in ascending order
    return sorted(delays)


if __name__ == "__main__":
    '''Test file for printing the correct output of the wait_n coroutine.'''
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
    print()
    print(asyncio.run(wait_n2(5, 5)))
    print(asyncio.run(wait_n2(10, 7)))
    print(asyncio.run(wait_n2(10, 0)))
