# UK spelling

| File             | Description                                                               |
| ---------------- | ------------------------------------------------------------------------- |
| differences.json | Example differences file. Shows the spelling changes generated            |
| ignore.txt       | Example ignore file. List of words to not change the spelling of          |
| overrides.json   | Example overrides file. Override the spelling suggestions from the script |
| uk.json          | The generated dictionary                                                  |
| uk.md            | Other UK related dictionary changes that aren't covered by the script     |
| uk.py            | The script                                                                |
| README.md        | This file                                                                 |

## Script Usage

You need to have python installed and know how to use the command-line.

Run `python uk.py -h` for help.

```
$ python uk.py -h
usage: uk.py [-h] [--ignore-dicts IGNORE_DICTS] [--ignore-file IGNORE_FILE] [--overrides-file OVERRIDES_FILE]
             [--differences-file DIFFERENCES_FILE]
             [output_file]

Generate a dictionary with changed spellings

positional arguments:
  output_file           File to save the dictionary to (default: uk.json)

options:
  -h, --help            show this help message and exit
  --ignore-dicts IGNORE_DICTS
                        A comma separated list of base names of dictionaries to ignore (default: none). By
                        default there are none, so it will look through all your enabled dictionaries. For
                        example 'commands.json,main.json'
  --ignore-file IGNORE_FILE
                        Path to ignore file (default: ignore.txt). It should be a text file with each spelling to
                        ignore on a new line
  --overrides-file OVERRIDES_FILE
                        Path to overrides file (default: overrides.json). It should be a json file with a single
                        object where the key is the old spelling and the value is the new spelling
  --differences-file DIFFERENCES_FILE
                        Path to output the overrides file (default: differences.json). This is a json object of
                        old spellings to new spellings, useful for review
```

### Download the source dictionaries

The current settings rely on have two files called `en_GB-ise-large.text` and `en_US-large.txt` in this directory. These are dictionary files generated from <http://app.aspell.net/create>, using the default settings for **en\_GB-ise** and **en\_US**, but with the SCOWL size set to large.

Neither are provided in this repository because they're kind of big.

### Customising

You can edit the ignore and override files, or generate and use different source dictionaries. You may need to change `good_guesses` if you use a different source dictionary.
