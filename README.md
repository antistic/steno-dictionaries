# Plover dictionaries

These are my dictionaries for Plover.

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
