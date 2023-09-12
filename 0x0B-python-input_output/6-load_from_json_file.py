#!/usr/bin/python3
"""Defines the JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create the Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)

