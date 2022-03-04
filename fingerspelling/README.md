# Fingerspelling

| File                | Description                                                   |
| ------------------- | ------------------------------------------------------------- |
| conflicts.txt       | Example conflicts file                                        |
| fingerspelling.json | The generated fingerspelling dictionary                       |
| fingerspelling.py   | The script used to generate the dictionary and find conflicts |
| fixes.json          | The generated suggested fixes dictionary                      |
| README.md           | This file                                                     |

## Usage

You need to have python installed and know how to use the command-line.

Run `python fingerspelling.py -h` for full help and usage instructions.

```
$ python fingerspelling.py -h
usage: fingerspelling.py [-h] [--print-dictionary] [--conflicts] [--conflicts-file CONFLICTS_FILE]
                         [--fixes-file FIXES_FILE] [--print-conflicts]
                         [output_file]

Generate a fingerspelling dictionary (and optionally find conflicts)

positional arguments:
  output_file           File to save the dictionary to (default: fingerspelling.json)

options:
  -h, --help            show this help message and exit
  --print-dictionary    Print dictionary to the console instead of saving it to a file
  --conflicts           Find conflicts with your active dictionaries and saves the results to files. It will find
                        if any stroke of a definition conflicts, and if all parts conflict, it will suggest a fix
  --conflicts-file CONFLICTS_FILE
                        File to save conflicts to (default: conflicts.txt)
  --fixes-file FIXES_FILE
                        File to save conflict fixes suggestions to (default: fixes.json)
  --print-conflicts     Print conflicts and fixes instead of saving to files
```

### Customising

You can edit `fingerspelling.py` to define your own fingerspelling rules.

- `SPELLING` is where you define which steno keys map to which letters. It'll also work for compound letters, like "th"
- `VARIANTS` is where you define letter variants, for example capital and lower case letters

### Conflicts

Passing `--conflicts` will find conflicts and suggest fixes. See the example `conflicts.txt` and `fixes.json`.

It will find conflicts in your enabled Plover dictionaries, but it'll only work for dictionaries which implement `items()`. In practice, this means that it won't check for conflicts in python dictionaries.

It may not load your configuration (in particular dictionary extensions) if you are running a different python environment than Plover, for example if you are using the AppImage.
