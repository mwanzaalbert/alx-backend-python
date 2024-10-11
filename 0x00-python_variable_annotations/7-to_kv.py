#!/usr/bin/env python3
"""
The module provides a function that returns a string and a numeric value tuple.

The module includes:

A function that pairs a string with a numeric value (int or float) in a tuple.
"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    Create a tuple containing a string and a numeric value.

    Args_:
        k (str): The string key.
        v (List[Union[int, float]]): A list containing a numeric value
        (int or float) to be paired with the key.

    Returns_:
        Tuple[str, float]: A tuple containing the string key and the numeric
        value as a float.
    """
    return k, v ** 2


if __name__ == "__main__":
    # Display function annotations
    print(to_kv.__annotations__)

    # Test the to_kv function with sample inputs
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
