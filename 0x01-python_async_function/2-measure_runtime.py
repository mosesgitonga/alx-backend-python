#!/usr/bin/env python3
from time import time

from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    start_time = time()

    run(wait_n(n, max_delay))

    end_time = time()

   

    return (end_time - start_time) / n