#!/usr/bin/env python3
import asyncio
import random
from typing import List, Generator
"""
program to create an async generator
"""


async def async_generator() -> Generator[float, None, None]:
    """
    return a list of random nums
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
