#!/usr/bin/env python3
"""
Module for creating multiplier functions.

This module provides a function `make_multiplier`
that returns another
function which multiplies a given float by the
specified multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a given
    float by the specified multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that
        takes a float as input and
        returns the product of the input and the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplies the given value by the preset multiplier.

        Args:
            value (float): The value to be multiplied.

        Returns:
            float: The result of the multiplication.
        """
        return value * multiplier

    return multiplier_function
