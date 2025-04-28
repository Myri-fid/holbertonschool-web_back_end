#!/usr/bin/env python3

from typing import AsyncGenerator
from typing import List
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """coroutine called async_generator that takes no arguments."""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension() -> List[float]:
    """coroutine will collect 10 random numbers"""

    return [num async for num in async_generator()]
