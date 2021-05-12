"""Test modifiers_stack.py

Usage:
    `pytest modifiers_stack_test.py` or the containing directory. Requires pytest.
"""
from ..modifiers_stack import lookup

import pytest


def id_function(val):
    # hacky way for the test case names to look like: test_fn["STROEBG" -> "stroke"]
    if isinstance(val, tuple):
        # stroke
        return '"' + "/".join(val) + '" '
    else:
        # output string
        return f'> "{val}"'


class TestLookup:
    @pytest.mark.parametrize(
        "strokes,output",
        [
            (("-LTZ", "-F", "S-"), "{#control(s)}"),
            (("-LTZ", "-P", "-B", "-EU"), "{#super(alt(i))}"),
            (("-LTZ", "-P", "-B", "-R", "A-"), "{#super(shift(alt(a)))}"),
            (
                ("-LTZ", "-F", "-B", "-P", "-R", "TP-"),
                "{#super(shift(control(alt(f))))}",
            ),
        ],
        ids=id_function,
    )
    def test_simple(self, strokes, output):
        assert lookup(strokes) == output

    @pytest.mark.parametrize(
        "strokes,output",
        [
            (("-LTZ",), "{#}"),
            (("-LTZ", "F"), "{#}"),
            (("-FLTZ", "-R"), "{#}"),
        ],
        ids=id_function,
    )
    def test_incomplete(self, strokes, output):
        assert lookup(strokes) == output

    @pytest.mark.parametrize(
        "strokes,output",
        [
            (("-FLTZ", "EU"), "{#control(i)}"),
            (("-LTZ", "TP-R"), "{#shift(f)}"),
            (("-FLTZ", "TP-"), "{#control(f)}"),
            (("-FRLTZ", "TPH-"), "{#shift(control(n))}"),
        ],
        ids=id_function,
    )
    def test_partial_stack(self, strokes, output):
        assert lookup(strokes) == output

    @pytest.mark.parametrize(
        "strokes,output",
        [
            (("-LTZ", "-F", "-F", "S-"), "{#control(s)}"),
        ],
        ids=id_function,
    )
    def test_repeat_modifiers_okay(self, strokes, output):
        assert lookup(strokes) == output

    @pytest.mark.parametrize(
        "strokes,output",
        [
            (("-PLTZ", "TPH*"), "{#super(parenleft)}"),
            (("-BLTZ", "-F", "KHA*"), "{#control(alt(delete))}"),
            (("-BLTZ", "KHA*F"), "{#control(alt(delete))}"),
            (("-RLTZ", "KHAO*"), "{#shift(escape)}"),
        ],
        ids=id_function,
    )
    def test_symbols_left(self, strokes, output):
        assert lookup(strokes) == output

    @pytest.mark.parametrize(
        "strokes,output",
        [
            (("-LTZ", "-R", "SKWH-EURPBG"), "{#shift(down)}"),
            (("-FLTZ", "SKWH-FPBG"), "{#control(asciitilde)}"),
            (("-LTZ", "-RB", "SKWH-E"), "{#shift(alt(tab))}"),
        ],
        ids=id_function,
    )
    def test_symbols_right(self, strokes, output):
        assert lookup(strokes) == output

    @pytest.mark.parametrize(
        "strokes,output",
        [
            (("-LTZ", "-F", "PHAO"), "{#control(2)}"),
            (("-RLTZ", "WHAO"), "{#shift(0)}"),
            (("-LTZ", "-B", "TPWAO"), "{#alt(F4)}"),
            (("-PLTZ", "TPWRAO"), "{#super(F11)}"),
            (("TPHRAOFLTZ",), "{#control(F12)}"),
            (("-PLTZ", "-F", "TPRAO"), "{#super(control(F10))}"),
        ],
        ids=id_function,
    )
    def test_numbers(self, strokes, output):
        assert lookup(strokes) == output

    @pytest.mark.parametrize(
        "strokes,output",
        [
            (("TP-FLTZ",), "{#control(f)}"),
            (("O-PLTZ",), "{#super(o)}"),
            (("-EUBLTZ",), "{#alt(i)}"),
            (("SKP*PLTZ",), "{#super(ampersand)}"),
        ],
        ids=id_function,
    )
    def test_complete_stack(self, strokes, output):
        assert lookup(strokes) == output

    @pytest.mark.parametrize(
        "strokes",
        [
            ("KROL",),
            ("KP-", "-LTZ"),
        ],
        ids=id_function,
    )
    def test_fails_when_no_starter(self, strokes):
        with pytest.raises((AssertionError, KeyError)):
            lookup(strokes)

    @pytest.mark.parametrize(
        "strokes",
        [
            ("T-LTZ",),
            ("-LTZ", "S"),
            ("-LTZ", "-EU"),
            ("-LTZ", "SKWHUFRLG"),
        ],
        ids=id_function,
    )
    def test_fails_when_no_modifier(self, strokes):
        with pytest.raises((AssertionError, KeyError)):
            lookup(strokes)

    @pytest.mark.parametrize(
        "strokes",
        [
            ("-LTZ", "1", "2", "3", "4", "5", "6"),
        ],
        ids=id_function,
    )
    def test_fails_when_too_long(self, strokes):
        with pytest.raises((AssertionError, KeyError)):
            lookup(strokes)

    @pytest.mark.parametrize(
        "strokes",
        [
            ("S*FLTZ",),  # not a symbol (left)
            ("-LTZ", "-P", "SKWH*UFRBLG"),  # not a symbol (right)
            ("-BLTZ", "PHRAO-"),  # not a number
            ("-LTZ", "-RB", "SHR"),  # not a letter
        ],
        ids=id_function,
    )
    def test_fails_when_invalid_character(self, strokes):
        with pytest.raises((AssertionError, KeyError)):
            lookup(strokes)

    @pytest.mark.parametrize(
        "strokes",
        [
            ("-LTZ", "PRAOR"),  # 10
            ("-BLTZ", "PWRAO-"),  # 11
            ("-LTZ", "P", "WHRAO-"),  # 12
            ("TWHAOLTZ",),  # F0
        ],
        ids=id_function,
    )
    def test_fails_when_invalid_numbers(self, strokes):
        with pytest.raises((AssertionError, KeyError)):
            lookup(strokes)

    @pytest.mark.parametrize(
        "strokes",
        [
            ("-LTZ", "-F", "S-", "TPHUL"),
        ],
        ids=id_function,
    )
    def test_fails_when_multiple_characters(self, strokes):
        with pytest.raises((AssertionError, KeyError)):
            lookup(strokes)
