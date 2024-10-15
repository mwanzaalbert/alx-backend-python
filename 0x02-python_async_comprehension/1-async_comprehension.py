#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
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
