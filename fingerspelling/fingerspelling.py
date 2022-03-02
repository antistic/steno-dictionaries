#!/usr/bin/python
"""Create a fingerspelling JSON dictionary

Usage:
    `python fingerspelling.py`
    or use the generated file "fingerspelling.json" in the parent directory
"""

import json
from pathlib import Path

from plover_stroke import BaseStroke
from plover.system import english_stenotype


class Stroke(BaseStroke):
    pass


Stroke.setup(
    english_stenotype.KEYS,
    english_stenotype.IMPLICIT_HYPHEN_KEYS,
    english_stenotype.NUMBER_KEY,
    english_stenotype.NUMBERS,
)


# Set to None to print to console instead
OUTPUT_FILE = Path(__file__).parent / "../fingerspelling.json"

SPELLING = {
    # Plover theory
    "A": "a",
    "PW": "b",
    "KR": "c",
    "TK": "d",
    "E": "e",
    "TP": "f",
    "TKPW": "g",
    "H": "h",
    "EU": "i",
    "SKWR": "j",
    "K": "k",
    "HR": "l",
    "PH": "m",
    "TPH": "n",
    "O": "o",
    "P": "p",
    "KW": "q",
    "R": "r",
    "S": "s",
    "T": "t",
    "U": "u",
    "SR": "v",
    "W": "w",
    "KP": "x",
    "KWR": "y",
    "STKPW": "z",
    #
    # not Plover theory
    "SWR": "z",  # easier on the hands
    # left hand only fingerspelling
    # same pattern as on the right, but with an S
    "SA": "e",
    "SAO": "i",
    "SO": "u",
}


def escape(string):
    return string.replace("{", "{{").replace("}", "}}")


# 1: The stroke added to make that fingerspelling variant
# 2: The text before the letter in the translation
# 3: The text after the letter in the translation
VARIANTS = [
    (Stroke("*"), "{^}{>}", "{^}"),
    (Stroke("*P"), "{^}{-|}", "{^}"),
    (Stroke("-RBGS"), "{>}{&", "}"),
    (Stroke("-FPLT"), "{-|}{&", "}"),
]


if __name__ == "__main__":
    output = {}

    for key, letter in SPELLING.items():
        letter_stroke = Stroke(key)
        letter_keys = letter_stroke.keys()
        for variant_stroke, before, after in VARIANTS:
            stroke = letter_stroke + variant_stroke
            output[str(stroke)] = before + letter + after

    if OUTPUT_FILE:
        OUTPUT_FILE.write_text(json.dumps(output, indent=2))
    else:
        print(json.dumps(output, indent=2))
