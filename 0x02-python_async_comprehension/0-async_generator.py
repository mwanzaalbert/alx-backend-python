#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module for asynchronous random number generation.

This module contains an asynchronous generator that yields random float
numbers between 0 and 10. It includes a coroutine to print the generated
numbers after a specified delay.

Functions:
-----------
- async_generator: Asynchronously generates 10 random float numbers
  between 0 and 10, waiting 1 second between each number.

- print_yielded_values: Collects and prints the values yielded by
  the async_generator.

Usage:
------
To execute the module, run it as a standalone script. The generated
random numbers will be printed to the console.

Example:
--------
$ python3 your_module_name.py


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
