#!/usr/bin/python
"""Numbers dictionary

Keypad design inspired by:
    https://www.reddit.com/r/Plover/comments/fgt6tp/list_of_alternative_number_systems/

    The original design allows for three digits at a time. I rarely used this, and
    it was hard to use with a number bar (it was designed for thumb number keys).
    So I've chosen to reduce the digits, and made more room for options. Most of the
    options use only the top row of the left hand, making it easier to hit with a
    number bar.

Requirements:
    - python dictionary plugin (https://pypi.org/project/plover-python-dictionary/)
    - recent version of Plover (after October 2021)

Usage:
    Enter up to 2 digits at once

    Digits are arranged in blocks of four keys:

        - First digit: FRPB
        - Second digit: LGTS

        The corners are 1, 3, 7, 9.
        Adjacent keys give you the ones in between.

        Any diagonal makes 0.
        Any 3 with the top row makes 00.
        L-shape makes 000
        Backwards L-shape makes ,000


    The other keys are available for options:

        F to press the function key instead
        T (plus others) for writing the time

        See OPTIONS defined below for what's available
"""

from plover.system import Stroke

LONGEST_KEY = 1

# set numbers for -FRPB block
NUMBERS = {
    "": "",
    "-F": "1",
    "-FP": "2",
    "-P": "3",
    "-FR": "4",
    "-FRPB": "5",
    "-FB": "5", # \ shape
    "-PB": "6",
    "-R": "7",
    "-RB": "8",
    "-B": "9",
    "-RP": "0", # / shape
    "-FRP": "00",  # top left corner
    "-FPB": "00",  # top right
    "-FRB": "000",  # bottom left
    "-RPB": ",000",  # bottom right
}

# then copy the layout for the -LGTS block
for key, value in NUMBERS.copy().items():
    keys = Stroke(key).keys()
    new_keys = set()
    for first, second in [("-F", "-L"), ("-P", "-T"), ("-R", "-G"), ("-B", "-S")]:
        if first in keys:
            new_keys.add(second)

    NUMBERS[Stroke(new_keys).rtfcre] = value


def function_key(x):
    if int(x) == 0 or int(x) > 12:
        raise KeyError
    return f"{{#F{x}}}"


OPTIONS = {
    "": lambda x: f"{{&{x}}}",
    "A": lambda x: "{^}" + x,  # Attach
    "TPH": lambda x: "-" + x,  # Negative
    "TPHA": lambda x: "{^}-" + x,  # Attach Negative
    "TP": function_key,  # Function key
    "EU": lambda x: f"{{#Super({x})}}",  # i3: Go to workspace x
    "*EU": lambda x: f"{{#Super(Shift({x}))}}",  # i3: Move to workspace x
    "AO": lambda x: x + "{}",  # separate numbers. AO like Emily spacing
    "O": lambda x: " ".join(x) + "{}",  # separate digits
    "T": lambda x: f"{x}:00",  # Time
    "TA": lambda x: f"{x}am",  # Time am
    "TO": lambda x: f"{x}pm",  # Time pm
    "T*": lambda x: f"{{^}}:{x}",  # Time (minutes)
    "TA*": lambda x: f"{{^}}:{x}am",  # Time (minutes) am
    "TO*": lambda x: f"{{^}}:{x}pm",  # Time (minutes) pm
    "P": lambda x: f"£{{^}}{{&{x}}}",  # Pounds
    "H": lambda x: f"${{^}}{{&{x}}}",  # dollars
}


def lookup(strokes):
    assert len(strokes) <= LONGEST_KEY

    stroke = Stroke(strokes[0])
    keys = stroke.keys()
    if "#" not in keys:
        raise KeyError

    options = stroke & Stroke("STKPWHRAO*EUDZ")
    digit1 = stroke & Stroke("-FRPB")
    digit2 = stroke & Stroke("-LGTS")

    output = ""
    output += NUMBERS[digit1.rtfcre]
    output += NUMBERS[digit2.rtfcre]

    if output == "":
        raise KeyError

    output = OPTIONS[options.rtfcre](output)

    return output
