#!/usr/bin/env python3
"""
This module provides a function to compute
the floor of a float.
"""


def floor(n: float) -> int:
    """
    Return the floor of the float n.

    Args:
        n (float): A floating point number
        to be floored.

    Returns:
        int: The largest integer less
        than or equal to n.
    """
    return int(n // 1)
