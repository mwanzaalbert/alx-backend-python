#!/usr/bin/env python3
"""
The module provides a function to safely retrieve a value from a dictionary.

The module includes:
- A function that returns the value associated with a key in a dictionary or
  a default value if the key is not present.
"""

import typing
# from types import NoneType  # Explicitly import NoneType

# Define the type variable T
T = typing.TypeVar('T')


def safely_get_value(
        dct: typing.Mapping,
        key: typing.Any,
        default: typing.Union[T, None] = None) -> typing.Union[typing.Any, T]:
    """
    Safely retrieve a value from a dictionary using a key.

    Args_:
        dct (Mapping): The dictionary from which to retrieve the value.
        key (Any): The key to look up in the dictionary.
        default (Union[T, NoneType], optional): The value to return if the key
                                               is not found. Defaults to None.

    Returns_:
        Union[Any, T]: The value associated with the key if it exists;
                       otherwise, the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default


if __name__ == "__main__":
    # Display function annotations
    annotations = safely_get_value.__annotations__

    print("Here's what the mappings should look like:")
    for k, v in annotations.items():
        print("{}: {}".format(k, v))
