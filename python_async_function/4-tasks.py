#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""
import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that takes in an integer argument"""

    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """task_wait_random that takes an integer max_delay
    and returns a asyncio.Task"""

    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random"""

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
