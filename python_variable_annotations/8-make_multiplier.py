#!/usr/bin/env python3
from typing import Callable
"""make_multiplier that takes a float
multiplier as argument and returns a function"""


def make_multiplier(multiplier: Callable[[float], float]) -> float[[float], float]:
    """make_multiplier that takes a float
    multiplier as argument and returns a function"""

    return sum(multiplier)
