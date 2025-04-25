#!/usr/bin/env python3
""". The list of the delays should be in
ascending order without using sort()"""
import asyncio
from typing import List
import random
import time


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


def measure_time(n: int, max_delay: int) -> float:
    """module to measure an approximate elapsed time."""

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
