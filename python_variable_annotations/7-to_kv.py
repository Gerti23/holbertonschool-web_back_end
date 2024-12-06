#!/usr/bin/env python3
"""
This module provides a function to create a tuple
with a string and the square of a number.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the string k,
    and the second element is the square of the int/float v.

    Args:
        k (str): The string to include in the tuple.
        v (Union[int, float]): The number to square and
        include in the tuple.

    Returns:
        Tuple[str, float]: A tuple containing the string
        k and the square of the number v.
    """
    return (k, float(v ** 2))
