#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:34:17 2024.

@author: AM
"""

import asyncio
import random
from typing import AsyncGenerator, List


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates 10 random numbers between 0 and 10.

    It waits 1 second between each number.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10


async def print_yielded_values() -> None:
    """Collect and print the values yielded by the async_generator."""
    result: List[float] = []
    async for i in async_generator():
        result.append(i)
    print(result)


if __name__ == "__main__":
    asyncio.run(print_yielded_values())
