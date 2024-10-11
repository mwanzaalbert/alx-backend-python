#!/usr/bin/env python3
"""
The module provides a simple string concatenation function.

The module includes:
- A function to concatenate two strings.
"""


def concat(a: str, b: str) -> str:
    """
    Concatenate two strings.

    Args_:
        a (str): The first string.
        b (str): The second string.

    Returns_:
        str: The concatenated result of the two strings.
    """
    return a + b


if __name__ == "__main__":
    # Test the concat function with sample inputs
    str1 = "egg"
    str2 = "shell"

    # Should return True if the function works as expected
    print(concat(str1, str2) == "{}{}".format(str1, str2))

    # Display function annotations
    print(concat.__annotations__)
