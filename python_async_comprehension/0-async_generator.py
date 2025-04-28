#!/usr/bin/env python3
"""coroutine called async_generator that takes no arguments."""
from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[int, None]:
    """coroutine called async_generator that takes no arguments."""

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
