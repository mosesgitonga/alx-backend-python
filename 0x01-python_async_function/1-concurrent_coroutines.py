#!/usr/bin/env python3
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
"""
 execute multiple coroutines
"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    call the wait_random and return random wait time 'n' times
    """

    mylist = []
    for _ in range(n):
        res = await wait_random(max_delay)
        mylist.append(res)

    return sorted(mylist)
