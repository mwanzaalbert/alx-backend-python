#!/usr/bin/env python3
"""
This module provides a function to create a zoomed-in version of an array.

The module includes:
- A function that repeats each element of a tuple a specified number of times.
"""

import typing
from typing import List


def zoom_array(lst: typing.Tuple, factor: int = 2) -> typing.List:
    """
    Create a zoomed-in version of a tuple by repeating each element.

    Args_:
        lst (Tuple): The tuple containing elements to be zoomed in.
        factor (int, optional): The number of times to repeat each element.
                                Defaults to 2.

    Returns_:
        List: A list containing the zoomed-in elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]

    return zoomed_in


array = [12, 72, 91]

# Generate zoomed-in versions of the array
zoom_2x = zoom_array(tuple(array))
zoom_3x = zoom_array(tuple(array), 3)


if __name__ == "__main__":
    # Display function annotations
    print(zoom_array.__annotations__)
