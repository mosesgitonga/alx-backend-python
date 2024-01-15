#!/usr/bin/env python3
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random

"""
 execute multiple coroutines
"""


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    call the wait_random and return random wait time 'n' times
    """

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
