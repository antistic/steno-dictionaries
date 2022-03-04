#!/usr/bin/python
"""Generate a fingerspelling dictionary (and optionally find conflicts)

Usage:
    Edit the SPELLING and VARIANTS

    Run `python fingerspelling.py -h` for help

Limitations:
    Won't find conflicts in dictionaries that don't implement `.items()`, such as
    python dictionaries
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


def find_conflicts():
    from plover.dictionary import base as dictionary
    from plover.registry import registry
    from plover import system
    from plover.config import Config
    from plover.oslayer.config import CONFIG_FILE

    config = Config(CONFIG_FILE)
    config.load()
    registry.update()
    system.setup("English Stenotype")
    dicts = [
        dictionary.load_dictionary(path)
        for path, enabled in config["dictionaries"]
        if enabled
    ]

    conflicts = []
    fixes = {}
    for dict in dicts:
        dict_conflicts = []

        for key, value in dict.items():
            all_parts_conflict = True
            any_conflict = False
            suggestion = ""
            for stroke in key:
                if stroke in output.keys():
                    suggestion += output[stroke]
                    any_conflict = True
                else:
                    all_parts_conflict = False
                    break

            rtfcre = "/".join(key)
            if all_parts_conflict:
                if suggestion != output.get(rtfcre, ""):
                    fixes[rtfcre] = suggestion
                    dict_conflicts.append(f"{rtfcre:50}{value:30}{suggestion}")
            elif any_conflict:
                dict_conflicts.append(f"{rtfcre:50}{value}")

        if len(dict_conflicts) > 0:
            conflicts.append("-" * len(dict.path))
            conflicts.append(dict.path)
            conflicts.append("-" * len(dict.path))
            conflicts.append("\n".join(dict_conflicts))
            conflicts.append("")

    return conflicts, fixes


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a fingerspelling dictionary (and optionally find conflicts)"
    )
    parser.add_argument(
        "output_file",
        help="File to save the dictionary to (default: fingerspelling.json)",
        type=str,
        nargs="?",
        default="fingerspelling.json",
    )
    parser.add_argument(
        "--print-dictionary",
        help="Print dictionary to the console instead of saving it to a file",
        action="store_true",
    )
    parser.add_argument(
        "--conflicts",
        help=(
            "Find conflicts with your active dictionaries and saves the results to files. "
            "It will find if any stroke of a definition conflicts, and if all parts "
            "conflict, it will suggest a fix"
        ),
        action="store_true",
    )
    parser.add_argument(
        "--conflicts-file",
        help="File to save conflicts to (default: conflicts.txt)",
        type=str,
        default="conflicts.txt",
    )
    parser.add_argument(
        "--fixes-file",
        help="File to save conflict fixes suggestions to (default: fixes.json)",
        type=str,
        default="fixes.json",
    )
    parser.add_argument(
        "--print-conflicts",
        help="Print conflicts and fixes instead of saving to files",
        action="store_true",
    )

    args = parser.parse_args()

    output = generate_dictionary()

    if args.conflicts or args.print_conflicts:
        conflicts, fixes = find_conflicts()

        if args.print_conflicts:
            print("CONFLICTS\n")
            print("\n".join(conflicts))
        else:
            conflicts_file = Path(args.conflicts_file)
            conflicts_file.write_text("\n".join(conflicts))
            print(f"Wrote conflicts to {conflicts_file.resolve()}")

            fixes_file = Path(args.fixes_file)
            fixes_file.write_text(json.dumps(fixes, indent=4))
            print(f"Wrote fixes to {fixes_file.resolve()}")

    if args.print_dictionary:
        print("DICTIONARY\n")
        print(json.dumps(output, indent=2))
        print(f"\n{len(output.keys())} entries")
    else:
        output_path = Path(args.output_file)
        output_path.write_text(json.dumps(output, indent=2))

        print(
            f"Wrote dictionary ({len(output.keys())} entries) to {output_path.resolve()}"
        )
