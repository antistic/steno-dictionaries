# Plover dictionaries

## [Dictionaries](./)

### [Keypad Numbers](./keypad_numbers.py)

Numbers dictionary

**Adapted from**: [/u/a589's alternative number system](https://www.reddit.com/r/Plover/comments/fgt6tp/list_of_alternative_number_systems/)

**Usage**:

Enter up to 3 digits at once

- First digit: PWHR
- Second digit: FRPB
- Third digit: LGTS

The corners are 1, 3, 7, 9.<br>
Adjacent keys give you the ones in between.

Any diagonal gives 0.<br>
Any 3 with the top row gives 00.<br>
Any 3 with the bottom row gives 000.

Modifiers at the bottom of the file.

**Changes**:

- Modifiers

### [Modifiers Stack](./modifiers_stack.py)

Modifiers dictionary which allows you to stack keys

**Adapted from**: https://github.com/EPLHREU/emily-modifiers

**Changes**:

- different symbols
- right hand symbols
- keypad numbers
- if you run this file directly it will print out any conflicts this file has with any
  of your enabled json dictionaries
- stacking!

**Stacking**:

You can write each part of the original stroke separately, for example if you are
writing an uncommon key combination and would rather not arpeggiate, or if you want to
use right hand symbols.

**Examples**:

See the tests for more examples of valid and invalid combinations.

- `KPWRA*FRLTZ`: all together, like the original emily-modifiers
- `-FLTZ`, `WHAO`: modifiers first, then the key
- `-LTZ`, `-FP`, `SR`: starter, modifiers, key
- `-FLTZ`, `-R`, `-B`, `A`: add extra modifiers in between
- `-PLTZ`, `SKWH-B`: the above but end with right hand symbols

### [Symbols](./symbols.py)

Symbols Dictionary

**Adapted from**: https://github.com/EPLHREU/emily-symbols

**Changes**:

- different symbols
- single, non-# starter
- trailing spaces are explicitly added if attachment method is space
- if you run this file directly it will print out any conflicts this file has with any
  of your enabled json dictionaries

## [Scripts](./scripts)

### [Conflicts.py](./scripts/conflicts.py)

Find conflicts in your Plover dictionaries

**Usage**:
```
    `python conflicts.py [-h] [--all] [ignore ...]`

    positional arguments:
    ignore      paths of dictionaries to ignore

    optional arguments:
    -h, --help  show this help message and exit
    --all       compare all registered dictionaries, not just enabled
```

### [Fingerspelling.py](./scripts/fingerspelling.py)

Create a fingerspelling JSON dictionary

**Usage**:

`python fingerspelling.py` or use the generated file [fingerspelling.json](./fingerspelling.json)

**Key**:

This is slightly different to the default Plover dictionary — here, the plain `*` and
`*P` entries are attach, not glue, so that it's easier to use programs like vim.

The glue versions now exist under `*RBGS` and `*FPLT`.

| keys    | translation    | description      | plover                     |
| ------- | -------------- | ---------------- | -------------------------- |
| `*`     | `{^}{>}x{^}`   | attach lowercase | `{>}{&x}`                  |
| `*P`    | `{^}{-\|}x{^}` | attach uppercase | `{&X})`                    |
| `*FPLT` | `{>}{&x}`      | glue lowercase   | `{&X.}` (inconsistently)   |
| `*RBGS` | `{-\|}{&x}`    | glue uppercase   | `{>}{&x}` (inconsistently) |


**Conflicts**:

This dictionary has conflicts with the default plover dictionaries — run this file
with `SHOW_CONFLICTS = True` to see conflicts with your currently enabled
dictionaries (except `OUTPUT_FILE`). This requires you to also have
[conflicts.py](./scripts/conflicts.py) in the same directory as this file.

| stroke      | translation | alternative |
| ----------- | ----------- | ----------- |
| `A*FPLT`    | amount      | `APLT`      |
| `*ERBGS`    | {extra^}    | `ERBGS`     |
| `*EURBGS`   | issues      | `EURBS`     |
| `SKWR*RBGS` | {;}         | `SP-PT`     |
