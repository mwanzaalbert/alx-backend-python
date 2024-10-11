#!/usr/bin/python3
"""
The module provides a function to calc sum of a mixed list of ints and floats.

The module includes:
- A function that sums all elements in a list containing both ints and floats.
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers and floating-point numbers.

    Args_:
        mxd_lst (List[Union[int, float]]): A list containing integers and/or
        floating-point numbers to be summed.

    Returns_:
        float: The sum of the numbers in the input list, returned as a float.
    """
    return sum(mxd_lst)


if __name__ == "__main__":
    # Display function annotations
    print(sum_mixed_list.__annotations__)

    # Test the sum_mixed_list function with a sample mixed list
    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)

    # Check if the output matches the built-in sum function
    print(ans == sum(mixed))  # Should return True

    # Display the result and its type
    print("sum_mixed_list(mixed) returns {} which is a {}".format(ans,
                                                                  type(ans)))
