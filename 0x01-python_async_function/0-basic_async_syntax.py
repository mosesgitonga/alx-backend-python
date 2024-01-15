#!/usr/bin/env python3
"""
Learning Python Async

This script demonstrates the use of Python's asyncio
     module for asynchronous programming.
Usage:
- Modify the max_delay parameter in wait_random() to adjust
     the range of random float.

Example:
    wait_time = await wait_random()
    print(f"Coroutine paused for {wait_time:.2f} seconds.")
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Generates a random float and pauses the execution of
        the coroutine.

    Parameters:
    - max_delay (float): The upper limit for
        the random float (default is 10).

    Returns:
    - float: The duration of the sleep, representing
        the random float.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return max_delay
