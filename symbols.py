#!/usr/bin/python
"""Symbols Dictionary

Adapted from: https://github.com/EPLHREU/emily-symbols

Requirements:
    - python dictionary plugin (https://pypi.org/project/plover-python-dictionary/)
    - scripts/conflicts.py if you want to find conflicts with other dictionaries

Changes:
    - different symbols
    - single, non-# starter
    - trailing spaces are explicitly added if attachment method is space
    - if you run this file directly it will print out any conflicts this file has with
      any of your enabled json dictionaries

Usage:
    starter        - SKWH (modifiable)
    spacing        - AO
    capitalisation - *
    variant        - EU
    symbol         - FRPBLG (any pattern)
    repetition     - TS
"""
import re

UNIQUE_STARTERS = ["SKWH"]
ATTACHMENT_METHOD = "space"

# variant format = ['', 'E', 'U', 'EU']
# or single string
# F P L
# R B G
SYMBOLS = {
    # computer keys
    "FG": ["{#Tab}", "{#Print}", "{#Return}", "{#Shift(Tab)}"],
    "RL": ["{#AudioPlay}", "{#AudioPrev}", "{#AudioNext}", "{#AudioMute}"],
    "FL": ["{#AudioLowerVolume}", "{#Home}", "{#End}", "{#AudioRaiseVolume}"],
    "RG": ["{#MonBrightnessDown}", "{#Page_Up}", "{#Page_Down}", "{#MonBrightnessUp}"],
    # space keys
    "": [
        "{^ ^}",
        "{*!}",
        "{*?}",
        "{#Space}",
    ],  # space, delete space, add space, space key
    # arrows
    "RPBG": ["{#Up}", "{#Left}", "{#Right}", "{#Down}"],
    # vertical lines
    "FR": ["!", "[", "]", ""],  # vertical line (left)
    "PB": ["|", "(", ")", "()"],  # vertical line (middle)
    "LG": [":", "\{", "\}", ";"],  # vertical line (right)
    "FRLG": ["#", "@", "~", "#!"],  # two (separated) vertical lines
    # left dots
    "F": ["'", "‘", "’", "‚"],  # dot (top left), like '
    "FP": ['"', "“", "”", "„"],  # two top left keys, like "
    "R": [
        ".",
        "•",
        "·",
        "…",
    ],  # dot (bottom left). period, bullet, interpunct, ellipses
    # middle dots
    "P": ["`", "<", ">", "->"],  # dot (mid top)
    "B": [",", "</", "/>", "=>"],  # dot (bottom middle)
    # right dots
    "L": ["+", "<=", ">=", "™"],  # dot (top right)
    "G": ["*", "×", "x", ""],  # dot (bottom right)
    # horizontal lines (width 3)
    "RBG": ["$", "¥", "€", "£"],  # S-shape
    # horizontal lines (width 2)
    "PL": ["-", "−", "–", "—"],  # line (top right). hyphen, minus, en-dash, em-dash
    "BG": ["_", "≠", "≈", "~"],  # line (bottom right)
    "PBLG": ["=", "!=", "!==", ""],  # both lines
    # slash shapes
    "RP": ["/", "÷", "?", "%"],  # /-shape
    "FB": ["\\", "", "", ""],  # \-shape
    # other shapes
    "FPB": ["?", "", "", "‽"],  # ?-shape
    "RPG": ["^", "°", "", "&"],  # ^-shape
}


LONGEST_KEY = 1


def lookup(chord):
    assert len(chord) <= LONGEST_KEY

    stroke = chord[0]

    # the regex decomposes a stroke into the following groups/variables:
    # starter:        #STKPWHR
    # attachment:             AO
    # capitalisation:           *-
    # variants:                   EU
    # pattern:                      FRPBLG
    # repetitions:                        TS
    # unused:                               DZ
    match = re.fullmatch(
        r"([#STKPWHR]*)([AO]*)([*-]?)([EU]*)([FRPBLG]*)([TS]*)", stroke
    )

    if match is None:
        raise KeyError
    (
        starter,
        attachments,
        capitalisation,
        variants,
        pattern,
        repetitions,
    ) = match.groups()

    if starter not in UNIQUE_STARTERS:
        raise KeyError

    # calculate the attachment method, and remove attachment specifier keys
    attach = [
        (ATTACHMENT_METHOD == "space") ^ ("A" in attachments),
        (ATTACHMENT_METHOD == "space") ^ ("O" in attachments),
    ]

    # detect if capitalisation is required, and remove specifier key
    capital = capitalisation == "*"

    # calculate the variant number, and remove variant specifier keys
    variant = 0
    if "E" in variants:
        variant = variant + 1
    if "U" in variants:
        variant = variant + 2

    # calculate the repetition, and remove repetition specifier keys
    repeat = 1
    if "S" in repetitions:
        repeat = repeat + 1
    if "T" in repetitions:
        repeat = repeat + 2

    if pattern not in SYMBOLS:
        raise KeyError

    # extract symbol entry from the 'symbols' dictionary, with variant specification if available
    selection = SYMBOLS[pattern]
    if type(selection) == list:
        selection = selection[variant]
    output = selection

    # repeat the symbol the specified number of times
    output = output * repeat

    # attachment space to either end of the symbol string to avoid escapement,
    # but prevent doing this for retrospective add/delete spaces, since it'll
    # mess with these macros
    if selection not in ["{*!}", "{*?}"]:
        output = " " + output + " "

    # add appropriate attachment as specified (again, prevent doing this
    # for retrospective add/delete spaces)
    if selection not in ["{*!}", "{*?}"] and not selection.startswith("{#Audio"):
        if attach[0]:
            output = "{^}" + output
        if attach[1]:
            output = output + "{^}"

    # cancel out some formatting when using space attachment
    if ATTACHMENT_METHOD == "space":
        if not attach[0]:
            output = "{}" + output
        if not attach[1]:
            output = output + "{^ ^}"  # explicit space

    # apply capitalisation
    if capital:
        output = output + "{-|}"

    # all done :D
    return output


if __name__ == "__main__":
    from scripts.conflicts import prepare, check_lookup_conflicts

    json_merged, python_lookups = prepare()

    check_lookup_conflicts(json_merged, python_lookups, lookup)
