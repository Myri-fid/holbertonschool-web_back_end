#!/usr/bin/env python3
""". The list of the delays should be in ascending order without using sort()"""
import asyncio
from typing import List
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """. The list of the delays should be in ascending order without using sort()"""

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for completed in asyncio.as_completed(tasks):
        result = await completed
        delays.append(result)
    return delays
