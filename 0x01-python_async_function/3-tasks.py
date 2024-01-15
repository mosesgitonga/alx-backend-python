#!/usr/bin/env python3
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


"""
awaiting task
"""


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    creating task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
