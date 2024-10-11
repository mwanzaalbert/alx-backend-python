#!/usr/bin/env python3
"""
The module provides a function to round a float number down to the nearest int.

The module includes:
- A function that returns the floor value of a floating-point number.
"""


def floor(n: float) -> int:
    """
    Return the floor value of a floating-point number.

    Args_:
        n (float): The floating-point number to be floored.

    Returns_:
        int: The floor value of the input number, cast as an integer.
    """
    return int(n)


if __name__ == "__main__":
    import math

    # Test the floor function with sample input
    ans = floor(3.14)

    # Compare the result with Python's built-in math.floor function
    print(ans == math.floor(3.14))  # Should return True

    # Display function annotations
    print(floor.__annotations__)

    # Display the result and its type
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
