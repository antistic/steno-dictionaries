# Finger Drill Dictionary

Dictionary for when you need to output raw strokes for drilling.

Requires:
- [plover_markdown_dictionary](https://github.com/antistic/plover_markdown_dictionary)
- [plover-dictionary-commands](https://pypi.org/project/plover-dict-commands/)

This dictionary will work well with the [Da Dreaded Dueling Digit
Duo](https://joshuagrams.github.io/steno-jig/finger-drills.html?section=1&iterations=20)
finger drills and the Steno Jig ["Learn the
Keyboard"](https://joshuagrams.github.io/steno-jig/learn-keyboard.html) drills.


## Dictionary Control

This expects this dictionary to be located in a `dictionaries` folder in the Plover
config folder. You'll need to change this if you put this dictionary somewhere else.

```yaml
(UPDATED) TPR*D: {PLOVER:SOLO_DICT:+dictionaries/finger_drills.md} # FR*D FingeR Drill
STPR*D: {PLOVER:END_SOLO_DICT} # SFR*D Stop FingeR Drill
```

## Steno Jig

```yaml
R*R: "{#Return}{^}" # Repeat: can't use R-R since it appears in "Left + Right" drill
STPH-G: "{#Right}{^}" # Next: default plover right arrow
STPH-R: "{#Left}{^}" # Back: default plover left arrow
STPH-B: "{#Down}{^}"
```
