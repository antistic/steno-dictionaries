#!/usr/bin/python
"""Modifiers dictionary which allows you to stack keys

Adapted from: https://github.com/EPLHREU/emily-modifiers

Requirements:
    - python dictionary plugin (https://pypi.org/project/plover-python-dictionary/)
    - scripts/conflicts.py if you want to find conflicts with other dictionaries

Changes:
    - different symbols
    - right hand symbols
    - keypad numbers
    - if you run this file directly it will print out any conflicts this file has with
      any of your enabled json dictionaries
    - stacking!

Stacking:
    You can write each part of the original stroke separately, for example if you are
    writing an uncommon key combination and would rather not arpeggiate, or if you want
    to use right hand symbols.

    Examples:
        KPWRA*FRLTZ: all together, like the original emily-modifiers
        -FLTZ, WHAO: modifiers first, then the key
        -LTZ, -FP, SR: starter, modifiers, key
        -FLTZ, -R, -B, A: add extra modifiers in between
        -PLTZ, SKWH-B: the above but end with right hand symbols

        See the tests for more examples of valid and invalid combinations.

Usage:
    It'll make more sense to read the original emily-modifiers first.
        https://github.com/EPLHREU/emily-modifiers

    pattern         STKPWHRAO EU
    is number              AO
    is symbol                *
    symbol variant         AO
    modifiers                   FRPB
    ender                           LGTSDZ

    right hand symbols:
    starter         STKPWHR
    symbol variant            EU
    pattern                     FRPBLG


"""
import re

UNIQUE_ENDERS = ["LTZ"]
UNIQUE_STARTERS = ["SKWH"]  # for symbols


# note: keep consistent with fingerspelling.py
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


# note: should keep consistent with symbols.py
SYMBOLS_LEFT = {
    # computer keys
    "KH": ["tab", "delete", "backspace", "escape"],
    "KPWHR": ["page_up", "end", "home", "page_down"],
    # no audio keys
    # space keys
    "": ["space", "tab", "return", "space"],
    # arrows
    "KPWR": ["up", "left", "right", "down"],
    # vertical lines
    "HR": ["exclam", "", "", ""],
    "PW": ["bar", "", "", ""],
    "TK": ["colon", "semicolon", "", ""],
    "TKHR": ["numbersign", "", "", ""],
    # bottom dots
    "R": ["period", "", "", ""],
    "W": ["comma", "", "", ""],
    "K": ["asterisk", "", "", "multiply"],
    # top dots
    "H": ["apostrophe", "", "", ""],
    "PH": ["quotedbl", "", "", ""],
    "P": ["grave", "", "", ""],
    "T": ["plus", "", "", ""],
    # horizontal lines (width 3)
    "TPH": ["parenleft", "bracketleft", "braceleft", ""],
    "KWR": ["parenright", "bracketright", "braceright", ""],
    # horizontal lines (width 2)
    "TP": ["minus", "", "", ""],
    "KW": ["underscore", "", "", ""],
    "TKPW": ["equal", "", "", ""],
    # slash shapes
    "WH": ["slash", "", "", ""],  # not mirrored
    "PWHR": ["percent", "", "", ""],  # not mirrored
    "PR": ["backslash", "", "", ""],  # not mirrored
    # and
    "SKP": ["ampersand", "", "", ""],
    # other shapes
    "PHR": ["question", "", "", ""],  # not mirrored
    "KPR": ["asciicircum", "", "", ""],
    "KPWH": ["dollar", "euro", "yen", "sterling"],  # not mirrored
    "TPWR": ["asciitilde", "at", "", ""],  # not mirrored
}

# note: should keep consistent with symbols.py
SYMBOLS_RIGHT = {
    # computer keys
    "FG": ["tab", "delete", "backspace", "escape"],
    "FRPBG": ["page_up", "end", "home", "page_down"],
    # no audio keys
    # space keys
    "": ["space", "tab", "return", "space"],
    # typable symbols
    "RPBG": ["up", "left", "right", "down"],
    # lines
    "FR": ["exclam", "", "", ""],
    "PB": ["bar", "", "", ""],
    "LG": ["colon", "semicolon", "", ""],
    "FRLG": ["numbersign", "", "", ""],
    # bottom dots
    "R": ["period", "", "", ""],
    "B": ["comma", "", "", ""],
    "G": ["asterisk", "", "", "multiply"],
    # top dots
    "F": ["apostrophe", "", "", ""],
    "FP": ["quotedbl", "", "", ""],
    "P": ["grave", "", "", ""],
    "L": ["plus", "", "", ""],
    # horizontal lines (width 3)
    "FPL": ["parenleft", "bracketleft", "braceleft", ""],
    "RBG": ["parenright", "bracketright", "braceright", ""],
    # horizontal lines (width 2)
    "PL": ["minus", "", "", ""],
    "BG": ["underscore", "", "", ""],
    "PBLG": ["equal", "", "", ""],
    # slash shapes (not mirrored)
    "RP": ["slash", "", "", ""],
    "FRPB": ["percent", "", "", ""],
    "FB": ["backslash", "", "", ""],
    # and
    "FBG": ["ampersand", "", "", ""],
    # other shapes
    "FPB": ["question", "", "", ""],  # not mirrored
    "RPG": ["asciicircum", "", "", ""],
    "RPBL": ["dollar", "euro", "yen", "sterling"],  # not mirrored
    "FPBG": ["asciitilde", "at", "", ""],  # not mirrored
}

