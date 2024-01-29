#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format 'My name is <first_name> <last_name>'.

    Parameters:
    - first_name (str): The first name.
    - last_name (str): The last name. Default is an empty string.

    Raises:
    - TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string" or
                        "last_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
