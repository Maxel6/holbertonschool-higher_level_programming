#!/usr/bin/python3
import json
"""Class to JSON"""


def class_to_json(obj):
    """eturns the dictionary description with simple data structure for \
    JSON serialization of an object"""
    return json.dumps(obj.__dict__)
