#!/usr/bin/env python3
"""
The module provides a function to calc len() of elements in list of sequences.

The module includes:
- A function that returns the length of each sequence in the input iterable.
"""

import typing


def element_length(
        lst: typing.Iterable[typing.Sequence]) -> (
            typing.List[typing.Tuple[typing.Sequence, int]]):
    """
    Calculate the length of each element in an iterable of sequences.

    Args_:
        lst (Iterable[Sequence]): An iterable containing sequences
                                    (like lists, tuples, etc.).

    Returns_:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains
                                    the sequence and its length.
    """
    return [(i, len(i)) for i in lst]


if __name__ == "__main__":
    # Display function annotations
    print(element_length.__annotations__)
