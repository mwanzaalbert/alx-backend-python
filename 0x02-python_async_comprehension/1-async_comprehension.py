#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for asynchronous random number collection.

This module defines a coroutine that collects random float numbers
between 0 and 10 using an asynchronous comprehension over a previously
defined asynchronous generator.

Functions:
-----------
- async_comprehension: Collects 10 random float numbers using
  an asynchronous comprehension over the async_generator.

Usage:
------
To execute the module, run it as a standalone script. The collected
random numbers will be printed to the console.

Example:
-------
$ python3 your_module_name.py

Created on Tue Oct 15 13:45:17 2024.

@author: AM
"""
import asyncio
from typing import List

# Import async_generator from the previous task
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehension.

    over async_generator.
    """
    return [i async for i in async_generator()]


async def main() -> None:
    """Entry Point."""
    print(await async_comprehension())


if __name__ == "__main__":
    asyncio.run(main())
