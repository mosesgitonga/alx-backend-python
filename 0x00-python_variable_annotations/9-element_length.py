#!/usr/bin/env python3
"""
element length
"""
from typing import List, Tuple, Sequence


def element_length(lst: List[str]) -> List[Tuple[Sequence, int]]:
    """
    find element length
    """
    return [(i, len(i)) for i in lst]