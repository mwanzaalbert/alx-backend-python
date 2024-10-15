#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:34:17 2024.

@author: AM
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates 10 random numbers between 0 and 10.

    waiting 1 second between each.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10


if __name__ == "__main__":
    async def print_yielded_values():
        """Execute Asynchronous Generator."""
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
