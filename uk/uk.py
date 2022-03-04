#!/usr/bin/python
"""Generate a dictionary with changed spellings
"""
import argparse
import json
from pathlib import Path

from plover.dictionary import base as dictionary
from plover.registry import registry
from plover import system
from plover.config import Config
from plover.oslayer.config import CONFIG_FILE

import enchant


def get_enabled_dicts(ignored):
    config = Config(CONFIG_FILE)
    config.load()
    registry.update()
    system.setup("English Stenotype")
    dicts = [
        dictionary.load_dictionary(path)
        for path, enabled in config["dictionaries"]
        if enabled and not Path(path).name in ignored
    ]

    return dicts


def main(dicts, overrides, ignore):
    # using dictionaries generated from http://app.aspell.net/create
    # they're the same as en_GB-ise and en_US, except the SCOWL size is large
    # these are NOT in git because they are very big
    new_spell = enchant.request_pwl_dict("en_GB-ise-large.txt")
    us_spell = enchant.request_pwl_dict("en_US-large.txt")

    # to use the default dictionaries that come with your system
    # comment out the above lines and uncomment these
    # new_spell = enchant.Dict("en_GB")
    # us_spell = enchant.Dict("en_US")

    differences = overrides.copy()
    new_dict = {}

    for dict in dicts:
        count = 0

        for key, value in dict.items():
            # don't do the same work twice
            if value in differences:
                rtfcre = "/".join(key)
                new_dict[rtfcre] = differences[value]
                continue

            # skip if already correct spelling
            if ignore.check(value) or new_spell.check(value):
                continue

            # skip things that *probably* aren't words
            # - if has punctuation/accents
            # - if not in US dict
            # - all uppercase
            if value.isupper() or not value.isalpha() or not us_spell.check(value):
                continue

            substitution = overrides.get(value, "")
            if not substitution:
                suggestions = new_spell.suggest(value)
                if len(suggestions) > 0:
                    good_guesses = {
                        value.replace("e", "ae", 1),
                        value.replace("e", "oe", 1),
                        value.replace("er", "re"),
                        value.replace("k", "c"),
                        value.replace("l", "ll"),
                        value.replace("o", "ou"),
                        value.replace("z", "s"),
                    }

                    substitution = suggestions[0]
                    for suggestion in suggestions:
                        if suggestion in good_guesses:
                            substitution = suggestion
                            continue

            differences[value] = substitution
            rtfcre = "/".join(key)
            new_dict[rtfcre] = substitution

            count += 1

        if count > 0:
            print(dict.path)
            print(count)
            print()

    return differences, new_dict


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a dictionary with changed spellings"
    )
    parser.add_argument(
        "output_file",
        help="File to save the dictionary to (default: uk.json)",
        type=str,
        nargs="?",
        default="uk.json",
    )
    parser.add_argument(
        "--ignore-dicts",
        help=(
            "A comma separated list of base names of dictionaries to ignore (default: none). "
            "By default there are none, so it will look through all your enabled dictionaries. "
            "For example 'commands.json,main.json'"
        ),
        type=str,
        default="",
    )
    parser.add_argument(
        "--ignore-file",
        help=(
            "Path to ignore file (default: ignore.txt). "
            "It should be a text file with each spelling to ignore on a new line"
        ),
        type=str,
        default="ignore.txt",
    )
    parser.add_argument(
        "--overrides-file",
        help=(
            "Path to overrides file (default: overrides.json). "
            "It should be a json file with a single object "
            "where the key is the old spelling and the value is the new spelling"
        ),
        type=str,
        default="overrides.json",
    )
    parser.add_argument(
        "--differences-file",
        help=(
            "Path to output the overrides file (default: differences.json). "
            "This is a json object of old spellings to new spellings, useful for review"
        ),
        type=str,
        default="differences.json",
    )

    args = parser.parse_args()

    ignore = enchant.request_pwl_dict(args.ignore_file)
    overrides = json.loads(Path(args.overrides_file).read_text())
    differences_path = Path(args.differences_file)
    output_path = Path(args.output_file)
    dicts = get_enabled_dicts(args.ignore_dicts)
    dicts.reverse()  # so that higher priority dicts overwrite lower ones

    differences, new_dict = main(dicts, overrides, ignore)

    print(f"{len(differences)} words changed in {len(new_dict)} entries")
    print()

    differences_path.write_text(json.dumps(differences, indent=4))
    output_path.write_text(json.dumps(new_dict, indent=4))
    print(f"Wrote differences to {differences_path.resolve()}")
    print(f"Wrote dictionary to {output_path.resolve()}")
