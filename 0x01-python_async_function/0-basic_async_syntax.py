#!/usr/bin/env python3
"""
learning python async
"""

import random
import asyncio


async def wait_random(max_delay=10):
    """
    generates a random float which is used to
      to pause execution of the couroutine
    """
    max_delay = random.uniform(0, 10)
    await asyncio.sleep(max_delay)
    return max_delay
