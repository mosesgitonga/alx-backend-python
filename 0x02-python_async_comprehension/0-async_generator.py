#!/usr/bin/env python3
import asyncio
import random
from typing import List, AsyncGenerator
"""
program to create an async generator
"""


async def async_generator() -> AsyncGenerator[float, None]:
    """
    return a list of random nums
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
