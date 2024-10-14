#!/usr/bin/env python3
"""
Return an asyncio.Task.

that runs wait_random with the given max_delay.
"""
import asyncio

# Import the wait_random function
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Return an asyncio.Task.

    that runs wait_random with the given max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    async def test(max_delay: int) -> float:
        """Check if task is an asyncio.Task."""
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
