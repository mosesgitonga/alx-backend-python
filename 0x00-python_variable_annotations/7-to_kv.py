#!/usr/bin/env python3
"""
complex types
"""
from typing import Union, Tuple


def to_kv(k: str = '1', v: Union[int, float] = 1) -> Tuple[str, float]:
    """
    complex types
    """
    v = v ** 2
    return (k, v)