# note: keep consistent with numbers.py
NUMBERS = {
    # RHWP
    0b0001: 1,
    0b0101: 2,
    0b0100: 3,
    0b0011: 4,
    0b1111: 5,
    0b1100: 6,
    0b0010: 7,
    0b1010: 8,
    0b1000: 9,
    0b0110: 0,  # /
    0b1001: 10,  # \ (diagonal including 1)
    0b1011: 11,  # 🭼 (3 keys including 1)
    0b1101: 12,  # 🭾 (3 keys including 2)
}


LONGEST_KEY = 6  # ender, 4 modifiers, key


def lookup(strokes):
    assert len(strokes) <= LONGEST_KEY, "length"

    match = re.fullmatch(r"([#STKPWHRAO*-EUFRPB]*)([LGTSDZ]*)", strokes[0])
    if not match:
        raise KeyError

    pattern, ender = match.groups()
    if ender not in UNIQUE_ENDERS:
        raise KeyError

    if pattern and pattern != "-":
        strokes_list = [pattern] + list(strokes[1:])
    else:
        strokes_list = list(strokes[1:])

    mods = set()
    character = None
    for stroke in strokes_list:
        if character:
            # can't add to the key combo after the character is defined
            raise KeyError

        match = re.fullmatch(
            r"([STKPWHR]*)([AO]*)(\*?)(-?)([EU]*)([FRPB]*)([LGTSDZ]*)", stroke
        )
        if not match:
            raise KeyError

        (key, vowel1, star, sep, vowel2, modifiers, ender) = match.groups()

        if key not in UNIQUE_STARTERS:
            if ender:
                raise KeyError

            if modifiers:
                if "R" in modifiers:
                    mods.add("shift")
                if "F" in modifiers:
                    mods.add("control")
                if "B" in modifiers:
                    mods.add("alt")
                if "P" in modifiers:
                    mods.add("super")

            if star:  # symbols, left side
                if key not in SYMBOLS_LEFT:
                    raise KeyError

                variant = 0
                if "A" in vowel1:
                    variant = variant + 1
                if "O" in vowel1:
                    variant = variant + 2

                entry = SYMBOLS_LEFT[key]
                if type(entry) == list:
                    extract = entry[variant]
                    # error out if the entry isn't applicable
                    if extract == "":
                        raise KeyError

                    character = extract
                else:
                    character = entry

            elif vowel1 == "AO" and not (vowel2):  # number
                number = NUMBERS[
                    ("P" in key) * 1
                    ^ ("W" in key) * 2
                    ^ ("H" in key) * 4
                    ^ ("R" in key) * 8
                ]

                function = False
                if "T" in key:
                    function = True

                if function:
                    character = "F" + str(number)
                    if number == 0:
                        raise KeyError
                else:
                    if number > 9:
                        raise KeyError
                    character = str(number)

            else:  # letter
                pattern = key + vowel1 + vowel2
                if pattern:
                    character = SPELLING[pattern]
        else:  # right side symbol
            shape = modifiers + ender
            if shape not in SYMBOLS_RIGHT:
                raise KeyError

            variant = 0
            if "E" in vowel2:
                variant = variant + 1
            if "U" in vowel2:
                variant = variant + 2

            entry = SYMBOLS_RIGHT[shape]
            if type(entry) == list:
                extract = entry[variant]
                # error out if the entry isn't applicable
                if extract == "":
                    raise KeyError

                character = extract
            else:
                character = entry

    if not character:
        return "{#}"
    if character and len(mods) == 0:
        raise KeyError

    combo = character
    for mod in sorted(list(mods)):
        combo = mod + "(" + combo + ")"

    result = "{#" + combo + "}"

    return result


if __name__ == "__main__":
    from scripts.conflicts import prepare, check_lookup_conflicts

    json_merged, python_lookups = prepare()

    check_lookup_conflicts(json_merged, python_lookups, lookup)
