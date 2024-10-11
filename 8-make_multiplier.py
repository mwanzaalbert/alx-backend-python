#!/usr/bin/python3
"""
The module provides a closer function to create a multiplier.

The module includes:
A function that calls a function to multiply a number by specified multiplier.
"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    Create a function that multiplies a given number by specified multiplier.

    Args_:
        multiplier (float): The number by which other numbers will be
                            multiplied.

    Returns_:
        Callable[[float], float]: A function that takes a float and returns
                                  the product of the float and the multiplier.
    """

    def times(x: float) -> float:
        """
        Multiply a number by the multiplier.

        Args_:
            x (float): The number to be multiplied.

        Returns_:
            float: The result of multiplying x by the multiplier.
        """
        return x * multiplier

    return times


if __name__ == "__main__":
    # Display function annotations
    print(make_multiplier.__annotations__)

    # Create a multiplier function
    fun = make_multiplier(2.22)

    # Test the multiplier function with a sample input
    print("{}".format(fun(2.22)))
