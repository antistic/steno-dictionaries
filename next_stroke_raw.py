#!/usr/bin/python
"""Write raw steno stroke on next stroke

Adapted from: https://pypi.org/project/plover-python-dictionary/
"""

LONGEST_KEY = 2

SHOW_STROKE_STENO = "RA*U"


def lookup(key):
    assert len(key) <= LONGEST_KEY

    if SHOW_STROKE_STENO != key[0]:
        raise KeyError
    if len(key) == 1:
        return "{#}"

    return key[1]
