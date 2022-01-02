#!/usr/bin/python
"""Find conflicts in your Plover dictionaries

Supports JSON-JSON and JSON-Python comparisons.

Adapted from:
https://discord.com/channels/136953735426473984/136953735426473984/835164920437538848


Usage:
    `python conflicts.py [-h] [--all] [ignore ...]`

    positional arguments:
    ignore      paths of dictionaries to ignore

    optional arguments:
    -h, --help  show this help message and exit
    --all       compare all registered dictionaries, not just enabled
"""

from collections import defaultdict
import json, glob, runpy, configparser, os, argparse
from plover.oslayer.config import CONFIG_FILE, CONFIG_DIR


def prepare(enabled_only=True, ignore=[]):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    system_name = config["System"]["name"]

    dictionaries = set(
        [
            os.path.join(CONFIG_DIR, d["path"])
            for d in json.loads(config["System: " + system_name]["dictionaries"])
            if not (enabled_only and not d["enabled"])
        ]
    )
    dictionaries = dictionaries - set(ignore)

    json_dictionaries = [d for d in dictionaries if os.path.splitext(d)[1] == ".json"]
    python_dictionaries = [d for d in dictionaries if os.path.splitext(d)[1] == ".py"]

    json_merged = defaultdict(list)
    json_reversed = defaultdict(list)

    for d_path in json_dictionaries:
        with open(d_path) as f:
            for k, v in json.load(f).items():
                json_merged[k].append((v, d_path))
                json_reversed[v].append((k, d_path))

    python_lookups = [
        (runpy.run_path(path)["lookup"], path) for path in python_dictionaries
    ]

    return json_merged, json_reversed, python_lookups


def print_conflicts(stroke, value, conflicts, json_reversed):
    if len(conflicts) > 0:
        message = [f"{stroke}: {value}"]
        for c in conflicts:
            if c[0] in json_reversed:
                alternatives = set(s[0] for s in json_reversed[c[0]])
                alternatives.discard(stroke)
                message.append(f"    {c[0]}")
                if len(alternatives) > 0:
                    message.append(
                        f"    ({len(alternatives)}) {','.join(alternatives)}"
                    )

        print("\n".join(message))


def check_strokes_conflicts(json_merged, json_reversed, python_lookups, dictionary):
    for stroke, value in dictionary.items():
        conflicts = [
            (v, f)
            for v, f in json_merged.get(stroke, [])
            # don't show conflict if it's redefined in this dictionary
            if v not in dictionary.values()
        ]
        for lookup, name in python_lookups:
            try:
                result = (lookup(tuple(stroke.split("/"))), name)
                conflicts.append(result)
            except Exception:
                pass

        print_conflicts(stroke, value, conflicts, json_reversed)


def check_lookup_conflicts(json_merged, json_reversed, python_lookups, lookup):
    for stroke, v in json_merged.items():
        conflicts = v

        try:
            value = lookup(tuple(stroke.split("/")))
            conflicts = [(v, f) for v, f in conflicts if v != value]

            # other python dictionaries
            for p_lookup, name in python_lookups:
                try:
                    result = (p_lookup(tuple(stroke.split("/"))), name)
                    conflicts.append(result)
                except Exception:
                    pass

            print_conflicts(stroke, value, conflicts, json_reversed)
        except Exception:
            pass


def check_all_conflicts(json_merged, python_lookups):
    for stroke, v in json_merged.items():
        conflicts = v
        for lookup, name in python_lookups:
            try:
                result = (lookup(tuple(stroke.split("/"))), name)
                conflicts.append(result)
            except Exception:
                pass

        if len(conflicts) > 1:
            print(f"{stroke}:")
            for c in conflicts:
                print(f"  |-> '{c[0]}' in '{c[1]}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find conflicts in your Plover dictionaries"
    )
    parser.add_argument(
        "--all",
        help="compare all registered dictionaries, not just enabled",
        action="store_true",
    )
    parser.add_argument("ignore", help="paths of dictionaries to ignore", nargs="*")
    args = parser.parse_args()

    json_merged, python_lookups = prepare(
        enabled_only=(not args.all),
        ignore=[os.path.abspath(path) for path in args.ignore],
    )

    check_all_conflicts(json_merged, python_lookups)
