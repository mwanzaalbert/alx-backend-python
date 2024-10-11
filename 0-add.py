#!/usr/bin/python3
"""
The module provides a simple addition function.

The module includes:
- A function to add two floating-point numbers.
"""


def add(a: float, b: float) -> float:
    """
    Add two floating-point numbers.

    Args_:
        a (float): The first number.
        b (float): The second number.

    Returns_:
        float: The sum of the two numbers.
    """
    return a + b


if __name__ == "__main__":
    # Test the add function with sample inputs
    print(add(1.11, 2.22) == 1.11 + 2.22)  # Should return True
    # Display function annotations
    print(add.__annotations__)
