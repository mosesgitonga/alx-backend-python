#!/usr/bin/env python3
"""
complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make multiplier
    """
    def multiplier_function(x: float) -> float:
        """
        multiplier
        """
        return x * multiplier

    return multiplier_function
