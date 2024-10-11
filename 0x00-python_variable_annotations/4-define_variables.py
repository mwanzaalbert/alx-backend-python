#!/usr/bin/env python3

"""
The module demonstrates the use of variable annotations in Python.

The module includes:
- Examples of variables annotated with specific data types.
"""

# Variable annotations
a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"

if __name__ == "__main__":
    # Display the type and value of each variable
    print("a is a {} with a value of {}".format(type(a), a))
    print("pi is a {} with a value of {}".format(type(pi), pi))
    print(f"i_understand_annotations is a {type(i_understand_annotations)}" +
          " with a value of {}".format(i_understand_annotations))
    print("school is a {} with a value of {}".format(type(school), school))
