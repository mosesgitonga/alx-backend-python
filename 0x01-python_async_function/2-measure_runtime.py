#!/usr/bin/env python3
from time import time
from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n
"""
measure time
"""


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the time taken for the asynchronous coroutine wait_n
    to complete 'n' times with the specified 'max_delay'.

    Parameters:
    - n (int): The number of times to run the wait_n coroutine.
    - max_delay (int): The maximum delay for the wait_n coroutine.

    Returns:
    - float: The average time taken for each iteration of the wait_n coroutine.
    """
    start_time = time()

    run(wait_n(n, max_delay))

    end_time = time()

    return (end_time - start_time) / n
