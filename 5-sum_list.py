#!/usr/bin/python3
"""
The module provides a function to calculate the sum of a list of float numbers.

The module includes:
- A function that sums all elements in a list of floats.
"""

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """
    Calculate the sum of a list of floating-point numbers.

    Args_:
        input_list (List[float]): A list of float numbers to be summed.

    Returns_:
        float: The sum of the numbers in the input list.
    """
    return sum(input_list)


if __name__ == "__main__":
    # Test the sum_list function with a sample list of floats
    floats = [3.14, 1.11, 2.22]
    floats_sum = sum_list(floats)

    # Check if the output matches the built-in sum function
    print(floats_sum == sum(floats))  # Should return True

    # Display function annotations
    print(sum_list.__annotations__)

    # Display the result and its type
    print(f"sum_list(floats) returns {floats_sum}" +
          " which is a {}".format(type(floats_sum)))
