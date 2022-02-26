#!/usr/bin/python
"""Modifiers dictionary which allows you to stack keys

Adapted from: https://github.com/EPLHREU/emily-modifiers

Requirements:
    - python dictionary plugin (https://pypi.org/project/plover-python-dictionary/)

Changes:
    - different symbols
    - keypad numbers

Usage:
    It'll make more sense to read the original emily-modifiers first.
        https://github.com/EPLHREU/emily-modifiers
"""
from plover.system import Stroke

UNIQUE_ENDERS = ["-LTZ"]
UNIQUE_STARTERS = ["SKWH"]  # for symbols

# note: keep up to date with fingerspelling.py
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
    # not Plover theory
    "SWR": "z",  # easier on the hands
    ## left hand only fingerspelling
    "SA": "e",
    "SAO": "i",
    "SO": "u",
}


# symbol positions are similar but not th same as in symbols.py
SYMBOLS = {
    # ░░░░░░ spaces
    # ░░░░░░
    "": ["space", "backspace", "delete", "escape"],
    #
    # ░░░░██ keys
    # ██░░░░
    "KH": ["tab", "print", "return", ""],
    #
    # ██░░██  ░░░░░░ navigation and
    # ░░░░░░  ██░░██ brightness
    "TH": ["page_up", "home", "end", ""],
    "KR": ["page_down", "", "", ""],
    #
    # ░░██░░ arrows
    # ██████
    "KPWR": ["up", "left", "right", "down"],
    #
    # ░░░░██ ░░██░░ ██░░░░ tall
    # ░░░░██ ░░██░░ ██░░░░ punctuation
    "HR": ["exclam", "bracketleft", "bracketright", ""],
    "PW": ["bar", "parenleft", "parenright", ""],
    "TK": ["colon", "braceleft", "braceright", "semicolon"],
    #
    # ██░░██ complicated
    # ██░░██ punctuation
    "TKHR": ["numbersign", "at", "asciitilde", ""],
    #
    # ░░░░██ ░░████ quotes
    # ░░░░░░ ░░░░░░
    "H": ["apostrophe", "", "", ""],
    "PH": ["quotedbl", "", "", ""],
    #
    # ░░░░░░ dots
    # ░░░░██
    "R": ["period", "", "", ""],
    #
    # ░░██░░ ░░░░░░
    # ░░░░░░ ░░██░░
    "P": ["grave", "less", "greater", ""],
    "W": ["comma", "", "", ""],
    #
    # ██░░░░ ░░░░░░
    # ░░░░░░ ██░░░░
    "T": ["plus", "", "", ""],
    "K": ["asterisk", "", "", ""],
    #
    # ░░░░░░ currency
    # ██████
    "KWR": ["dollar", "euro", "yen", "sterling"],
    #
    # ████░░ ░░░░░░ ████░░
    # ░░░░░░ ████░░ ████░░
    "TP": ["minus", "", "", ""],
    "KW": ["underscore", "", "", ""],
    "TKPW": ["equal", "", "", ""],
    #
    # ░░░░██ ░░██░░ slashes
    # ░░██░░ ░░░░██
    "WH": ["slash", "", "", "percent"],  # not mirrored
    "PR": ["backslash", "", "", ""],  # not mirrored
    # other shapes
    #
    # ░░████ question
    # ░░░░██ mark
    "PHR": ["question", "", "", ""],  # not mirrored
    #
    # ░░██░░
    # ██░░██
    "KPR": ["asciicircum", "", "", "ampersand"],
}

# note: keep consistent with numbers.py
NUMBERS = {
    # RHWP
    "P": 1,
    "PH": 2,
    "H": 3,
    "PW": 4,
    "PWHR": 5,
    "HR": 6,
    "W": 7,
    "WR": 8,
    "R": 9,
    "WH": 0,
    "PR": 0,
    "K": 10,
    "KP": 11,
    "KPH": 12,
}


LONGEST_KEY = 1


def lookup(strokes):
    assert len(strokes) <= LONGEST_KEY, "length"

    stroke: Stroke = Stroke(strokes[0])
    keys = stroke.keys()

    ender = stroke & Stroke("-LGTSDZ")
    if ender.rtfcre not in UNIQUE_ENDERS:
        raise KeyError

    modifiers = stroke & Stroke("-FRPB")
    modifier_keys = modifiers.keys()
    if len(modifier_keys) == 0:
        raise KeyError

    mods = set()
    if "-R" in modifiers:
        mods.add("shift")
    if "-F" in modifiers:
        mods.add("control")
    if "-B" in modifiers:
        mods.add("alt")
    if "-P" in modifiers:
        mods.add("super")

    is_symbol = "*" in keys
    is_number = (
        not is_symbol
        and (Stroke("AO") in stroke)
        and (Stroke("EU") not in stroke)
        and ("S-" not in keys)
    )

    character = ""
    if is_symbol:
        pattern = stroke & Stroke("STKPWHREU")
        variant = ("A-" in keys) + 2 * ("O-" in keys)  # abuse of True = 1, False = 0
        entry = SYMBOLS[pattern.rtfcre]
        if type(entry) == list:
            character = entry[variant]
        else:
            character = str(entry)
    elif is_number:
        pattern = stroke & Stroke("KPWHR")
        number = NUMBERS[pattern.rtfcre]
        if "T-" in keys:
            character = "F" + str(number)
        else:
            character = str(number)
    else:
        pattern = stroke & Stroke("STKPWHRAOEU")
        character = SPELLING[pattern.rtfcre]

    if not character:
        return "{#}"
    if character and len(mods) == 0:
        raise KeyError

    combo = character
    for mod in sorted(list(mods)):
        combo = mod + "(" + combo + ")"

    result = "{#" + combo + "}"

    return result
