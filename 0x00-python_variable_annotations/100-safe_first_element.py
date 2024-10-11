#!/usr/bin/env python3
"""
The module provides a function to safely retrieve first element of a sequence.

The module includes:
- A function that returns the first element of a sequence or None if the
 sequence is empty.
"""

import typing
# from types import NoneType  # Explicitly import NoneType


def safe_first_element(
        lst: typing.Sequence[typing.Any]) -> typing.Union[typing.Any, None]:
    """
    Retrieve the first element of a sequence safely.

    Args_:
        lst (Sequence[Any]): A sequence (such as a list or tuple) from which
                             to get the first element.

    Returns_:
        Union[Any, None]: The first element of the sequence if it exists;
                          otherwise, None.
    """
    if lst:
        return lst[0]
    else:
        return None


if __name__ == "__main__":
    # Display function annotations
    print(safe_first_element.__annotations__)
