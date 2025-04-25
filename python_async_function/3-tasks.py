#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that takes in an integer argument"""

    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """task_wait_random that takes an integer max_delay
    and returns a asyncio.Task"""

    return asyncio.create_task(wait_random(max_delay))
