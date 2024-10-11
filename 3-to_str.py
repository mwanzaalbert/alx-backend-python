#!/usr/bin/python3
"""
This module provides a function to convert a floating-point number to a string.

The module includes:
- A function that converts a float to its string representation.
"""


def to_str(n: float) -> str:
    """
    Convert a floating-point number to its string representation.

    Args_:
        n (float): The floating-point number to be converted.

    Returns_:
        str: The string representation of the input number.
    """
    return str(n)


if __name__ == "__main__":
    # Test the to_str function with sample input
    pi_str = to_str(3.14)

    # Check if the output matches the string representation of 3.14
    print(pi_str == str(3.14))  # Should return True

    # Display function annotations
    print(to_str.__annotations__)

    # Display the result and its type
    print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))
