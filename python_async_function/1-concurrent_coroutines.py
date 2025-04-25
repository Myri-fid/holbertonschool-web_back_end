#!/usr/bin/env python3
""". The list of the delays should be in
ascending order without using sort()"""
import asyncio
from typing import List
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that takes in an integer argument"""

    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """. The list of the delays should be
    in ascending order without using sort()"""

    tasks = [wait_random(max_delay) for i in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    return delays
