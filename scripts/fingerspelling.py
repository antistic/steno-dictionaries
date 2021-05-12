#!/usr/bin/python
"""Create a fingerspelling JSON dictionary

Usage:
    `python fingerspelling.py`
    or use the generated file "fingerspelling.json" in the parent directory

Key:
    This is slightly different to the default Plover dictionary — here, the plain * and
    *P entries are attach, not glue, so that it's easier to use programs like vim.

    The glue versions now exist under *RBGS and *FPLT.

    *     - `{^}{>}x{^}`  attach lowercase (in Plover as `{>}{&x}`)
    *P    - `{^}{-|}x{^}` attach uppercase (in Plover as `{&X})
    *FPLT - `{>}{&x}`     glue lowercase (inconsistently in Plover as `{&X.}`)
    *RBGS - `{-|}{&x}`    glue uppercase (inconsistently in Plover as `{>}{&x}`)

Conflicts:
    This dictionary has conflicts with the default plover dictionaries — run this file
    with SHOW_CONFLICTS = True to see conflicts with your currently enabled
    dictionaries (except OUTPUT_FILE). This requires you to also have conflicts.py in
    the same directory as this file.

    'A*FPLT':
        |-> 'amount' in 'main.json'    // also defined as APLT
    '*ERBGS':
        |-> '{extra^}' in 'main.json'  // also defined as ERBGS
    '*EURBGS':
        |-> 'issues' in 'main.json'    // also defined as *EURBS
    'SKWR*RBGS':
        |-> '{;}' in 'main.json'       // also defined as SP-PT
"""

import re
import json
from pathlib import Path


# Print any conflicts found in enabled dictionaries
SHOW_CONFLICTS = False

# Set to None to print to console instead
OUTPUT_FILE = Path(__file__).parent / "../fingerspelling.json"

SPELLING = {
    "A": "a",
    "PW": "b",
    "KR": "c",
    "TK": "d",
    "E": "e",
    "TW": "e",  # for left hand only fingerspelling
    "TP": "f",
    "TKPW": "g",
    "H": "h",
    "EU": "i",
    "TWR": "i",  # for left hand only fingerspelling
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
    "TR": "u",  # for left hand only fingerspelling
    "SR": "v",
    "W": "w",
    "KP": "x",
    "KWR": "y",
    "STKPW": "z",
    "SWR": "z",  # easier on the hands
}

# left:      #STKPWHR
# vowel1:            AO
# separator:           *-
# vowel2:                EU
# right:                   FRPBLTSDZ
# letter: the letter as defined in SPELLING
# https://docs.python.org/3/library/string.html#format-string-syntax
VARIANTS = [
    ("{left}{vowels1}*{vowels2}", "{{^}}{{>}}{letter}{{^}}"),
    ("{left}{vowels1}*{vowels2}P", "{{^}}{{-|}}{letter}{{^}}"),
    ("{left}{vowels1}*{vowels2}RBGS", "{{>}}{{&{letter}}}"),
    ("{left}{vowels1}*{vowels2}FPLT", "{{-|}}{{&{letter}}}"),
]


if __name__ == "__main__":
    output = {}
    if SHOW_CONFLICTS:
        from conflicts import prepare, check_strokes_conflicts

        json_merged, python_lookups = prepare(ignore=[str(OUTPUT_FILE.resolve())])

    for stroke, letter in SPELLING.items():
        match = re.fullmatch(
            r"(#?S?T?K?P?W?H?R?)(A?O?)(\*?-?)(E?U?)(F?R?P?B?L?G?T?D?Z?)", stroke
        )
        if not match:
            raise ValueError("Not steno")

        left, vowels1, separator, vowels2, right = match.groups()

        strokes = []
        for stroke_format, translation in VARIANTS:
            stroke = stroke_format.format(
                left=left,
                vowels1=vowels1,
                separator=separator,
                vowels2=vowels2,
                right=right,
            )
            strokes.append(stroke)
            output[stroke] = translation.format(letter=letter)

        if SHOW_CONFLICTS:
            check_strokes_conflicts(json_merged, python_lookups, strokes)

    if OUTPUT_FILE:
        OUTPUT_FILE.write_text(json.dumps(output, indent=2))
    else:
        print(json.dumps(output, indent=2))
