#!/usr/bin/env python3
import asyncio
from typing import AsyncGenerator, List
"""
async coprehension
"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    corutine for async comprehension
    """
    res = [i for i in async_generator()]
    return res
