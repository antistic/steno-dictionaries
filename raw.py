#!/usr/bin/python
"""Write raw steno

Adapted from: https://pypi.org/project/plover-python-dictionary/

Writes out the raw steno stroke as if you had disabled all your dictionaries. Useful
for doing layout drills, e.g. https://joshuagrams.github.io/steno-jig/learn-keyboard.html.
"""

LONGEST_KEY = 1


def lookup(key):
    assert len(key) <= LONGEST_KEY

    stroke = key[0]

    if stroke == "*":
        raise KeyError

    return stroke
