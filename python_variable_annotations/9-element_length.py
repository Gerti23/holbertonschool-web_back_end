#!/usr/bin/env python3
"""
Module for calculating the length of elements in
an iterable of sequences.

This module provides a function `element_length`
that returns a list of tuples,
each containing a sequence from the input and its length.
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    where each tuple contains a sequence and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
        each containing a sequence
        and its length.
    """
    return [(i, len(i)) for i in lst]
