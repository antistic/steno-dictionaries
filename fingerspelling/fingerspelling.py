#!/usr/bin/python
"""Create a fingerspelling JSON dictionary

Usage:
    Edit the SPELLING and VARIANTS

    Then run `python fingerspelling`
    `python fingerspelling.py -h` for help on what the options are
"""

import argparse
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

# key: letter(s)
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


def generate_dictionary():
    dictionary = {}
    for key, letter in SPELLING.items():
        letter_stroke = Stroke(key)
        for variant_stroke, before, after in VARIANTS:
            stroke = letter_stroke + variant_stroke
            dictionary[str(stroke)] = before + letter + after
    return dictionary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a fingerspelling dictionary")
    parser.add_argument(
        "output_file",
        help="Dictionary output file (default: fingerspelling.json)",
        type=str,
        nargs="?",
        default="fingerspelling.json",
    )
    parser.add_argument(
        "--console",
        help="Print dictionary to the console instead of saving it to a file",
        action="store_true",
    )

    args = parser.parse_args()

    dictionary = generate_dictionary()

    if args.console:
        print(json.dumps(dictionary, indent=2))
    else:
        output_path = Path(args.output_file)
        output_path.write_text(json.dumps(dictionary, indent=2))

        print(
            f"Wrote dictionary ({len(dictionary.keys())} entries) to {output_path.resolve()}"
        )
