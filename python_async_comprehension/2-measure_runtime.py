#!/usr/bin/env python3
"""coroutine called async_generator that takes no arguments."""
from typing import List
import asyncio
import time
import random


async def async_generator():
    """coroutine called async_generator that takes no arguments."""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension() -> List[float]:
    """coroutine will collect 10 random numbers"""

    return [num async for num in async_generator()]


async def measure_runtime():
    """should measure the total runtime and return it."""

    start_time = time.time()
    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
