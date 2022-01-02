#!/usr/bin/python
"""Numbers dictionary

Adapted from: /u/a589
https://www.reddit.com/r/Plover/comments/fgt6tp/list_of_alternative_number_systems/

Requirements:
    - python dictionary plugin (https://pypi.org/project/plover-python-dictionary/)
    - scripts/conflicts.py if you want to find conflicts with other dictionaries

Usage:
    Enter up to 3 digits at once

    - First digit: PWHR
    - Second digit: FRPB
    - Third digit: LGTS

    The corners are 1, 3, 7, 9.
    Adjacent keys give you the ones in between.

    Any diagonal gives 0.
    Any 3 with the top row gives 00.
    Any 3 with the bottom row gives 000.

    Modifiers at the bottom of the file.

Changes:
    - Modifiers
"""

LONGEST_KEY = 1

NUMBERS = {
    # RHWP
    0b0001: "1",
    0b0101: "2",
    0b0100: "3",
    0b0011: "4",
    0b1111: "5",
    0b1100: "6",
    0b0010: "7",
    0b1010: "8",
    0b1000: "9",
    0b1001: "0",
    0b0110: "0",
    0b0111: "00",
    0b1011: "000",
    0b1101: "00",
    0b1110: "000",
}


def function(x):
    if x == "0" or int(x) > 12:
        raise KeyError
    return f"{{#F{x}}}"


def lookup(strokes):
    assert len(strokes) <= LONGEST_KEY

    stroke = strokes[0]

    # first translate stroke into a set of keys
    key_prefix = ""
    keys = set()
    for c in stroke:
        i = "1234506789".find(c)
        if i > -1:
            c = "STPHAOFPLT"[i]
            keys.add("#")
        if c in "AO-*EU":
            key_prefix = "-"
            if c != "-":
                keys.add(c)
        else:
            keys.add(key_prefix + c)

    if "#" not in keys:
        raise KeyError

    groups = [
        sum((key in keys) << index for index, key in enumerate(group))
        for group in (
            ("S", "T", "K", "A", "O", "E", "U", "-D", "-Z"),
            ("P", "W", "H", "R"),
            ("-F", "-R", "-P", "-B"),
            ("-L", "-G", "-T", "-S"),
        )
    ]

    if all(x == 0 for x in groups[1:]):
        raise KeyError
    while groups[-1] == 0:
        groups.pop()
    if any(x == 0 for x in groups[1:]):
        raise KeyError

    main = "".join(NUMBERS[x] for x in groups[1:])

    # modifiers:
    main = {
        # ZDUEOAKTS
        0b000000000: lambda x: x,
        0b000001000: lambda x: "{^}" + x,  # A: Append
        0b000000001: lambda x: "-" + x,  # S: Minus
        0b000000010: function,  # T: Function (like in modifiers, TP=F)
        0b000001001: lambda x: "{^}-" + x,  # SA: Append minus
        0b000000011: lambda x: x + "{}",  # ST: SeparaTe numbers
        0b000000111: lambda x: " ".join(x) + "{}",  # SD: Separate Digits
        0b001100000: lambda x: "{^}[" + x + "]",  # I: Index
        0b001100001: lambda x: "{^}[-" + x + "]",  # SI: negative index
        0b000000101: lambda x: f"{{#Super(Shift({x}))}}",  # SK: move window to workspace x (i3)
        0b000000100: lambda x: f"{{#Super({x})}}",  # K: Change to workspace x (i3)
        0b000000110: lambda x: x + "{^}:{^}",  # D-: colon, e.g. for time
        0b010000000: lambda x: x + "am",  # D: am
        0b100000000: lambda x: x + "pm",  # Z: pm
    }[groups[0]](main)
    return main


if __name__ == "__main__":
    from scripts.conflicts import prepare, check_lookup_conflicts

    json_merged, python_lookups = prepare()

    check_lookup_conflicts(json_merged, python_lookups, lookup)
