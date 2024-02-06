#!/usr/bin/env python3
"""
Function to return the JSON representation of an object (string).
"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of the given object."""
    return json.dumps(my_obj)
