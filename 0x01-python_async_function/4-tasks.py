#!/usr/bin/env python3
"""
Spawn task_wait_random n times with the specified max_delay.

Returns the list of delays in ascending order.
"""
import asyncio
from typing import List

# Import task_wait_random from the previous file
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay.

    Returns the list of delays in ascending order.
    """
    # Create list of tasks using task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Gather results of the tasks
    delays = await asyncio.gather(*tasks)

    # Return delays in ascending order
    return sorted(delays)


if __name__ == "__main__":
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
