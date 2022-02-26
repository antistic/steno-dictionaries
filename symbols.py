#!/usr/bin/python
"""Symbols Dictionary

Adapted from:
    https://github.com/EPLHREU/emily-symbols

    - different symbols
    - trailing spaces are explicitly added if attachment method is space

Requirements:
    - python dictionary plugin (https://pypi.org/project/plover-python-dictionary/)

Usage:
    starter        - SKWH (modifiable)
    spacing        - AO
    capitalisation - *
    variant        - EU
    symbol         - FRPBLG (any pattern)
    repetition     - TS
"""

from plover.system import Stroke

UNIQUE_STARTERS = ["SKWH"]
ATTACHMENT_METHOD = "space"

# variant format = ['', 'E', 'U', 'EU']
# or single string to set all
SYMBOLS = {
    # ░░░░░░ spaces
    # ░░░░░░
    "": [
        "{^ ^}",
        "{*!}",  # delete space
        "{*?}",  # add space
        "{#Space}",
    ],
    #
    # ██░░░░ keys
    # ░░░░██
    "-FG": ["{#Tab}", "{#Print}", "{#Return}", "{#Shift(Tab)}"],
    #
    # ██░░██  ░░░░░░ navigation and
    # ░░░░░░  ██░░██ brightness
    "-FL": ["{#Page_Up}", "{#Home}", "{#End}", "{#MonBrightnessUp}"],
    "-RG": [
        "{#Page_Down}",
        "{#Control(Left)}",  # move cursor left one word
        "{#Control(Right)}",  # move cursor right one word
        "{#MonBrightnessDown}",
    ],
    #
    # ██░░██ media
    # ██░░░░ position
    "-FRL": ["{#AudioPlay}", "{#AudioPrev}", "{#AudioNext}", "{#AudioStop}"],
    #
    # ██░░░░ media
    # ██░░██ volume
    "-FRG": [
        "{#AudioMute}",
        "{#AudioLowerVolume}",
        "{#AudioRaiseVolume}",
        "{#AudioMute}",
    ],
    #
    # ░░██░░ arrows
    # ██████
    "-RPBG": ["{#Up}", "{#Left}", "{#Right}", "{#Down}"],
    #
    # ██░░░░ ░░██░░ ░░░░██ tall
    # ██░░░░ ░░██░░ ░░░░██ punctuation
    "-FR": ["!", "[", "]", ""],
    "-PB": ["|", "(", ")", "()"],
    "-LG": [":", "\\{", "\\}", ";"],
    #
    # ██░░██ complicated
    # ██░░██ punctuation
    "-FRLG": ["#", "@", "~", "#!"],
    #
    # ██░░░░ ████░░ quotes
    # ░░░░░░ ░░░░░░
    "-F": ["'", "‘", "’", "‚"],  # dot (top left), like '
    "-FP": ['"', "“", "”", "„"],  # two top left keys, like "
    #
    # ░░░░░░ dots
    # ██░░░░
    "-R": [".", "•", "·", "…"],  # period, bullet, interpunct, ellipses
    #
    # ░░██░░ ░░░░░░
    # ░░░░░░ ░░██░░
    "-P": ["`", "<", ">", "->"],
    "-B": [",", "</", "/>", "=>"],
    #
    # ░░░░██ ░░░░░░
    # ░░░░░░ ░░░░██
    "-L": ["+", "©", "°", "™"],
    "-G": ["*", "", "", "×"],
    #
    # ░░░░░░ currency
    # ██████
    "-RBG": ["$", "£", "€", "¥"],
    #
    # ░░████ ░░░░░░ ░░████
    # ░░░░░░ ░░████ ░░████
    "-PL": ["-", "−", "–", "—"],  #  hyphen, minus, en-dash, em-dash
    "-BG": ["_", "", "", "~"],
    "-PBLG": ["=", "!=", "!==", "≈"],
    #
    # ░░██░░ ██░░░░ slashes
    # ██░░░░ ░░██░░
    "-RP": ["/", "÷", "", "%"],
    "-FB": ["\\", "", "", ""],
    #
    # ████░░ question
    # ░░██░░ marks
    "-FPB": ["?", "?!", "(?)", "‽"],
    #
    # ░░██░░
    # ██░░██
    "-RPG": ["^", "{#Tab}", "", "&"],
}


LONGEST_KEY = 1


def lookup(strokes):
    assert len(strokes) <= LONGEST_KEY

    stroke = Stroke(strokes[0])
    keys = stroke.keys()

    starter = stroke & Stroke("#STKPWHR-")
    pattern = stroke & Stroke("-FRPBLG")

    if starter.rtfcre not in UNIQUE_STARTERS:
        raise KeyError

    if pattern.rtfcre not in SYMBOLS:
        raise KeyError

    attach_left = "A-" in keys
    attach_right = "O-" in keys
    capital = "*" in keys
    variant = ("-E" in keys) + 2 * ("-U" in keys)  # abuse of True = 1, False = 0
    repeat = 1 + ("-S" in keys) + 2 * ("-T" in keys)

    # calculate the attachment method
    attach = [
        (ATTACHMENT_METHOD == "space") ^ attach_left,
        (ATTACHMENT_METHOD == "space") ^ attach_right,
    ]

    # extract symbol entry from the 'symbols' dictionary, with variant specification if available
    selection = SYMBOLS[pattern.rtfcre]
    if isinstance(selection, list):
        selection = selection[variant]
    output = selection

    # repeat the symbol the specified number of times
    output = output * repeat

    if selection not in ["{*!}", "{*?}"]:  # retrospective add/delete spaces
        # attachment space to either end of the symbol string to avoid escapement,
        output = " " + output + " "

        # add appropriate attachment as specified
        if not selection.startswith("{#Audio"):
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

    if capital:
        output = output + "{-|}"

    return output
